from Hog import Hog
from Cell import Cell
from Block import Block
from Histogram import Histogram
import numpy as np

test_holes_image = np.array([[0,0,0,0,0,0,1,0,0,0],
                             [0,1,1,1,1,1,0,0,0,0],
                             [0,1,0,0,1,1,0,0,0,0],
                             [0,1,1,1,0,1,0,0,0,0],
                             [0,1,1,1,1,1,0,0,0,0],
                             [0,0,0,0,0,0,0,1,1,1],
                             [0,0,0,0,0,0,0,1,0,1],
                             [0,0,0,0,0,0,0,1,1,1]])

def test_gradient_image():
    