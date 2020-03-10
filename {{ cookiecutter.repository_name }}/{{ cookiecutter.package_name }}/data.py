'''Raw data acquisition'''

import click
import logging
from . import home_dir, LOG_FMT
from dotenv import find_dotenv, load_dotenv
from pathlib import Path


def download_dataset(output_dir=None):
    '''Retrieves data from source and outputs files into the specified
    directory. If `output_dir` is not specified, the directory defaults to:

        `{{ cookiecutter.package_name.upper() }}_HOME/datasets/raw/`

    Parameters
    ----------
    output_dir : path or str, optional
        Absolute path to output directory.

    Returns
    -------
    None
    '''
    if output_dir:
        output_dir = Path(output_dir)
    else:
        output_dir = home_dir('datasets', 'raw')

    logger = logging.getLogger(__name__)
    logger.info('downloading raw dataset')
    
    pass  # download logic goes here


@click.command()
@click.option('--output_directory', required=False, type=click.Path(),
              help='Relative path to output directory.')
def script_main(output_directory):
    '''Retrieves data from source and outputs files into the specified 
    directory relative to the current working directory. If `output_dir` is not
    specified, the folder defaults to:

        `{{ cookiecutter.package_name.upper() }}_HOME/datasets/raw/`
    '''
    if output_directory:
        download_dataset(Path.cwd().joinpath(output_directory))
    else:
        download_dataset(None)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format=LOG_FMT)

    # Load environment variables by walking up the directory tree until .env
    # is found and then loading the .env file
    load_dotenv(find_dotenv())

    script_main()
