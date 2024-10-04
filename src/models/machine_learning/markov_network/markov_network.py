import numpy as np
from typing import List, Dict, Tuple

class MarkovNetwork:
    def __init__(self, variables: List[str], cliques: List[List[str]]):
        self.variables = variables
        self.cliques = cliques
        self.factors = {tuple(clique): np.random.rand(2**len(clique)) for clique in cliques}
        self.var_to_clique = self._build_var_to_clique()

    def _build_var_to_clique(self) -> Dict[str, List[Tuple[str, ...]]]:
        var_to_clique = {var: [] for var in self.variables}
        for clique in self.cliques:
            for var in clique:
                var_to_clique[var].append(tuple(clique))
        return var_to_clique

    def _calculate_energy(self, state: Dict[str, int]) -> float:
        energy = 0
        for clique, factor in self.factors.items():
            idx = sum(state[var] * (2**i) for i, var in enumerate(clique))
            energy += np.log(factor[idx])
        return -energy

    def gibbs_sampling(self, num_samples: int, burn_in: int = 100) -> List[Dict[str, int]]:
        state = {var: np.random.randint(2) for var in self.variables}
        samples = []

        for _ in range(num_samples + burn_in):
            for var in self.variables:
                state[var] = 0
                energy_0 = self._calculate_energy(state)
                state[var] = 1
                energy_1 = self._calculate_energy(state)

                prob_1 = 1 / (1 + np.exp(energy_1 - energy_0))
                state[var] = np.random.choice([0, 1], p=[1-prob_1, prob_1])

            if _ >= burn_in:
                samples.append(state.copy())

        return samples

    def train(self, data: List[Dict[str, int]], learning_rate: float = 0.01, num_epochs: int = 100):
        for _ in range(num_epochs):
            for clique, factor in self.factors.items():
                grad = np.zeros_like(factor)
                for sample in data:
                    idx = sum(sample[var] * (2**i) for i, var in enumerate(clique))
                    grad[idx] += 1 / factor[idx]

                model_samples = self.gibbs_sampling(len(data))
                for sample in model_samples:
                    idx = sum(sample[var] * (2**i) for i, var in enumerate(clique))
                    grad[idx] -= 1 / factor[idx]

                self.factors[clique] += learning_rate * grad / len(data)
            print(self.factors)

    def inference(self, evidence: Dict[str, int], query_var: str, num_samples: int = 1000) -> float:
        samples = self.gibbs_sampling(num_samples)
        consistent_samples = [s for s in samples if all(s[k] == v for k, v in evidence.items())]
        return sum(s[query_var] for s in consistent_samples) / len(consistent_samples)

# 示例用法
if __name__ == "__main__":
    variables = ["A", "B", "C"]
    cliques = [["A", "B"], ["B", "C"]]
    mn = MarkovNetwork(variables, cliques)

    # 生成一些训练数据
    train_data = [
        {"A": 0, "B": 1, "C": 1},
        {"A": 1, "B": 1, "C": 0},
        {"A": 0, "B": 0, "C": 1},
        {"A": 1, "B": 0, "C": 0},
    ]

    # 训练模型
    mn.train(train_data, learning_rate=0.01, num_epochs=100)

    # 进行推理
    evidence = {"A": 1, "B": 1}
    query_var = "C"
    prob_c = mn.inference(evidence, query_var)
    print(f"P(C=1 | A=1, B=1) ≈ {prob_c:.3f}")
    