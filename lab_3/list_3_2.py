#2 Write a function which takes sets of parameters of two figures and compares their fields. (4p)
# The exemplary input is [[Circle, 4], [Rhombus, 2, 4]]
# Expected output would be 'The first figure (Circle) has larger field'

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
            return pi * X ** 2
        else:
            print('Please enter the correct radius of the circle (radius >= 0)')

    elif type == 'rectangle':
        if X >= 0 and Y >= 0:
            return X * Y
        else:
            print('Please enter the correct sides of the rectangle (side >= 0)')

    elif type == 'triangle':
        if X >= 0 and Y >= 0:
            return 0.5 * X * Y
        else:
            print('Please enter the correct sides of the triangle (side >= 0)')

    elif type == 'rhombus':
        if X >= 0 and Y >= 0:
            return 0.5 * X * Y
        else:
            print('Please enter the correct diagonals of the rhombus (side >= 0)')
    else:
        print('Please enter the correct type of geometric figure (e.g. circle, rectangle, triangle, rhombus): ')


def bigger_Field(t, A, B, y, C, D):

    countField(t, A, B)
    countField(y, C, D)

    if countField(t, A, B) > countField(y, C, D):
        print('The first figure (',t,') has larger field')

    elif countField(t, A, B) < countField(y, C, D):
        print('The second figure (',y,') has larger field')

    elif countField(t, A, B) < countField(y, C, D):
        print('The fields of both figures are the same')

bigger_Field('circle', 10, 4, 'rhombus', 12, 15)