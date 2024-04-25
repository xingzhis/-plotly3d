from setuptools import setup, find_packages

setup(
    name="plotly3d",
    version="0.4.7",
    packages=find_packages(),
    install_requires=[
        "plotly",
        "scikit-learn",
        "pandas",
        "numpy",
    ],
    author="Xingzhi Sun",
    author_email="xingzhi.sun@yale.edu",
    description="A helper for ploting scatter plots and trajectory plots with plotly",
    keywords="plotly 3d plotting",
)
