import shutil
from pathlib import Path

def remove(path_or_str):
    '''Delete a file or directory'''
    path = Path(path_or_str)
    if path.is_dir():
        shutil.rmtree(path)
    elif path.is_file():
        path.unlink()

if '{{ cookiecutter.license }}' == 'None':
    remove(Path.cwd() / 'LICENSE.md')
