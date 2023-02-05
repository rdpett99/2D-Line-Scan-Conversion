'''
This program implements Bresenham's Line Drawing algorithm.
This program uses the Python Imaging Library in order to
assist with line drawing.

'''

# Standard Libraries
import time
from decimal import Decimal, getcontext
from random import randint

# Image module from the Python Imaging Library
from PIL import Image

# Creates an empty black image
image = Image.new(mode = "RGB", size = (500, 500), color = (0,0,0))

def bresenham_alg(x0, y0, x1, y1):
    '''
    This function uses Bresenham's Line Drawing Algorithm
    to draw a line from coordinates (x0, y0) to (x1, y1).
    Meanwhile, this function also keeps track of the total
    time it takes for all lines to be drawn.

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

        # Check if |x1 - x0| >= |y1 - y0|
        if abs(x1 - x0) >= abs(y1 - y0):

            # If x0 > x1, switch values of each coordinate pair
            if x0 > x1:
                (x0, x1) = (x1, x0)
                (y0, y1) = (y1, y0)
            
            # Calculates slope, delta x, and delta y, and E
            slope = (y1 - y0) / (x1 - x0)
            dx = abs(x1 - x0)
            dy = abs(y1 - y0)
            big_e = 2 * dy - dx

            # Calculates each increment value and x, y, and x_max values for loop
            inc1 = 2 * dy
            inc2 = 2 * (dy - dx)
            x = x0
            y = y0
            x_max = max(x0, x1)

            # Starts timer for loop
            start_time = Decimal(time.perf_counter())

            # Critical loop
            while True:
                image.putpixel((x, y), (r, g, b))
                if big_e < 0:
                    big_e += inc1
                else:
                    # if slope >= 0, y += 1; otherwise y -= 1
                    if slope >= 0:
                        y += 1
                    else:
                        y -= 1
                    big_e += inc2
                x += 1
                if x >= x_max:
                    break
            
            # Stops timer once loop breaks
            end_time = Decimal(time.perf_counter())

            # Calculates total time
            draw_time += (end_time - start_time)
        
        # else if |y1 - y0| > |x1 - x0|
        elif abs(y1 - y0) > abs(x1 - x0):

            # If y0 > y1, switch values of each coordinate pair
            if y0 > y1:
                (x0, x1) = (x1, x0)
                (y0, y1) = (y1, y0)
            
            # Calculates slope, delta x, and delta y, and E
            slope = (y1 - y0) / (x1 - x0)
            dx = abs(x1 - x0)
            dy = abs(y1 - y0)
            big_e = 2 * dx - dy

            # Calculates each increment value and x, y, and y_max values for loop
            inc1 = 2 * dx
            inc2 = 2 * (dx - dy)
            x = x0
            y = y0
            y_max = max(y0, y1)

            # Starts timer for loop
            start_time = Decimal(time.perf_counter())

            # Critical loop
            while True:
                image.putpixel((x, y), (r, g, b))
                if big_e < 0:
                    big_e += inc1
                else:
                    # if slope >= 0, x += 1; otherwise x -= 1
                    if slope >= 0:
                        x += 1
                    else:
                        x -= 1
                    big_e += inc2
                y += 1
                if y >= y_max:
                    break
            
            # Stops timer once loop breaks
            end_time = Decimal(time.perf_counter())

            # Calculates total time
            draw_time += (end_time - start_time)

    return draw_time

# Debug
total = 0
total += bresenham_alg(50, 100, 50, 200)
total += bresenham_alg(75, 75, 237, 100)
total += bresenham_alg(85, 45, 337, 20)
total += bresenham_alg(30, 30, 80, 30)

print(f'Loop took {total} seconds long.')
image.show()