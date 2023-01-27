'''
This program implements a basic line scan-conversion (line drawing)
algorithm. This program uses the Python Imaging Library in order to
assist with line drawing.

'''

# Standard Libraries
import math
import time
import decimal

# Python Imaging Library
from PIL import Image

# Creates an empty black image
image = Image.new(mode="RGB", size = (250, 250), color = (0,0,0))
decimal.getcontext().prec = 5

'''
This function draws a line starting at point (x0, y0) and ending at point 
(x1, y1) in a standard coordinate system.

'''
def draw_line(x0, y0, x1, y1):
    # If x0 == x1 : the line is vertical
    if x0 == x1 and y0 != y1:
        # Need the smallest y value to know if line is going up or down
        y_min = min(y0, y1)

        # Starts the timer for the critical loop
        start_time = decimal.Decimal(time.time())

        # Critical loop
        for y_coord in range(abs(y1 - y0)):
            image.putpixel((x0, y_min + y_coord), (255, 0, 255))
        
        # Stops timer
        end_time = decimal.Decimal(time.time())

        # Debug
        print(f'Loop took {end_time - start_time} seconds long.')
        image.show()

draw_line(50, 50, 50, 100)