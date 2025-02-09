from setuptools import find_packages
import setuptools

setuptools.setup(
    name="jina-executors",
    version="0.0.1",
    author='Jina Dev Team',
    author_email='dev-team@jina.ai',
    description="A selection of Executors for Jina",
    url="https://github.com/jina-ai/executors",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(where='.', include=['jinahub.*']),
    python_requires=">=3.7",
)
