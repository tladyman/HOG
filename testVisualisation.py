import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from scipy import misc

from HistogramPlotter import HistogramPlotter

img = np.zeros((100, 100), dtype=np.uint8)
histogram = np.zeros((200, 100, 9), dtype=np.uint8)

plotter = HistogramPlotter(img, histogram)

plotter.drawLine(50,50,30, 48, 1)

plt.imshow(plotter.getOutput(), cmap=plt.cm.gray, interpolation="nearest")
plt.show()
