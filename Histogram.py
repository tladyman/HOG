import numpy as np

class Histogram:
    """The histogram and associated methods.

    Attributes:
    histogramArray: An array of blocks. blocks.shape is of the form [a,b,c,d]
                    where a are all blocks from one row, b is how many per row
                    and (c,d) is the size of the block. So blocks[0][0] is the
                    first block from the first row. So if thinking about each 
                    block the shape of the array of blocks is (a,b).

    """
    def __init__(self, block, oBins=8):
        """Constructor from an input array. Array should be 2x2 etc.

        Args:
            block: Block object with blocks and cell arrays within it
            oBins: The number of orientation bins to create for the histogram.
                   default: 8
        """
        i = 7
