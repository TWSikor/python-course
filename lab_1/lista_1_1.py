#1 calculate & print the value of function y = 2x^2 + 2x + 2 for x=[56, 57, ... 100] (0.5p)

from numpy import*

def function(x):
    y = 2*x**2 + 2*x + 2
    return print('x:', x,' ->  y:', y)

A = 56
B = 100
for x in range (A, B+1):
    function(x)
