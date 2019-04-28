from numpy import*
from matplotlib.pyplot import plot, show, legend, figure, cm, contour, clabel
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import fmin
from numpy.random import rand, randint

def function(w):
    x = w[0]
    y = w[1]
    return sin(x) * x ** 2  + 1 * (y - 0.5 * x)  ** 2 + (0.5 * x * y) - 1.5 * x + cos(y)


T = 300
X = linspace(- 3, 3, T)
Y = linspace(- 3, 3, T)
X, Y = meshgrid(X, Y)
w = [X, Y]
Z = function(w)


ax = Axes3D(figure(figsize = (10, 7)))
ax.plot_surface(X, Y, Z, cmap = cm.rainbow, linewidth = 0.4)
ax.text2D(0.05, 0.95, '3d function function with multiple local optima', transform = ax.transAxes)
show()


figure(figsize = (10, 7))
CS = contour(X, Y, Z)
clabel(CS, inline = 1, fontsize = 10)
show()


initial_random_point = randint(-3, 3) * rand(2)
print('initial_random_point =', initial_random_point, '\n')
x_min = fmin(function, initial_random_point)

figure(figsize = (10, 7))
CS = contour(X, Y, Z)
clabel(CS, inline = 1, fontsize = 10)
plot(initial_random_point[0], initial_random_point[1],'ko', label ='initial point')
plot(x_min[0], x_min[1], 'ro', label = 'local minimum point')
legend()
show()


list_of_minima_arg = []
list_of_minima_val = []

N = 10000

for i in range(N):
    random_value = rand()

    if random_value <= 0.25:
        initial_random_point = [- 3 * rand(), - 3 * rand()]
        list_of_minima_arg.append(initial_random_point)

    elif random_value <= 0.50:
        initial_random_point = [ 3 * rand(), - 3 * rand()]
        list_of_minima_arg.append(initial_random_point)

    elif random_value <= 0.75:
        initial_random_point = [- 3 * rand(), 3 * rand()]
        list_of_minima_arg.append(initial_random_point)

    elif random_value <= 1.00:
        initial_random_point = [ 3 * rand(), 3 * rand()]
        list_of_minima_arg.append(initial_random_point)

for i in range(N):
    list_of_minima_val.append(function(list_of_minima_arg[i]))

j = list_of_minima_val.index(min(list_of_minima_val))
min_glob = list_of_minima_arg[j]

figure(figsize = (10, 7))
CS = contour(X, Y, Z)
clabel(CS, inline = 1, fontsize = 10)
plot(min_glob[0], min_glob[1],'ro', label =' global minimum point')
legend()
show()