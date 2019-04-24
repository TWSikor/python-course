#2 Beside the solution print the 'ideal' approximation on your chart using for example green color as a reference. (1p)
#2 Hint: use small step value. Use plt.legend to explain which serie is the 'ideal'

import numpy as np
import matplotlib.pyplot as plt
from list_4_1 import function_with_the_Euler_method

# parameters
a = 0.32
T = 7
h_1 = 0.3
h_2 = 0.0001

t_1 = np.arange(0, T, h_1)
x_1 = function_with_the_Euler_method(a, h_1, t_1)

t_2 = np.arange(0, T, h_2)
x_2 = function_with_the_Euler_method(a, h_2, t_2)

plt.plot(t_1, x_1, '--k', label = 'base')
plt.plot(t_2, x_2, '-g', label = 'ideal')
plt.legend(loc = 'upper left', fontsize=14)
plt.xlabel('t', fontsize = 15)
plt.ylabel('x', fontsize = 15)
plt.show()