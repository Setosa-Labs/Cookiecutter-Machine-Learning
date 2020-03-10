'''Model definition, training and validation'''

from . import home_dir
from pathlib import Path


class ModelHandler:
    '''Class for working with models'''

    def __init__(self):
        self.model = None

    def fit(self, y, X):
        '''Fit model to data matrix X and response vector y
        
        Parameters
        ----------
        y : (M,) array_like
            Target values
        X : (M,N) array_like
            Training data

        Returns
        -------
        None
        '''
        pass  # Finalized training code

    def predict(self, X):
        '''Predict values y for samples X 
        
        Parameters
        ----------
        X : (M,N) array_like
            Samples

        Returns
        -------
        y : (M,) array_like
            Predicted values
        '''
        pass  # Code for prediction

    def serialize(self, model_path):
        '''Persist the model'''
        if model_path:
            model_path = Path(model_path)
        else:
            model_path = home_dir('')

        pass

    def deserialize(self, model_path):
        '''Retrieve a persisted model'''
        if model_path:
            model_path = Path(model_path)
        else:
            model_path = home_dir('')

        pass
