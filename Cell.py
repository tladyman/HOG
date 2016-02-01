from scipy import misc
from Histogram import Histogram

class Cell:
    """A container object to manage the cells. These are squares of pixels.

    Attributes:
        _pixelArray (numpy.ndarray): The arrays of pixels.

    """

    histogram = Histogram()

    def __init__(self, pixelArray, cellSizeX, cellSizeY):
        """Constructor from an input array. Array should be 2x2 etc.

        Args:
            pixelArray: The array of pixels.
            cellSizeX: The number of pixels on the x axis of this Cell.
            cellSizeY: The number of pixels on the y axis of this Cell.

        """
        self._pixelArray = pixelArray
