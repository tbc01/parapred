from setuptools import setup

setup(
    name="parapred",
    packages=["parapred"],
    entry_points={
        "console_scripts": ['parapred = parapred.parapred:main']
    },
    version="1.0.1",
    description="Deep-learning-powered antibody binding site prediction.",
    author="E Liberis",
    author_email="el398@cam.ac.uk",
    url="https://github.com/eliberis/parapred",
    package_data={"parapred": ["data/*.csv", "precomputed/*"]}
)
