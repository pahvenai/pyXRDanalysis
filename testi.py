__author__ = 'Patrik Ahvenainen'

from Experimentals import Measurement
from Visualization import Basic as vs
from Experimentals import Analysis
import numpy as np

image = Measurement.ReadImage('../data/AgBeh_7min_004.raw32_2300')
print(image.shape)

pri = Analysis.findPrimary(image)

print np.sum(pri)

mx = np.ma.array(image, mask=pri)

vs.plot2Dimage(mx)

