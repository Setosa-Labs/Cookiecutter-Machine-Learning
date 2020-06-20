'''Model definition, training and validation'''

import pickle
from . import home_dir
from pathlib import Path


class ModelManager:
    '''Machine learning model manager.

    Attributes
    ----------
    model : object
        The machine learning model object.
    version : object
        A string-serializable object to represent the version of the model
        object.

    Methods
    -------
    serialize(model_path)
        Persist the current model to the file specified by model_path.
    deserialize(model_path)
        Deserialize a model from the file specified by model_path.
    fit(y, X)
        Fit a model to target vector y with respect to data matrix X.
    predict(X)
        Predict values for y with respect to data matrix X.
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
            the current working directory) of the file to serialize the model
            to.

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
        '''Fit a model to target vector y with respect to data matrix X.
        
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
        '''Predict values for y with respect to data matrix X.
        
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
