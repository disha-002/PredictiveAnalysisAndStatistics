from setuptools import setup, find_packages

setup(
    name="topsis-disha-102303705",
    version="0.0.2",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "topsis=topsis.topsis:main"
        ]
    },
    install_requires=["numpy", "pandas"]
)
