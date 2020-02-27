import shutil
from pathlib import Path


def remove(path_or_str):
    '''Delete a file or directory'''
    path = Path(path_or_str)
    if path.is_dir():
        shutil.rmtree(path)
    elif path.is_file():
        path.unlink()


def script_main():
    root_dir = Path.cwd().resolve()

    if '{{ cookiecutter.license }}' == 'None':
        remove(root_dir / 'LICENSE.md')

    # Replace project home variable with absolute path
    with open(root_dir / '.env', 'r+', encoding='utf-8') as env_file:
        env_content = env_file.read().replace('${PWD}', str(root_dir))
        env_file.seek(0)
        env_file.write(env_content)
        env_file.truncate()


if __name__ == '__main__':
    script_main()
