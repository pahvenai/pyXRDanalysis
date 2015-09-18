__author__ = 'Patrik Ahvenainen'

from Experimental import Experimental
from Visualization import Basic
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from scipy.spatial.distance import euclidean as distance
import pylab as plb
import numpy as np
from PIL import Image, ImageDraw

class Analysis(Experimental):
    pass

class EventCatcher(object):
    def __init__(self):
        self.key_pressed = 'OrriMorri'
        self.fig = None
        self.cid = None

    def pick_key_press(self,fig):
        self.fig = fig
        self.cid = fig.canvas.mpl_connect('button_press_event', self.key_press)
        plt.show()

    def key_press(self, event):
        self.key_pressed = event.button
        self.fig.canvas.mpl_disconnect(self.cid)
        return self.key_pressed

def onclick(event):
    print 'button=%d, x=%d, y=%d, xdata=%f, ydata=%f'%(
        event.button, event.x, event.y, event.xdata, event.ydata)


def findPrimary(image):
    """
    Gives the user the possibility to find the region of the primary
    beam are by selecting a region from the image.

    :param image:
    :return pri:
    """

    fig = plt.figure()
    ax1 = fig.add_subplot(111, aspect='equal')
    Basic.plot2Dimage(image, picker=True, show=True, block=False)
    pri = _selectRegion(image, ax1)
    plt.show()

    return pri

def createMask(image):
    """
    A mask can be used to mask out parts of the image that are not interesting.

    :param image:
    :return mask:
    """

    # plot the image
    fig = plt.figure()
    ax1 = fig.add_subplot(111, aspect='equal')
    Basic.plot2Dimage(image, picker=True, show=True, block=False)

    maskregions = list()
    mask = np.zeros(image.shape)

    while True:
        plt.title('Click on the image to add a new region to the mask.\nPress Enter to finish the mask.')
        pts = plt.ginput(1, 0, show_clicks=False)
        if len(pts) < 1:
            break
        print pts, len(pts)

        maskregions.append(_selectRegion(image, ax1))
        for region in maskregions:
            mask = mask + region

    plt.title('Masking finished.')

    return mask


def _selectRegion(image, axes=None):
    """
    Select a region on an image. The region can be a rectangle, circle or
    a polygon.

    :param image: The original image is used to create a shape of the same size as the original
    :param axes: If axes are other than the current ones, they can be given
    :return region: A mask of the same size as the original image. Selected shape is marked with ones.
    """

    # This allows the user to zoom in to the interesting area before selecting a region
    plt.title('Zoom around the region of interest. \nPress Enter when finished.')
    plt.ginput(0, 0, show_clicks=False)
    plt.title("Select a rectangle by clicking inside the two corner pixels. \nFor a circle click on the origin and "
              "press enter.")
    pts = plb.ginput(0, 0)
    pts_np = np.array(pts, dtype=float)

    if len(pts_np) == 0:
        return None

    # if only two points are used, draw a rectangle using these two points
    if len(pts_np) == 2:
        # add two more points to form a rectangle
        pts.insert(1, (pts[1][0], pts[0][1]))
        pts.append((pts[0][0], pts[2][1]))
        pts_np = np.array(pts)


    # A circle is drawn by first choosing the origin. The rest of this section is used to select the radius.
    if len(pts_np) == 1:

        origin = pts_np[0]

        # We need axes for this part
        if not axes:
            axes = plt.gca()

        plt.title('Select radius. ')
        xy = plb.ginput(0,0)  # This should be implemented to more complex shapes later
        xy_np = np.array(xy[0])  # This should be implemented to more complex shapes later
        radius = distance(origin, xy_np)

        # For visualization
        circle = patches.Circle(origin, radius, fc='w', alpha=0.5)
        axes.add_patch(circle)

        # create the actual polygon
        # more points for bigger circles
        n_points = max(int(radius * np.pi), 10000)
        pts = list()
        for point in range(1, n_points+1):
            theta = point * (2*np.pi / float(n_points))
            pts.append( tuple(list(origin+(radius*np.sin(theta), radius*np.cos(theta)))) )

    else:
        # For visualization, draw the (non-circular) polygon here if circle was not chosen
        patchi = patches.Polygon(pts_np, alpha=0.5, fc='w')
        if axes:
            axes.add_patch(patchi)
        # create the actual polygon

    # This image is used to create the shape
    width, height = image.shape
    img = Image.new('L', (width, height), 0)
    ImageDraw.Draw(img).polygon(pts, outline=1, fill=1)
    region = np.array(img)

    return region
