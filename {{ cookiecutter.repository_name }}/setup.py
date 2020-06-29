from setuptools import find_packages, setup
from pathlib import Path

with open(Path('{{ cookiecutter.package_name }}') / 'VERSION', 'r') as file:
    __version__ = file.read().strip()

setup(
    name='{{ cookiecutter.package_name }}',
    version=__version__,
    description='{{ cookiecutter.project_name }}',
    author='{{ cookiecutter.author_name }}',
    packages=find_packages('{{ cookiecutter.package_name }}'),
    {%- if cookiecutter.license != 'None' -%}license='{{ cookiecutter.license }}',{%- endif -%}
    python_requires='>=3.7'
)
