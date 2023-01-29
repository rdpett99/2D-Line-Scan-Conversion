'''
This program implements a basic line scan-conversion (line drawing)
algorithm. This program uses the Python Imaging Library in order to
assist with line drawing.

'''

# Standard Libraries
import math
import time
import decimal
from random import randint

# Image module from the Python Imaging Library
from PIL import Image

# Creates an empty black image
image = Image.new(mode = "RGB", size = (500, 500), color = (0,0,0))

# Used to round the timer to 5 significant figures
decimal.getcontext().prec = 5

def bresenham_alg(x0, y0, x1, y1):
    '''
    This function uses Bresenham's Line Drawing Algorithm
    to draw a line from coordinates (x0, y0) to (x1, y1).
    Meanwhile, this function also keeps track of the total
    time it takes for all lines to be drawn.

    Returns
    -------
    draw_time
        total time it takes to draw all lines

    '''

    # Used for calculating total time to draw all the given lines
    draw_time = 0

    # Assigns random RGB values to differenciate between different drawn lines.
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)