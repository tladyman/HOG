from scipy import misc
from Histogram import Histogram
from skimage.util import view_as_blocks


class Cell:
    """A container object to manage the cells. These are squares of pixels.

    Attributes:
        _pixelArray (numpy.ndarray): The arrays of pixels.
        cellArray: The array of cells to have 
    """

    histogram = Histogram()

    def __init__(self, blockArray, cellSizeX, cellSizeY):
        """Constructor from an input array, this should be a block object. Array should be 2x2 etc.

        Args:
            blockArray: The array of blocks
            cellSizeX: The number of pixels on the x axis of this Cell.
            cellSizeY: The number of pixels on the y axis of this Cell.
        """
        self._block = blockArray
        self.cellArray = view_as_blocks(pixelArray, block_shape, step)

