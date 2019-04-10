#2 Write a function which takes sets of parameters of two figures and compares their fields. (4p)
# The exemplary input is [[Circle, 4], [Rhombus, 2, 4]]
# Expected output would be 'The first figure (Circle) has larger field'

from numpy import pi

def count_Field(X):
    """
    Function calculate the area of geometric figure.
    :param X[0]: is a type of geometric figure (e.g. circle, rectangle, triangle, rhombus)
    :param X[1]: :param X[2]:  for circle we get only 'X[1]' which stands for radius. For Rectangle 'X[1]' and 'X[2]' are the figure's
    sides, for triangle they are accordingly the base and the height and for rhombus - diagonals
    :return: the area of geometric figure
    """
    list_of_figure = ['circle', 'rectangle', 'triangle', 'rhombus']
    try:
        if X[0] in list_of_figure:
            if X[0] == 'circle':

                if len(X) > 2:
                    print('Too many arguments')

                else:
                    if X[1] >= 0:
                        return (pi * X[1] ** 2)
                    else:
                        print('Please enter the correct radius of the circle (radius >= 0)')

            elif len(X) > 3:
                print('Too many arguments')
                exit()

            else:
                if X[0] == 'rectangle':
                    if X[1] >= 0 and X[2] >= 0:
                        return (X[1] * X[2])
                    else:
                        print('Please enter the correct sides of the rectangle (side >= 0)')

                elif X[0] == 'triangle':
                    if X[1] >= 0 and X[2] >= 0:
                        return (0.5 * X[1] * X[2])
                    else:
                        print('Please enter the correct sides of the triangle (side >= 0)')

                elif X[0] == 'rhombus':
                    if X[1] >= 0 and X[2] >= 0:
                        return (0.5 * X[1] * X[2])
                    else:
                        print('Please enter the correct diagonals of the rhombus (side >= 0)')

        else:
            print('Please enter the correct type "X[0]" of geometric figure (e.g. circle, rectangle, triangle, rhombus): ')

    except TypeError:
        print('Wrong order of arguments')

def bigger_Field(X):
    """
    Function compare the area of geometric figures.
    :param X: list of inputs
    :return: which of two geometric figures has larger area
    """
    Y = X[0]
    Z = X[1]
    try:
        if len(X) != 2:
            print('The function supports only two arguments')
        else:
            if ((1 < len(Y) < 4) and (1 < len(Z) < 4)):
                A = count_Field(Y)
                B = count_Field(Z)

                if A > B:
                    print('The first figure (', Y[0], ') has larger field')

                elif B > A:
                    print('The second figure (', Z[0], ') has larger field')

                elif A == B:
                    print('Both of the figure (', Y[0], Z[0], ') have the same field')
            else:
                print('Bad values were given')

    except (IndexError or TypeError):
        print('Bad values were given')

bigger_Field([['CiRcLe'.lower(), 12], ['rHombus'.lower(), 400, 20]])