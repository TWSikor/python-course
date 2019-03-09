#1 Perimeter & field of circles with given radius X for the first circle & Y for the second one. (1p)
from numpy import*

X = float(input('Enter the radius of the first circle: '))
Y = float(input('Enter the radius of the second circle: '))

def perimeter(A):
    return 2 * pi * A

def area(A):
    return pi * A ** 2

if X < 0:
    print('Please enter the correct number of the first circle')
else:
    print('The perimeter of the first circle is: ', perimeter(X), 'and the area of the first circle is: ', area(X))

if Y < 0:
    print('Please enter the correct number of the second circle')
else:
    print('The perimeter of the second circle is: ', perimeter(Y), 'and the area of the second circle is: ', area(Y))