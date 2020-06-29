### Globals ###

SHELL=/bin/bash
PROJECT_ENV = {{ cookiecutter.package_name }}


### Environment ###

environment:
	conda create --name $(PROJECT_ENV)

remove_environment:
	conda env remove --name $(PROJECT_ENV)


### Dependencies

dependencies:
	source $$(conda info --base)/etc/profile.d/conda.sh;\
	conda activate $(PROJECT_ENV);\
	conda env update --name $(PROJECT_ENV) --file environment.yml --prune;\
	pip install --editable . --no-deps;\
	conda deactivate

export_dependencies:
	conda env export --name $(PROJECT_ENV) --no-builds --from-history | grep -v "^prefix:" > environment.yml

lint:
	flake8 test_project
