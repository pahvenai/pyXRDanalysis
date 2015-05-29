__author__ = 'Patrik Ahvenainen'

import numpy as NP
import scipy as SP
import matplotlib.pyplot as plt

class Component(object):
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



