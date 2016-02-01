from scipy import misc
from Cell import Cell


class Block:
    """A container object to manage the blocks. These are rectangles of cells.

    Attributes:
        _pixelArray (numpy.ndarray): The arrays of pixels.

    """

    def __init__(self, pixelArray, blockSizeX, blockSizeY, overlap, cellSizeX, cellSizeY, xpos, ypos):
        """Constructor from an input array. Array should be 2x2 etc.

        Args:
            pixelArray: The array of pixels.
            blockSizeX: The number of cells on the x axis of this Block. The
                size in pixels is blockSizeX*cellSizeX
            blockSizeY: The number of cells on the y axis of this Block. The
                size in pixels is blockSizeY*cellSizeY
            overlap: Fraction of overlap between Blocks.
            cellSizeX: The number of pixels on the x axis of the Cells within
                this Block.
            cellSizeY: The number of pixels on the y axis of the Cells within
                this Block.
            xpos: x position in grid
            ypos: y position in grid
        """
        self._pixelArray = pixelArray

        # Create the cells and store in a 2D array/list in this object
