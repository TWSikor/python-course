#1 Write a function countField which calculates the field of a given figure. It takes the following input parameters:
# - X[0]: circle/rectangle/triangle/rhombus
# - x & optional X[2].
# For circle we get onlX[2] x which stands for radius. For Rectangle x&X[2] are the figure's sides, for triangle theX[2] are
# accordinglX[2] the base and the height and for rhombus - diagonals (4p)

from numpy import pi

def countField(X):
    """
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
                        print('The area of the circle is: ', pi * X[1] ** 2)
                    else:
                        print('Please enter the correct radius of the circle (radius >= 0)')

            elif len(X) > 3:
                print('Too many arguments')

            else:
                if X[0] == 'rectangle':
                    if X[1] >= 0 and X[2] >= 0:
                        print('The area of the rectangle is: ', X[1] * X[2])
                    else:
                        print('Please enter the correct sides of the rectangle (side >= 0)')

                elif X[0] == 'triangle':
                    if X[1] >= 0 and X[2] >= 0:
                        print('The area of the triangle is: ', 0.5 * X[1] * X[2])
                    else:
                        print('Please enter the correct sides of the triangle (side >= 0)')

                elif X[0] == 'rhombus':
                    if X[1] >= 0 and X[2] >= 0:
                        print('The area of the rhombus is: ', 0.5 * X[1] * X[2])
                    else:
                        print('Please enter the correct diagonals of the rhombus (side >= 0)')

        else:
            print('Please enter the correct type "X[0]" of geometric figure (e.g. circle, rectangle, triangle, rhombus): ')

    except TypeError:
        print('Wrong order of arguments')

countField(['Triangle'.lower(), 30, 4, 8])