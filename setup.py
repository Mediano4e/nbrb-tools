from setuptools import setup, find_packages


setup(
    name="nbrb-tools",
    version="0.1.0",
    description="A Python library that provides tools to work conveniently with the https://api.nbrb.by/",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Mediano4e",
    author_email="mediano4e@gmail.com",
    license="MIT",
    packages=find_packages(where="nbrb"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8, <3.13",
    install_requires=[
        "requests>=2.32.3",
    ],
)
