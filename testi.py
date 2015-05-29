__author__ = 'Patrik Ahvenainen'

from Experimentals import Measurement
from Visualization import Basic as vs

image = Measurement.ReadImage('../data/test_image.tif')
print(image.shape)

vs.plot2Dimage(image)
