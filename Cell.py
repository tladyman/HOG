import numpy as np
from scipy import misc
from skimage.util import view_as_blocks
from Histogram import Histogram


class Cell:
    """A container object to manage the cells. These are rectangles of pixels.

    Attributes:
        _blockArray (numpy.ndarray): The arrays of pixels.
        cellArray: The array of cells to have 
    """

    def __init__(self, blockArray, cellSizeX, cellSizeY):
        """Constructor from an input array, this should be a block object.

        Args:
            blockArray: The array of blocks, should be two dimensional.
            cellSizeX: The number of pixels on the x axis of this Cell.
            cellSizeY: The number of pixels on the y axis of this Cell.
        """
        self._blockArray = blockArray

        (block_row, block_col, block_y, block_x) = blockArray.shape

        cell_shape = (cellSizeY, cellSizeX)

        practice = view_as_blocks(blockArray[0,0], cell_shape)
        (cell_row, cell_col, cell_y, cell_x) = practice.shape

        dim1 = block_row * cell_row
        dim2 = block_col * cell_col

        cellArray = np.zeros((dim1, dim2, cellSizeY, cellSizeX))

        for i, row in enumerate(blockArray):
            for j, col in enumerate(row):
                cell = view_as_blocks(col, (cellSizeY, cellSizeX))
                to_add_y = cell_row * i
                to_add_x = cell_col * j

                for k, cRow in enumerate(cell):
                    for l, cCol in enumerate(cRow):
                        # position to put the cell into
                        y_position = k + to_add_y
                        x_position = l + to_add_x

                        # put cell into cellArray
                        cellArray[y_position, x_position,: ,:] = cCol

        self.cellArray = cellArray

