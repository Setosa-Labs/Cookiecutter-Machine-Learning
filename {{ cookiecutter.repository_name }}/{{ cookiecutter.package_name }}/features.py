'''Feature engineering from raw data'''

import click
import logging
from . import home_dir, LOG_FMT
from dotenv import find_dotenv, load_dotenv
from pathlib import Path


def construct_features(input_dir=None, output_dir=None):
    '''Construct features for model training.
    
    Transform raw data in the `input_dir` directory into features for model 
    input in the `output_dir` directory. If `input_dir` is not specified, the 
    input directory defaults to:

        `{{ cookiecutter.package_name.upper() }}_HOME/datasets/processed/`
    
    If `output_dir` is not specified, the output directory defaults to:

        `{{ cookiecutter.package_name.upper() }}_HOME/datasets/raw/`

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
    if not input_dir:
        input_dir = home_dir('datasets', 'raw')

    if not output_dir:
        output_dir = home_dir('datasets', 'processed')

    if not output_dir.exists():
        output_dir.mkdir(parents=True)

    logger = logging.getLogger(__name__)
    logger.info('creating features')

    # TODO: Feature engineering code
    pass


@click.command()
@click.option('--input_directory', required=False, type=click.Path(),
              help='Path to input directory.')
@click.option('--output_directory', required=False, type=click.Path(),
              help='Path to output directory.')
def cli_main(input_directory, output_directory):
    '''Transform raw data in the `input_directory` into features for model
    input in the `output_directory`. If `input_directory` directory is not 
    specified, the input directory defaults to:

        `{{ cookiecutter.package_name.upper() }}_HOME/datasets/raw/`
    
    If `output_directory` is not specified, the output directory defaults to:

        `{{ cookiecutter.package_name.upper() }}_HOME/datasets/processed/`
    '''
    logging.basicConfig(level=logging.INFO, format=LOG_FMT)

    construct_features(Path(input_directory), Path(output_directory))


if __name__ == '__main__':
    # Load environment variables by walking up the directory tree until .env
    # is found and then loading the .env file
    load_dotenv(find_dotenv())

    # Call the command-line interface
    cli_main()
