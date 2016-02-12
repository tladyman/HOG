import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from scipy import misc
from skimage.draw import line_aa
from skimage.draw import line
import math

from Histogram import Histogram

class HistogramPlotter:
    """Plot the histograms onto an output image

    Attributes:


    """

    def __init__(self, inputImage, histogramArray):
        """Constructor

        """
        self._inputImage = inputImage
        self._histogramArray = histogramArray

        # Draw an output
        self._outputImage = np.zeros_like(self._inputImage)

        print(self._outputImage.shape)
        print(self._histogramArray.shape)

        #plt.imshow(self._outputImage, cmap=plt.cm.gray, interpolation="nearest")
        #plt.show()

    def plot(self):
        # Cells are 8x8 with 50% overlap so centres are 4px apart
        xStep = 4
        yStep = 4

        yPos = yStep
        # Iterate through the histogram array
        for y in range(self._histogramArray.shape[0]):
            xPos = xStep
            for x in range(self._histogramArray.shape[1]):
                # For each cell find the largest histogram bin
                maxValue = 0
                maxIndex = 0
                for z in range(self._histogramArray.shape[2]):
                    thisValue = self._histogramArray[y,x,z]
                    if(thisValue > maxValue):
                        maxValue = thisValue
                        maxIndex = z
                # Draw the line
                self.drawLine(xPos,yPos,20*maxIndex, 2, 1)
                # Move the x position to the next centre
                xPos += xStep
            # Move the y position to the next row
            yPos += yStep
        # Plot
        plt.imshow(self.getOutput(), cmap=plt.cm.gray, interpolation="nearest")
        plt.show()

    def drawLine(self, centerX, centerY, angle, length, colour):
        """Plot a line from an angle, length and center
        Parameters:
            colour: 0:1 intensity percentage

        Attributes:

        """
        # Calculate the offset of the start and end from the center
        radAngle = math.radians(angle)
        xOffset = length * math.cos(radAngle)
        yOffset = length * math.sin(radAngle)

        # Calculate start and finish of the lines
        startx = math.floor(centerX - xOffset)
        stopx = math.floor(centerX + xOffset)
        starty = math.floor(centerY - yOffset)
        stopy = math.floor(centerY + yOffset)
        # Draw the line onto the array
        rr, cc, val = line_aa(starty, startx, stopy, stopx)
        #rr, cc = line(starty, startx, stopy, stopx)
        self._outputImage[rr, cc] = colour * 255

    def getOutput(self):
        return self._outputImage
