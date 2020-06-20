'''Model definition, training and validation'''

import click
import logging
import pickle
from . import home_dir, LOG_FMT
from dotenv import find_dotenv, load_dotenv
from pathlib import Path


class ModelManager:
    '''Machine learning model manager.

    Attributes
    ----------
    model : object
        The machine learning model object.
    version : object
        A string-serializable object to represent the version of the `model`
        object.

    Methods
    -------
    serialize(model_path)
        Persist the current model to the file specified by `model_path`.
    deserialize(model_path)
        Deserialize a model from the file specified by `model_path`.
    fit(y, X)
        Fit a model to target vector `y` with respect to data matrix `X`.
    predict(X)
        Predict values for y with respect to data matrix `X`.
    '''

    def __init__(self, model=None, version=1):
        self.model = model
        self.version = version

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, version_value):
        # Enforce version invariants here
        self._version = version_value

    def serialize(self, model_path):
        '''Persist a model with version metadata to disk.
        
        Parameters
        ----------
        model_path : path-like object
            A path-like object giving the pathname (absolute or relative to
            the current working directory) of the file to persist the model to.

        Returns
        -------
        None
        '''
        with open(model_path, 'wb') as model_file:
            pickle.dump(self, model_file)

    def deserialize(self, model_path):
        '''Retrieve a persisted model with version metadata from disk.
        
        Parameters
        ----------
        model_path : path-like object
            A path-like object giving the pathname (absolute or relative to
            the current working directory) of the file to deserialize the
            model from.

        Returns
        -------
        None
        '''
        with open(model_path, 'rb') as model_file:
            model_manager = pickle.load(model_file)

        self.version = model_manager.version
        self.model = model_manager.model

    def fit(self, y, X):
        '''Fit a model to target vector `y` with respect to data matrix `X`.
        
        Parameters
        ----------
        y : (M,) array_like
            Vector of target variable values
        X : (M,N) array_like
            Data matrix of input variable values

        Returns
        -------
        None
        '''
        pass  # Finalized training code

    def predict(self, X):
        '''Predict values for `y` with respect to data matrix `X`.
        
        Parameters
        ----------
        X : (M,N) array_like
            Data matrix of input variable values

        Returns
        -------
        y : (M,) array_like
            Vector of predicted values
        '''
        pass  # Code for prediction


def train_model(input_dir, model_path):
    '''Train and serialize a model.

    Read datasets from directory `input_dir`, train the corresponding model
    and persist the model to disk at path `model_path`. If `input_dir` is not
    specified, the input directory defaults to:

        `{{ cookiecutter.package_name.upper() }}_HOME/datasets/processed/`

    If `model_path` is not specified, the path defaults to:

        `{{ cookiecutter.package_name.upper() }}_HOME/models/model.pkl`

    Parameters
    ----------
    input_dir : path-like object, optional
    model_path : path-like object, optional

    Returns
    -------
    None
    '''
    if not input_dir:
        input_dir = home_dir('datasets', 'processed')

    if not model_path:
        model_path = home_dir('models', 'model.pkl')

    if not model_path.parent.exists():
        model_path.parent.mkdir(parents=True)

    logger = logging.getLogger(__name__)
    logger.info('training model')

    # TODO: Model training code
    pass


@click.command()
@click.option('--input_directory', required=False, type=click.Path(),
              help='Path to input directory.')
@click.option('--output_model', required=False, type=click.Path(),
              help='Path to output model.')
def cli_main(input_directory, output_model):
    '''Read datasets from directory `input_directory`, train the corresponding
    model and persist the model to disk at path `output_model`. If
    `input_directory` is not specified, the input directory defaults to:

        `{{ cookiecutter.package_name.upper() }}_HOME/datasets/processed/`

    If `output_model` is not specified, the path defaults to:

        `{{ cookiecutter.package_name.upper() }}_HOME/models/model.pkl`
    '''
    logging.basicConfig(level=logging.INFO, format=LOG_FMT)

    train_model(Path(input_directory), Path(output_model))


if __name__ == '__main__':
    # Load environment variables by walking up the directory tree until .env
    # is found and then loading the .env file
    load_dotenv(find_dotenv())

    # Call the command-line interface
    cli_main()
