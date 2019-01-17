"""main script for the heart_graph_py.py project. Read README.md for more information"""

# imports
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from time import sleep
from random import randint


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
    gca().set_position((.1, .3, .8, .6))
    line1, = ax.plot(x, y, 'b-', linewidth=2.5)
    grid(True)
    plt.xlim(-4, 4)
    plt.ylim(-2, 3.5)
    randomizer = randint(0, 10)
    if randomizer < 5:

        figtext(.02, .02,
                """
         \"Liebe muss nicht bitten, auch nicht fordern.
            Liebe muss die Kraft haben, in sich selbst zur Gewissheit zu kommen.
             [1] Dann übertrifft sie sogar die Schönheit der Mathematik ...\"
        	                - Hermann Hesse (Anhang [1] von von Victor Reisenauer)
                """)
    else:
        figtext(.02, .02,
                """
         \"Wer richtig rechnet, der findet sich selbst.
            Die meisten Menschen aber rechnen, um sich zu verlieren.\"
        	                - Hermann Hesse (gewisse Änderungen von von Victor Reisenauer)
                """)

    for phase in range(0, 1500, 15):
        speed = 100
        line1.set_ydata(calculate_datapoints(phase/speed)[1])
        fig.canvas.draw()
        sleep(0.05)
    plt.show(block=True)


if __name__ == '__main__':
    DATA = calculate_datapoints(10)
    plot_graph(DATA[0], DATA[1])
    plt.close()
