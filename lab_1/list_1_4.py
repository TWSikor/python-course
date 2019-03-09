#4 looking at lab1-input and lab1-plot files create your own python script that takes a number and returns any chart of a given length.
#the length of a chart is the input to your script. The output is a plot (it doesn't matter if it's a y=x or y=e^x+2x or y=|x| function, use your imagination)
#test your solution properly. Look how it behaves given different input values. (1p)

from numpy import *
from matplotlib.pyplot import *

def chart(number_of_points):
    x = linspace(0, number_of_points, 20000)
    y = sin(x/2) * x**cos(x/20)
    plot(x, y)
    scatter(x[0], y[0], c='orange', edgecolors='none', s=50)
    scatter(x[-1], y[-1], c='black', edgecolors='none', s=50)
    show()

A = int(input('Enter the number of points: '))
chart(A)

