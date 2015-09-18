__author__ = 'Patrik Ahvenainen'

import numpy as NP
import scipy as SP
import matplotlib.pyplot as plt

class Component(object):
    """
    This class in intended as a basic heritable class for all components of an X-ray scattering set-up. The purpose of
    Components is to save the experimental set-up used in a standardized way. Anyone not familiar with an experiment
    should be able to easily get the specs of the set-up and there should be no ambiguity on what devices/components
    were used.
    """
    def __init__(self,manufacturer,model='n/a',manufactureYear='',comment=''):
        self._manufacturer = manufacturer
        self._model = model
        self._manufactureYear = manufactureYear
        self._comment = comment

    @classmethod
    def addComment(self,comment):
        self._comment = self._comment + comment
    @classmethod
    def replaceComment(self,comment):
        self._comment = comment



