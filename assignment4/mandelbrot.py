#!/usr/bin/env python3


def interface_options():
    print()
    print("1. Mandelbrot basic (without numpy or numba)")
    print("2. Mandelbrot with numpy")
    print("3. Mandelbrot with numba")
    print("4. Exit")


while (True):
    interface_options()
    print("Enter your option [1-4] or --help :")
    option_io = input()

    if option_io=="1":
        print("MANDELBROT_1 BASIC")
        exec(open("mandelbrot_1.py").read())

    elif option_io=="2":
        print("MANDELBROT_2 NUMPY")
        exec(open("mandelbrot_2.py").read())

    elif option_io=="3":
        print("MANDELBROT_3 NUMBA")
        exec(open("mandelbrot_3.py").read())

    elif option_io=="4":
        print("PROGRAM ENDING.")
        exit()

    elif option_io=="--help":
        print()
        print("--HELP")
        print("This program should be run as follows:")
        print(">>python mandelbrot.py xmin xmax ymin ymax resolution output_name")
        print("example:")
        print(">>python mandelbrot.py -2.0 1.0 -1.0 1.0 1000 result.jpg")
        print("Exit the program if you would like to re-adjust your arguments.")
        print("Arguments must be adjusted before choosing option 1-3.")
    else:
        # other input given
        print("OPTION DOESN'T EXIST, TRY AGAIN.")
