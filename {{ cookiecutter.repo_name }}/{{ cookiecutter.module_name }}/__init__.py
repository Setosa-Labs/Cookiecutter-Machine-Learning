import os
from pathlib import Path

def cache_dir(*sub_dirs):
    if '{{ cookiecutter.module_name.upper() }}_HOME' in os.environ:
        path = Path(os.getenv('{{ cookiecutter.module_name.upper() }}_HOME'))
    else:
        path = Path.home() / '.{{ cookiecutter.module_name }}'

    return path.joinpath(*sub_dirs) if sub_dirs else path

LOG_FMT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
