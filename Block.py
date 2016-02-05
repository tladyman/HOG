from scipy import misc
from Cell import Cell


class Block:
    """A container object to manage the blocks. These are rectangles of cells.

    Attributes:
        _pixelArray (numpy.ndarray): The arrays of pixels.
        blockArray: An array of blocks. blocks.shape is of the form [a,b,c,d]
                        where a are all blocks from one row, b is how many per row
                        and (c,d) is the size of the block. So blocks[0][0] is the
                        first block from the first row. So if thinking about each 
                        block the shape of the array of blocks is (a,b).

    """

    def __init__(self, pixelArray, blockSizeX, blockSizeY, overlap, cellSizeX, cellSizeY):
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
        """
        self._pixelArray = pixelArray

        # Create the cells and store in a 2D array/list in this object
        # Calculate step from overlap and block size
        # NB This will be calculated as the minimum of either the x or y steps
        step_x = floor(overlap * blockSizeX)
        step_y = floor(overlap * blockSizeY)

        step = min(step_x, step_y)
        block_shape = (blockSizeY, blockSizeX)

        self.blockArray = view_as_windows(pixelArray, block_shape, step)
