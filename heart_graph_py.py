"""main script for the heart_graph_py.py project. Read README.md for more information"""

# imports
from pylab import *
import numpy as np

def cube(x):
    """
    helper function to calculate the cube of a
    negative number (complex numbers)
    """
    if 0 <= x: 
        return x**(1./3.)
    return -(-x)**(1./3.)

def calculate_datapoints(param_a):
    """
    calculate an array of datapoints with this special function:
    y = x**(2/3) + 0.9*(3.3 - x**2)**(1/2) * sin(a*pi*x)
    """
    x = np.arange(-2.0, 2.0, 0.01)
    x = np.around(x, decimals=3)
    y = [cube(t**2)+0.9*np.sqrt((3.3 - t**2))*sin(param_a*pi*t) for t in x]
    data = [x, y]
    return data

def plot_graph(x, y):
    plot(x, y)
    grid(True)
    show()

if __name__ == '__main__':
	"""don't excecute when script is used as a module"""
	data = calculate_datapoints(10)
	plot_graph(data[0], data[1])
