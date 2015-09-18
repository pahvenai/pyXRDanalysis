__author__ = 'Patrik Ahvenainen'

from Experimentals import Measurement
from Visualization import Basic as vs
from Experimentals import Analysis
import numpy as np

image = Measurement.ReadImage('../data/tupla_alumiinifolio_15min_003.raw32_2300')

pri = Analysis.findPrimary(image)

print np.shape(pri)

mx = np.ma.array(image, mask=pri)

vs.plot2Dimage(mx)

