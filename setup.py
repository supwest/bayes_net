from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
        name='bayesnet'
        version='0.0.1-SNAPSHOT'
        description='Bayesian Network package for Python'
        long_decsription=readme,
        author="Cully West"
        url="https://github.com/supwest/bayes_net"
        license=license,
        packages=find_packages(exclude=("tests", "docs"))
)
