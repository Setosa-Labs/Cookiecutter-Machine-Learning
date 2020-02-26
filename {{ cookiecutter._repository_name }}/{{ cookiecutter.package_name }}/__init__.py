import importlib.resources as res
import os
from pathlib import Path


with res.open_text('{{ cookiecutter.package_name }}', 'VERSION') as version_file:
    __version__ = version_file.read().strip()


def home_dir(*sub_dirs):
    '''Path to the application home directory for data and serialized models.

    The environment is checked for the following environment variable:

        `{{ cookiecutter._envvar_prefix }}_HOME`

    If the variable exists, it is used as the path prefix and each argument of
    `sub_dirs` is appended to the path. If the variable is not defined, the
    path prefix defaults to the following directory located in the user's home:

        `.{{ cookiecutter.package_name }}`

    Parameters
    ----------
    *sub_dirs : variable-length str argument list
        Subdirectories or files to be appended to the home directory path

    Returns
    -------
    path : path with subdirectories appended
    '''
    if '{{ cookiecutter.module_name.upper() }}_HOME' in os.environ:
        path = Path(os.getenv('{{ cookiecutter._envvar_prefix }}_HOME'))
    else:
        path = Path.home() / '.{{ cookiecutter.package_name }}'

    return path.joinpath(*sub_dirs) if sub_dirs else path


LOG_FMT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'