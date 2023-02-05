'''
This is the main program which is responsible for taking
user input and passing along arguments to each of the line-drawing
algorithms.

'''

# Standard Library
from random import randint

# My Modules
import basic_line_algorithm as basic
import bresenham_line_algorithm as bresenham

prompt = "\nHow many lines do you wish to display? "
num_of_lines = int(input(prompt))
prompt = "\nWhich algorithm do you wish to draw these lines? "
prompt += 'Please type "basic" for the basic algorithm or "bres"\n'
prompt += "for Bresenham's algorithm: "
specified_alg = input(prompt)

if specified_alg == 'basic':
    timer = 0
    for line in range(num_of_lines):
        x0 = randint(0, 499)
        y0 = randint(0, 499)
        x1 = randint(0, 499)
        y1 = randint(0, 499)
        timer += basic.draw_line(x0, y0, x1, y1)
    print(f"Algorithm took {timer} seconds long.")
    basic.image.show()
elif specified_alg == 'bres':
    timer = 0
    for line in range(num_of_lines):
        x0 = randint(0, 499)
        y0 = randint(0, 499)
        x1 = randint(0, 499)
        y1 = randint(0, 499)
        timer += bresenham.bresenham_alg(x0, y0, x1, y1)
    print(f"Algorithm took {timer} seconds long.")
    bresenham.image.show()
else:
    print("Invalid algorithm. Try again.")