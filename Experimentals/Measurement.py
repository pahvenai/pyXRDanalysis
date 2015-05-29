__author__ = 'Patrik Ahvenainen'

from Experimental import Experimental
import matplotlib.pyplot as plt
import os
import numpy as np
class Measurement(Experimental):
    def __init__(self,scientist,dateRange,supervisor='n/a',institution='n/a',comment=''):
        super.__init__(scientist,dateRange,supervisor,institution,comment)

def ReadImage(filepath):
    """
    Reads a 2D scattering image from a file.
    Supported file types: -
    """
    fileName, fileExtension = os.path.splitext(filepath)
    fileExtension = fileExtension.lower() # ignore case

    print(fileName,fileExtension)

    if fileExtension in ['.tif', '.tiff']:
        return ReadTiffImage(filepath)

    raise TypeError('File extension not supported.')

def ReadTiffImage(filepath):
    image = plt.imread(filepath)
    return(np.array(image))
