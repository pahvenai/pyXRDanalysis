__author__ = 'Patrik Ahvenainen'

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def plot2Dimage(image, picker=False, show=True, block=True, clim=None, alpha=1):
    """
    Plots the image as a 2D plot. If the color limits are given, some hopefully useful default limits are calculated and
    used. This function is intended for basic plotting purposes.

    :param image:
    :param picker:
    :param show:
    :param block:
    :param clim:
    :return:
    """
    #cmap = mpl.colors.Colormap('afmhot', N=512)
    #cmap.set_bad(color=u'k', alpha=None)

    # This code tries to make the default color limits sensible with most scattering data
    if not clim:
        min_val = np.amin(image)
        image_corr = image - min_val + 1
        image_corr = np.log(image_corr)

        median_val = np.median(image_corr)
        max_val = np.amax(image_corr)

        cmin_val = median_val
        cmax_val = max_val
        clim = (cmin_val, cmax_val)

    else:
        image_corr = np.log(image+1)

    plt.imshow(image_corr, picker=picker, interpolation='none', alpha=alpha)

    # adjust colormap
    plt.hot()
    plt.clim(clim)

    if show:
        plt.show(block=block)
    return plt

