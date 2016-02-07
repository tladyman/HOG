import numpy as np

class Histogram:
    """The histogram and associated methods.

    Attributes:
    histArray: An array of blocks. blocks.shape is of the form [a,b,c,d]
                    where a are all blocks from one row, b is how many per row
                    and (c,d) is the size of the block. So blocks[0][0] is the
                    first block from the first row. So if thinking about each 
                    block the shape of the array of blocks is (a,b).

    """
    def __init__(self, gradBlock, magBlock, oBins=9):
        """Constructor from an input array. Array should be 2x2 etc.

        Args:
            gradBlock: Block object with blocks and cell arrays within it of the
                       gradient image
            magBlock: Block object with blocks and cell arrays within it of the
                      magnitude image
            oBins: The number of orientation bins to create for the histogram.
                   default: 9 (optimum used in Dalal and Triggs)
        """
        
        # The magnitude image and the gradient image have the same structure
        # for the array (i.e. each element of a particular position in one array
        # corresponds to the that position in the other array)

        # Put cell arrays into variables
        gradCells = gradBlock.cellArray
        magCells = magBlock.cellArray

        # Create array of bins using equal bins between 0 and pi (signed)
        # because histogram requires end points the num of points must be one greater
        # than the number of bins.
        bins = np.linspace(-np.pi, np.pi, num=obins + 1)

        # dim1 and dim2 are the shape of the first two dimensions of the cellArray
        # dim3 is the histogram which is a 1d array (therefore no dim4)
        dim1 = gradCells.shape[0]
        dim2 = gradCells.shape[0]
        dim3 = len(bins)

        accumulator = np.zeros((dim1, dim2, dim3))

        for i, row in enumerate(gradCells):
            for j, col in enumerate(row):
                # At this point we have cells! and magBlock[i,j] will give us the
                # corresponding mag block.
                weights = magBlock[i,j]

                # histogram gives us the option of using a weights array so that
                # the magnitude provides votes rather than adding 1 each time.
                hist, bin_edges = np.histogram(col, bins, weights=weights)

                # Put the corresponding histogram into the accumulator

        self.histArray = accumulator

