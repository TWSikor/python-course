#3 Find a differential equation which represents a process / model (your choice) and implement it using odeint python function (1p)

from numpy import linspace,arange, zeros
from matplotlib.pyplot import show, figure, plot
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint

def F(x, t):
    """"
    the Rössler attractor
    """
    a = 0.2
    b = 0.2
    c = 6
    dx = zeros(3)
    dx[0] = - x[1] - x[2]
    dx[1] = x[0] + a * x[1]
    dx[2] = b + x[2] * (x[0] - c)
    return dx

T = 200
h = 0.01
t_initial = 0

t = arange(t_initial, T + h, h)
x_initial = [0.2, 0.5, 1]

X = odeint(F, x_initial, t)
x = X[:, 0]
y = X[:, 1]
z = X[:, 2]

fig = figure(1)
ax = Axes3D(fig)
ax.plot(x, y, z)
show()