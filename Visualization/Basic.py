__author__ = 'Patrik Ahvenainen'

import matplotlib.pyplot as plt

def plot2Dimage(image, picker=False, show=True, block=True):
    plt.imshow(image, picker=picker, interpolation='none')
    plt.hot()
    if show:
        plt.show(block=block)
    return plt

