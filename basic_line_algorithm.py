'''
This program implements a basic line scan-conversion (line drawing)
algorithm. This program uses the Python Imaging Library in order to
assist with line drawing.

'''

# Standard Libraries
import math
import time
from decimal import Decimal, getcontext
from random import randint

# Image module from the Python Imaging Library
from PIL import Image

# Creates an empty black image
image = Image.new(mode = "RGB", size = (500, 500), color = (0,0,0))

def draw_line(x0, y0, x1, y1):
    '''
    This function draws a line starting at point (x0, y0) and ending at point 
    (x1, y1) in a standard coordinate system. While lines are being drawn, this
    function also keeps track of the amount of time it takes to draw all lines
    so it can be later displayed for the user.

    Returns
    -------
    draw_time
        total time it takes to draw one line

    '''

    # Used for calculating total time to draw all the given lines
    draw_time = 0

    # Used to round the timer to 5 significant figures
    getcontext().prec = 5

    # Assigns random RGB values to differenciate between different drawn lines.
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)

    # If x0 == x1 : the line is vertical
    if x0 == x1:
        y_min = min(y0, y1)

        # Starts the timer for the critical loop
        start_time = Decimal(time.perf_counter())

        # Critical loop
        for y_coord in range(abs(y1 - y0)):
            image.putpixel((x0, y_min + y_coord), (r, g, b))
        
        # Stops timer
        end_time = Decimal(time.perf_counter())

        # Calculates total time
        draw_time += (end_time - start_time)
    
    # Else, the line is not vertical
    else:
        
        # Calculates the slope and y-intercept
        slope = (y1 - y0) / (x1 - x0)
        y_intercept = y1 - (slope * x1)

        # Check if |x1 - x0| >= |y1 - y0|
        if (abs(x1 - x0) >= abs(y1 - y0)):
            x_min = min(x0, x1)

            # Starts timer
            start_time = Decimal(time.perf_counter())

            # Critical loop
            for x_coord in range(abs(x1 - x0) + 1):
                x = x_min + x_coord
                y = (slope * x) + y_intercept
                y = math.trunc(y)
                image.putpixel((x, y), (r, g, b))
            
            # Stops timer
            end_time = Decimal(time.perf_counter())

            # Calculates total time
            draw_time += (end_time - start_time)

        # Check if |x1 - x0| < |y1 - y0|
        elif (abs(x1 - x0) < abs(y1 - y0)):
            y_min = min(y0, y1)

            # Starts timer
            start_time = Decimal(time.perf_counter())

            # Critical loop
            for y_coord in range(abs(y1 - y0) + 1):
                y = y_min + y_coord
                x = (y - y_intercept) / slope
                x = math.trunc(x)
                image.putpixel((x, y), (r, g, b))
            
            # Stops timer
            end_time = Decimal(time.perf_counter())

            # Calculates total time
            draw_time += (end_time - start_time)

    return draw_time

# Debug
total = 0
total += draw_line(50, 100, 50, 200)
total += draw_line(75, 75, 237, 100)
total += draw_line(85, 45, 337, 20)
total += draw_line(30, 30, 80, 30)

print(f'Loop took {total} seconds long.')
image.show()