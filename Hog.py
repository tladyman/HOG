import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from scipy import misc
from skimage.util import view_as_windows
from Block import Block
from Histogram import Histogram
from Cell import Cell


class Hog:
    """A container object to manage the HOG algorithm.

    Attributes:
        _inputImage (numpy.ndarray): The raw unprocessed input image.
        grad
        mag
        gradBlock
        magBlock
    """

    def __init__(self, filename, blockSizeX, blockSizeY, overlap, cellSizeX, cellSizeY, oBins):
        """Constructor from an input image.

        Args:
            filename: Filename of input image e.g. 'test.png'. 
                It can also takes a numpy array
            blockSizeX: The number of cells on the x axis of the Blocks. The
                size in pixels is blockSizeX*cellSizeX
            blockSizeY: The number of cells on the y axis of the Blocks. The
                size in pixels is blockSizeY*cellSizeY
            overlap: Fraction of overlap between Blocks.
            cellSizeX: The number of pixels on the x axis of the Cells within
                this Block.
            cellSizeY: The number of pixels on the y axis of the Cells within
                this Block.
            oBins: Number of orientation bins

        """
        if type(filename) == str:
            # load the image
            self._inputImage = misc.imread(filename)
        elif type(filename) == np.ndarray:
            self._inputImage = filename
        else:
            raise TypeError("That is not a valid input")

        # plt.imshow(self._inputImage, cmap=plt.cm.gray, interpolation="nearest")
        # plt.show()

        # Calculate gradient and magnitude arrays and then create Blocks for each of them
        gx, gy = self._create_gradient_images(self._inputImage)

        # Create block objects for each the magnitude and gradient images.
        self.gradBlock = Block(self.grad, blockSizeX, blockSizeY, overlap, cellSizeX, cellSizeY)
        self.magBlock = Block(self.mag, blockSizeX, blockSizeY, overlap, cellSizeX, cellSizeY)

        # Create histogram object - which takes the gradient Block object and the 
        # magnitude Block object
        self.histogram = Histogram(self.gradBlock, self.magBlock, oBins)

        self.output = self.histogram.histArray


    def _create_gradient_images(self,pixelArray):
        """Creates gradient images in x and y directions.

        Args:
            pixelArray: The array of pixels

        Returns:
            grad: gradient image 
            mag: gradient in the y direction
        """

        # Create the column and row vectors to convolve

        ker = np.array([1,0,-1])

        column = ker.reshape((3,1))
        row = ker.reshape((1,3))

        # mode = constant ensures that the edges of the image ar padded with
        # constant values in this case the default is 0 - perfect for our purposes. 
        # The array is then restored to its original dimensions.

        # Convolve the vectors to create gradients in x and y directions
        gx = ndimage.filters.convolve(pixelArray, row, mode = "constant")
        gy = ndimage.filters.convolve(pixelArray, column, mode = "constant")

        # Create gradient image using arctan2 (remember its in radians!)
        self.grad = np.arctan2(gy,gx)

        # The square of each element is just matrix^2 in python
        self.mag = np.sqrt(gx**2 + gy**2)

        return gx, gy
