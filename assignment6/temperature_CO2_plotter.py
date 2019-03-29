#!/usr/bin/python
import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt

def read_CO2(range_min, range_max, y_axis_min, y_axis_max):
    """
        Function that uses pandas to read from file then makes
        a plot out of the read values and saves plot in the
        folder 'static'.

        Args:
            range_min (int):    Variable containing starting year
            range_max (int):    Variable containing ending year
            y_axis_min (int):   Variable containing lowest 'y' value
            y_axis_max (int):   Variable containing highest 'y' value
    """
    CO2_stats = pd.read_csv('CO2.csv', sep=',')
    type(CO2_stats)

    data = CO2_stats[['Year', 'Carbon']]
    data.plot(x = "Year", y = "Carbon")

    plt.xlim(range_min, range_max)
    plt.ylim(y_axis_min, y_axis_max)
    plt.title('CO2.csv"')
    plt.xlabel('Year')
    plt.ylabel('CO2')

    plt.savefig("static/result_CO2.jpg")


def read_temperature(month, range_min, range_max, y_axis_min, y_axis_max):
    """
        Function that uses pandas to read from file then makes
        a plot out of the read values and saves plot in the
        folder 'static'.

        Args:
            month (string):     Variable containing month name
            range_min (int):    Variable containing starting year
            range_max (int):    Variable containing ending year
            y_axis_min (int):   Variable containing lowest 'y' value
            y_axis_max (int):   Variable containing highest 'y' value
    """
    temperature_stats = pd.read_csv('temperature.csv', sep=',')
    type(temperature_stats)

    data = temperature_stats[['Year', month]]
    data.plot(x = "Year", y = month)

    plt.xlim(range_min, range_max)
    plt.ylim(y_axis_min, y_axis_max)
    plt.title('temperature.csv')
    plt.xlabel('Year')
    plt.ylabel('CO2')

    plt.savefig("static/result_temperature.jpg")

def read_co2bycountry(year, up_thresh, low_thresh):
    print("co2_by_country")

    """
        Function that uses pandas to read from file then makes
        a plot out of the read values and saves plot in the
        folder 'static'.

        Args:
            month (string):     Variable containing month name
    """
    CO2bycountry_stats = pd.read_csv('CO2_by_country.csv', sep=',')
    type(CO2bycountry_stats)

    data = CO2bycountry_stats[['Country Name', year]]
    data.plot(x = "Country Name", y = year, kind='bar')

    plt.title('CO2_by_country.csv')
    plt.xlabel('Country')
    plt.ylabel('CO2')

    # # split it up
    # above_threshold = np.maximum(data - up_thresh, 0)
    # below_threshold = np.minimum(data, low_thresh)
    #
    # # and plot it
    # fig, ax = plt.subplots()
    # ax.bar(x, below_threshold, 0.35, color="g")
    # ax.bar(x, above_threshold, 0.35, color="r",
    #         bottom=below_threshold)
    #
    # # horizontal line indicating the threshold
    # ax.plot([0., 4.5], [threshold, threshold], "k--")

    plt.savefig("static/result_CO2bycountry.jpg")

def the_menu(which_plot, month, range_min, range_max, y_axis_min, y_axis_max):
    """
        Function acting as a menu which takes the necessary variables
        and decides according to those whether to run the read_CO2() or
        read_temperature() function with their respective parameters.

        Args:
            which_plot (int):   1 = read_CO2(), 2 = read_temperature()
            month (string):     Variable containing month name (if relevant)
            range_min (int):    Variable containing starting year
            range_max (int):    Variable containing ending year
            y_axis_min (int):   Variable containing lowest 'y' value
            y_axis_max (int):   Variable containing highest 'y' value
    """
    if(which_plot == 1):
        read_CO2(int(range_min), int(range_max), int(y_axis_min), int(y_axis_max))

    if(which_plot == 2):
        read_temperature(month, int(range_min), int(range_max), int(y_axis_min), int(y_axis_max))

the_menu(1, "month", 1910, 1950, 500, 1700) #there needs to be a 2nd parameter although we won't use be using it
the_menu(2, "May", 1880, 1990, 5, 20) #for 6.1 the user can change the parameter containing the month here
read_co2bycountry('2005', 30, 40) #6.4 param1=year, param2=low_thresh, param3=up_thresh
