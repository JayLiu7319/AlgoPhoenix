from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="您的项目名称",
    version="0.1.0",
    author="您的姓名",
    author_email="您的邮箱",
    description="项目的简短描述",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/您的用户名/您的项目名称",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "Flask==2.0.1",
        "pandas==1.3.3",
        "numpy==1.21.2",
        "SQLAlchemy==1.4.25",
        "requests==2.26.0",
        "python-dotenv==0.19.0",
    ],
)