#!/usr/bin/env python3

import numpy as np
from numba import jit
import matplotlib.pyplot as plt
import time
import sys

#added to accommodate for exercise 4.5
xmin = int(float(sys.argv[1]))
xmax = int(float(sys.argv[2]))
ymin = int(float(sys.argv[3]))
ymax = int(float(sys.argv[4]))
height = int(float(sys.argv[5])) #resolution
width = int(float(sys.argv[5])) #resolution
output_name = sys.argv[6]

def mandelbrot(z, maxiter):
    """
    Function that takes a complex number and the maximum amount
    of iterations possible as parameters. By applying a formula
    to the given complex number, this function checks how many "n"
    times it is able to reapply the formula to itself until either
    having an absolute value above 2 or reaching beyond the "maxiter"
    amount of iterations.

    Args:
        z: complex number
        maxiter: maximum amount of iterations we allow

    Return:
        n: amount of times iteration occured
        maxiter: maximum amount of iterations we allow
    """
    c = z
    for n in range(maxiter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return maxiter

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, maxiter):
    """
    Function that chooses some rectangle in the complex plane
    according to the given parameters and plots the coloring
    of mandelbrot as an image while also timing the process.

    Args:
        xmin: lowest x-axis value
        xmax: highest x-axis value
        ymin: lowest y-axis value
        ymax: highest y-axis value
        width: length of x-axis
        height: length of y-axis
        maxiter: maximum amount of iterations we allow
    Return:
        cols: colums
        rows: rows
        arr_img: array containing the mandelbrot
    """
    start = time.time() #starts timer
    cols = np.linspace(xmin, xmax, width)
    rows = np.linspace(ymin, ymax, height)

    arr_img = np.empty((width, height))
    for i in range(width):
        print("%.2f%%" % (i/width * 100.0)) #Prints our progression
        for j in range(height):
            arr_img[i,j] = mandelbrot(cols[i] + 1j*rows[j], maxiter)

    plt.figure(dpi=200)
    plt.imshow(arr_img.T, cmap='hot', interpolation='bilinear', extent=[xmin, xmax, ymin, ymax])

    end = time.time() #ends timer
    print("Time elapsed: ", ("%.2f" % (end - start)))

    return (cols,rows,arr_img)

#You can edit your values here
mandelbrot_set(xmin, xmax, ymin, ymax, width, height, 1000)

#name of savefig accommodated for exercise 4.5
plt.savefig(output_name)
plt.show()
