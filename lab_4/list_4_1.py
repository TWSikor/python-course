#1 Looking at the Euler method above create your own function which takes:
# a (from x' = ax)
# h - step
# T time range
# as an input and plots the solution of a differential equation x' = ax (1p)

import numpy as np
import matplotlib.pyplot as plt

def function_with_the_Euler_method(a, h, t):
    """
    :param a:
    :param h: step
    :param t: time range
    :return: list of function values
    """
    initial_x = 0.5
    x = np.zeros(t.shape)
    x[0] = initial_x

    for i in range(t.size - 1):
        x[i + 1] = x[i] + h * (a * x[i])

    return x

# parameters
a = 0.32
T = 7
h = 0.1

t = np.arange(0, T, h)
x = function_with_the_Euler_method(a, h, t)

plt.plot(t, x)
plt.xlabel('t', fontsize = 15)
plt.ylabel('x', fontsize = 15)
plt.show()