# 5
# ----------------------------------------------------------------------------------------------------------------------
# Create your own 3d function with multiple local optima.
# 5_1

import numpy as np
from matplotlib.pyplot import plot, show, legend, figure, cm, contour, clabel
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import fmin
from numpy.random import randn, randint

def ackley_function(x_1, x_2):
    """
    :return:
    """
    a = 20
    b = 0.2
    c = 2 * np.pi
    d = 0.5

    sum_1 = x_1 ** 2 + x_2 ** 2
    sum_2 = np.cos(c * x_1) + np.cos(c * x_2)

    part_1 = - a * np.exp(- b * (d * sum_1 ** (0.5)))
    part_2 = - np.exp(d * sum_2)

    return part_1 + part_2 + a + np.exp(1)

# parameters
T = 1000
X = np.linspace(- 20, 20, T)
Y = np.linspace(- 20, 20, T)

X, Y = np.meshgrid(X, Y)
Z = ackley_function(X, Y)

fig = figure()
ax = Axes3D(figure(figsize = (8, 5)))
ax.plot_surface(X, Y, Z, cmap = cm.coolwarm, linewidth = 0.4)
ax.text2D(0.05, 0.95, '3d Ackley function with multiple local optima', transform = ax.transAxes)
show()

# ----------------------------------------------------------------------------------------------------------------------
# Create an algorithm which takes an initial point and looks for the closest local optimum (1p)
# 5_2
"""
def gradient_descent_for_ackley_function():

    initial_point = randint(- 15, 15) * randn(2)
    rate = 0.01
    precision = 0.000001
    previous_step_size = 1
    max_iters = 10000
    iteration_counter = 0
    dx_1 = lambda x_1, :
    dx_2 = lambda x_2,:
    while previous_step_size > precision and iteration_counter < max_iters:
        x_1 = initial_point[0]
        x_2 = initial_point[1]
        new_x_1 = new_x_1 - rate * dx_1(x_1)
        new_x_2 = new_x_2 - rate * dx_2(x_2)
        previous_step_size_1 = abs(new_x_1 - x_1)
        previous_step_size_2 = abs(new_x_2 - x_2)
        iteration_counter = iteration_counter + 1
        print('iteration: ', iteration_counter, '\n Z value is: ', )
    print('The local minimum is', new_x_1, new_x_2 )
"""
initial_point = randint(- 15, 15) * randn(2)
T = 1000
X = np.linspace(- 20, 20, T)
Y = np.linspace(- 20, 20, T)

X, Y = np.meshgrid(X, Y)
Z = ackley_function(X, Y)

figure()
CS = contour(X, Y, Z)
clabel(CS, inline = 1, fontsize = 15)
plot(initial_point[0],initial_point[1],'ko', label = 'initial point')
#plot(x_min[0],x_min[1],'ko', label='final')
legend()
show()

# ----------------------------------------------------------------------------------------------------------------------
# Create an algorithm which aims to find a global optimum, the time of execution is limiter to ~30sec (1p)
# 5_3

# ----------------------------------------------------------------------------------------------------------------------
# If your solution is heuristic test its quality. Measure the probability of finding the GLOBAL optimum (1p).
# 5_4

# ----------------------------------------------------------------------------------------------------------------------
# You can, for example, execute your search function multiple times and check if the returned result is what you expected.
# Measure the success / total trials rate (2p)
# 5_5
