'''
This program implements a basic line scan-conversion (line drawing)
algorithm. This program uses the Python Imaging Library in order to
assist with line drawing.

'''

# Standard Libraries
import math
import decimal
import time

# Python Imaging Library
from PIL import Image

# Creates an empty black image
image = Image.new(mode="RGB", size = (250, 250), color = (0,0,0))
# image.show()