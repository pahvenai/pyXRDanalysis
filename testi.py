__author__ = 'Patrik Ahvenainen'

from Experimentals import Measurement
from Visualization import Basic as vs
from Experimentals import Analysis
import numpy as np

image = Measurement.ReadImage('../data/tupla_alumiinifolio_15min_003.raw32_2300')

mask = Analysis.createMask(image)

print np.shape(mask)

mx = np.ma.array(image, mask=mask)

vs.plot2Dimage(mx)

