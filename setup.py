from setuptools import setup, find_packages

setup(
    name="glaes",
    version="1.3.4",
    author="Severin Ryberg",
    url="https://github.com/coroa/glaes",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "geokit>=1.4.0",
        "gdal>=3,<4",
        "numpy",
        "descartes",
        "pandas",
        "scipy",
        "matplotlib",
        "tqdm",
    ],
)
