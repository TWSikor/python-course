#5 Look at lab2-plot.py and create your own script which takes a number as an input and plots the same 3D wave but with different characteristics
# it's totally up to your imagination how do you want to amend the figure according to the input number (1p)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def wave_3D(A):
    x_knots = np.linspace(-A * np.pi, A * np.pi, 201)
    y_knots = np.linspace(-A * np.pi, A * np.pi, 201)
    X, Y = np.meshgrid(x_knots, y_knots)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.cos(R) ** 2 * np.exp(-0.1 * R)
    ax = Axes3D(plt.figure(figsize = (8, 5)))
    ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap = plt.cm.coolwarm, linewidth = 0.4)
    plt.show()

X = float(input('Please enter a number: '))
wave_3D(X)