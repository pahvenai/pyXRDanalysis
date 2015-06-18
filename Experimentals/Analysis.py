__author__ = 'Patrik Ahvenainen'

from Experimental import Experimental
from Visualization import Basic
import matplotlib.pyplot as plt
import matplotlib.patches as patches
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
    beam are by selecting a rectangle.

    :param image:
    :return pri:
    """

    fig = plt.figure()
    ax1 = fig.add_subplot(111, aspect='equal')
    Basic.plot2Dimage(image,picker=True,show=True,block=False)
    plt.title('Zoom around the primary region. \nPress Enter when finished.')
    plt.ginput(0,0,show_clicks = False)

    plt.title("Select a rectangle by clicking inside the two corner pixels.")
    pts = plb.ginput(0, 0)  # This should be implemented to more complex shapes later
    pts_np = np.array(pts)  # This should be implemented to more complex shapes later
    # pts = np.array(plb.ginput(2, 0))
    print("clicked",pts)

    # if only two points are used, draw a rectangle using these two points
    if len(pts_np) == 2:
        # xMin = round(min(pts_np[:, 0]))
        # xMax = round(max(pts_np[:, 0]))
        # yMin = round(min(pts_np[:, 1]))
        # yMax = round(max(pts_np[:, 1]))
        # pri = np.zeros_like(image)
        # pri[xMin:xMax+1][yMin:yMax+1] = 1
        #
        # ax1.add_patch(patches.Rectangle((xMin-0.5, yMin-0.5), width=xMax-xMin+1, height=yMax-yMin+1, alpha=0.5, fc='w'))
        # plt.draw()

        # add two more points to form a rectangle
        pts.insert(1, (pts[1][0], pts[0][1]))
        pts.append((pts[0][0], pts[2][1]))
        pts_np = np.array(pts)

    # For visualization
    patchi = patches.Polygon(pts_np, alpha=0.5, fc='w')
    ax1.add_patch(patchi)

    # For actual masking
    width, height = image.shape
    img = Image.new('L', (width, height), 0)
    ImageDraw.Draw(img).polygon(pts, outline=1, fill=1)
    pri = np.array(img)

    #origin = (np.mean(pts_np[:, 0]), np.mean(pts_np[:, 1]))

    plt.show()

    return pri
