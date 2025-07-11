from setuptools import find_packages, setup


def parse_requirements(file):
    with open(file, "r") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]


setup(
    name="MaskTerial",
    version="0.1",
    packages=find_packages(),
    install_requires=parse_requirements("requirements.txt"),
    entry_points={
        "console_scripts": [],
    },
    author="Jan-Lucas Uslu",
    author_email="janlucas.uslu@gmail.com",
    description="A package for detecting 2D Material flakes",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jaluus/MaskTerial",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
)
