import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from scipy import misc
from skimage.util import view_as_windows, view_as_blocks
from Block import Block
from Histogram import Histogram
from Cell import Cell

test_holes_image = np.array([[0,0,0,0,0,0,1,0,0,0],
                             [0,1,1,1,1,1,0,0,0,0],
                             [0,1,1,1,1,1,0,0,0,0],
                             [0,1,1,1,1,1,0,0,0,0],
                             [0,1,1,1,1,1,0,0,0,0],
                             [0,0,0,0,0,0,0,2,2,2],
                             [0,0,0,0,0,0,0,2,0,2],
                             [0,0,0,0,0,0,0,2,2,2]])

def test_gradient_image():
    h = Hog(test_holes_image, 16, 16, 0.5, 8, 8)
    gx, gy = h._create_gradient_images(h._inputImage)

    expected_gx = np.array([[0,0,0,0,0, 1, 0,-1,0, 0],
                            [1,1,0,0,0,-1,-1, 0,0, 0],
                            [1,1,0,0,0,-1,-1, 0,0, 0],
                            [1,1,0,0,0,-1,-1, 0,0, 0],
                            [1,1,0,0,0,-1,-1, 0,0, 0],
                            [0,0,0,0,0, 0, 2, 2,0,-2],
                            [0,0,0,0,0, 0, 2, 0,0, 0],
                            [0,0,0,0,0, 0, 2, 2,0,-2]])

    expected_gy = np.array([[0, 1, 1, 1, 1, 1, 0, 0,0, 0],
                            [0, 1, 1, 1, 1, 1,-1, 0,0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0,0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0,0, 0],
                            [0,-1,-1,-1,-1,-1, 0, 2,2, 2],
                            [0,-1,-1,-1,-1,-1, 0, 2,0, 2],
                            [0, 0, 0, 0, 0, 0, 0, 0,0, 0],
                            [0, 0, 0, 0, 0, 0, 0,-2,0,-2]])

    expected_grad = np.arctan2(expected_gy, expected_gx)

    np.testing.assert_almost_equal(h.grad, expected_grad)

def testHog():
    """Tests our version of Hog with skimage's version"""
    

split = np.array([[1, 1, 5, 5, 9, 9,13,13,17,17,21,21],
                  [1, 1, 5, 5, 9, 9,13,13,17,17,21,21],
                  [2, 2, 6, 6,10,10,14,14,18,18,22,22],
                  [2, 2, 6, 6,10,10,14,14,18,18,22,22],
                  [3, 3, 7, 7,11,11,15,15,19,19,23,23],
                  [3, 3, 7, 7,11,11,15,15,19,19,23,23],
                  [4, 4, 8, 8,12,12,16,16,20,20,24,24],
                  [4, 4, 8, 8,12,12,16,16,20,20,24,24]])

