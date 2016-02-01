from scipy import ndimage
from scipy import misc
import matplotlib.pyplot as plt


class Hog:
    """A container object to manage the HOG algorithm.

    Attributes:
        _inputImage (numpy.ndarray): The raw unprocessed input image.

    """

    def __init__(self, filename, blockSizeX, blockSizeY, overlap, cellSizeX, cellSizeY):
        """Constructor from an input image.

        Args:
            filename: Filename of input image e.g. 'test.png'.
            blockSizeX: The number of cells on the x axis of the Blocks. The
                size in pixels is blockSizeX*cellSizeX
            blockSizeY: The number of cells on the y axis of the Blocks. The
                size in pixels is blockSizeY*cellSizeY
            overlap: Fraction of overlap between Blocks.
            cellSizeX: The number of pixels on the x axis of the Cells within
                this Block.
            cellSizeY: The number of pixels on the y axis of the Cells within
                this Block.

        """
        # load the image
        self._inputImage = misc.imread(filename)
        plt.imshow(self._inputImage, cmap=plt.cm.gray)
        plt.show()

        # Create the Blocks and store in a 2D array/list in this object
