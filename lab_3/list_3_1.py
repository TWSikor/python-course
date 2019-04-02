#1 Write a function countField which calculates the field of a given figure. It takes the following input parameters:
# - type: circle/rectangle/triangle/rhombus
# - x & optional y.
# For circle we get only x which stands for radius. For Rectangle x&y are the figure's sides, for triangle they are
# accordingly the base and the height and for rhombus - diagonals (4p)

from numpy import*

def countField(type, X, Y):
    """
    :param type: is a type of geometric figure (e.g. circle, rectangle, triangle, rhombus)
    :param X: :param Y:  for circle we get only 'X' which stands for radius. For Rectangle 'X' and 'Y' are the figure's
    sides, for triangle they are accordingly the base and the height and for rhombus - diagonals
    :return: the area of geometric figure
    """
    if type == 'circle':
        if X >= 0:
            print('The area of the circle is: ', pi * X ** 2)
        else:
            print('Please enter the correct radius of the circle (radius >= 0)')

    elif type == 'rectangle':
        if X >= 0 and Y >= 0:
            print('The area of the rectangle is: ', X * Y)
        else:
            print('Please enter the correct sides of the rectangle (side >= 0)')

    elif type == 'triangle':
        if X >= 0 and Y >= 0:
            print('The area of the triangle is: ', 0.5 * X * Y)
        else:
            print('Please enter the correct sides of the triangle (side >= 0)')

    elif type == 'rhombus':
        if X >= 0 and Y >= 0:
            print('The area of the rhombus is: ', 0.5 * X * Y)
        else:
            print('Please enter the correct diagonals of the rhombus (side >= 0)')
    else:
        print('Please enter the correct type of geometric figure (e.g. circle, rectangle, triangle, rhombus): ')

countField('rhombus', -0.1 ,-0.1)