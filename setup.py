from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="AlgoPhoenix",
    version="0.1.0",
    author="JayLiu",
    author_email="JayLiu7319@gmail.com",
    description="5步12级经典算法复现计划",
    long_description="5步12级经典算法复现计划",
    long_description_content_type="text/markdown",
    url="https://github.com/JayLiu7319/AlgoPhoenix",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.10",
    install_requires=[
        "fastapi==0.115.0",
    ],
)
