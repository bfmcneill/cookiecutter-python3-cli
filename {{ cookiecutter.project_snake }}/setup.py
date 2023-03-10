from setuptools import setup, find_packages

setup(
    name="{{ cookiecutter.project_snake }}",
    version="0.1.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "pcmd={{ cookiecutter.project_snake }}.cli:main",
        ],
    },
)
