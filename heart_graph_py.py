"""main script for the heart_graph_py.py project. Read README.md for more information"""

# imports
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from time import sleep


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
    """
    Generate and customize a graph.
    Also plot the values passed from calculate_datapoints().
    """
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    line1, = ax.plot(x, y, 'b-')
    grid(True)
    for phase in range(0, 1500, 15):
        speed = 100
        line1.set_ydata(calculate_datapoints(phase/speed)[1])
        fig.canvas.draw()
        sleep(0.05)

if __name__ == '__main__':
    """don't excecute when script is used as a module"""
    data = calculate_datapoints(10)
    plot_graph(data[0], data[1])
