'''Feature engineering from raw data'''

import click
import logging
from . import home_dir, LOG_FMT
from dotenv import find_dotenv, load_dotenv
from pathlib import Path


def create_features(input_dir=None, output_dir=None):
    '''Transforms raw data in the `input_dir` directory and outputs features 
    for training into the `output_dir` directory. If `output_dir` is not
    specified, the directory defaults to:

        `{{ cookiecutter.package_name.upper() }}_HOME/datasets/raw/`

    If the `input_dir` directory is not specified, it defaults to:

        `{{ cookiecutter.package_name.upper() }}_HOME/datasets/processed/`

    Parameters
    ----------
    input_dir : path or str, optional
        Absolute path to input directory.
    output_dir : path or str, optional
        Absolute path to output directory.

    Returns
    -------
    None
    '''
    if input_dir:
        input_dir = Path(input_dir)
    else:
        input_dir = home_dir('datasets', 'raw')

    if output_dir:
        output_dir = Path(output_dir)
    else:
        output_dir = home_dir('datasets', 'processed')

    logger = logging.getLogger(__name__)
    logger.info('creating features')

    pass  # Feature engineering logic goes here


@click.command()
@click.option('--input_directory', required=False, type=click.Path(),
              help='Relative path to input directory.')
@click.option('--output_directory', required=False, type=click.Path(),
              help='Relative path to output directory.')
def script_main(input_directory, output_directory):
    '''Transforms raw data in the `input_dir` directory relative to the current
    working directory and outputs features for training into the `output_dir` 
    directory relative to the current working directory. If `output_dir` is not
    specified, the directory defaults to:

        `{{ cookiecutter.package_name.upper() }}_HOME/datasets/raw/`

    If the `input_dir` directory is not specified, it defaults to:

        `{{ cookiecutter.package_name.upper() }}_HOME/datasets/processed/`
    '''
    if output_directory:
        output_dir = Path.cwd().joinpath(output_directory)
    else:
        output_dir = None

    if input_directory:
        input_dir = Path.cwd().joinpath(input_directory)
    else:
        input_dir = None

    create_features(input_dir, output_dir)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format=LOG_FMT)

    # Load environment variables by walking up the directory tree until .env
    # is found and then loading the .env file
    load_dotenv(find_dotenv())

    script_main()
