from setuptools import find_packages, setup

with open('{{ cookiecutter.package_name }}/VERSION', 'r') as version_file:
    VERSION = version_file.read().strip()

setup(
    name='{{ cookiecutter.package_name }}',
    version=VERSION,
    description='{{ cookiecutter.project_name }}',
    author='{{ cookiecutter.author_name }}',
    packages=find_packages('{{ cookiecutter.package_name }}'),
    {%- if cookiecutter.license != 'None' -%}license='{{ cookiecutter.license }}',{%- endif -%}
    python_requires='>=3.6'
)
