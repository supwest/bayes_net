import numpy as np
import pandas as pd
from sklearn.datasets import make_classification


class BaggedBN(object):
    '''
    Bagged BN classifier, like a random forest of Naive Bayes classifiers
    '''

    def __init__(self, n_estimators=10, n_features=1):
        self.n_estimators = n_estimators
        self.n_features = n_features
        self.chosen_features = None



    def fit(self, X):


    def _select_features(self, X):
        features_chosen = []
        features = [i for i in xrange(X.shape[1])]
        while len(features_chosen) < self.n_features:
            estimator_index = np.random.randint(len(features))
            features_chosen.append(features.pop(estimator_index))
        self.chosen_features = features_chosen



if __name__ == '__main__':

    data = make_classification(n_features = 5)
    
