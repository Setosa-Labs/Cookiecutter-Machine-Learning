'''Raw data acquisition'''

import click
import logging
from . import home_dir, LOG_FMT
from dotenv import find_dotenv, load_dotenv
from pathlib import Path


def download_dataset(output_dir=None):
    '''Download raw datasets.
    
    Retrieve data from source and output files into the directory specified 
    by `output_dir`. If `output_dir` is not specified, the directory defaults
    to:

        `{{ cookiecutter.package_name.upper() }}_HOME/datasets/raw/`

    Parameters
    ----------
    output_dir : path or str, optional
        Absolute path to output directory.

    Returns
    -------
    None
    '''
    if not output_dir:
        output_dir = home_dir('datasets', 'raw')

    if not output_dir.exists():
        output_dir.mkdir(parents=True)

    logger = logging.getLogger(__name__)
    logger.info('downloading raw dataset')
    
    # TODO: dataset download code
    pass


@click.command()
@click.option('--output_directory', required=False, type=click.Path(),
              help='Path to output directory.')
def cli_main(output_directory):
    '''Retrieve data from source and output files into the directory specified 
    by `output_directory`. If `output_directory` is not specified, the
    directory defaults to:

        `{{ cookiecutter.package_name.upper() }}_HOME/datasets/raw/`
    '''
    logging.basicConfig(level=logging.INFO, format=LOG_FMT)

    download_dataset(Path(output_directory))


if __name__ == '__main__':
    # Load environment variables by walking up the directory tree until .env
    # is found and then loading the .env file
    load_dotenv(find_dotenv())

    # Call the command-line interface
    cli_main()
