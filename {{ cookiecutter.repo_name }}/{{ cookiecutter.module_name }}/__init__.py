import os
from pathlib import Path


LOG_FMT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


def cache_dir(*sub_dirs):
    '''Path to the application cache directory for data and serialized models.

    The environment is checked for the following environment variable:
        `{{ cookiecutter.module_name.upper() }}_HOME`
    If the variable exists, it is used as the path prefix. If the variable is 
    not defined, the path prefix defaults to the user's home directory. The
    path is then joined with each argument of `sub_dirs`.

    Parameters
    ----------
    *sub_dirs : variable-length str argument list
        Subdirectories or files to be appended to the cache directory path

    Returns
    -------
    path : path with subdirectories appended
    '''
    if '{{ cookiecutter.module_name.upper() }}_HOME' in os.environ:
        path = Path(os.getenv('{{ cookiecutter.module_name.upper() }}_HOME'))
    else:
        path = Path.home() / '.{{ cookiecutter.module_name }}'

    return path.joinpath(*sub_dirs) if sub_dirs else path
