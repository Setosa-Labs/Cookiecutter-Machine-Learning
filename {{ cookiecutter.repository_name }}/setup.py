from setuptools import find_packages, setup

with open('{{ cookiecutter.module_name }}/VERSION', 'r') as version_file:
    VERSION = version_file.read().strip()

setup(
    name='{{ cookiecutter.module_name }}',
    version=VERSION,
    description='{{ cookiecutter.project_name }}',
    author='{{ cookiecutter.owner }}',
    packages=find_packages('{{ cookiecutter.module_name }}'),{% if cookiecutter.license != 'None' %}
    license='{{ cookiecutter.license }}',
    {% endif %}python_requires='>=3.6'
)
