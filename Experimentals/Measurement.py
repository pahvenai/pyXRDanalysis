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

    Supported file types:
    .tif / .tiff
    .rawXXXX / .raw32_XXXX
    """
    fileName, fileExtension = os.path.splitext(filepath)
    fileExtension = fileExtension.lower() # ignore case

    if fileExtension in ['.tif', '.tiff']:
        return ReadTiffImage(filepath)
    if fileExtension[0:4] == '.raw':
        return ReadRawImage(filepath, fileExtension)

    raise TypeError('File extension not supported.')

def ReadTiffImage(filepath):
    image = plt.imread(filepath)
    return(np.array(image))

def ReadRawImage(filepath, fileExtension, shape=None):
    """
    Works only for raw files where extensions starts
    with 'raw' and ends in the size of the data.
    The data shape can be given in the parameter shape.

    :param filepath: Path to the data file
    :param fileExtension: The file extension, including a period
    :return read_data: read image from raw file
    """

    if not shape:
        # Read data size
        matrix_size = int(fileExtension[-4:])
        shape = (matrix_size, matrix_size)  # Assume square data matrix

    # Find out bitsize
    if fileExtension[4:7] == '32_':
        datatype = np.uint32
    else:
        datatype = np.uint16

    filein = open(filepath, 'rb')
    read_data = np.fromfile(file=filein, dtype=datatype).reshape(shape)
    return read_data
