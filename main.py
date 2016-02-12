from Hog import Hog
import numpy as np
from PIL import Image
# Load an image and initialise a Hog Object with it
#inputImage = Image.open('test.png').convert("L")
inputImage = Image.open('per00110.ppm').convert("L")
hogObject = Hog(np.asarray(inputImage), 16, 16, 0.5, 8, 8, 9)
