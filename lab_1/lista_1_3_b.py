# 3 write a function which takes an array of numbers as an input and finds the lowest value. Return the index of that element and its value (1p)

from numpy import *
from numpy.random import *

A = []
B = int(input('Enter the number of inputs: '))
C = int(input('Random numbers -  select "1", your own suggestions -  select "2": '))

def find_the_lowest_value(C):
    """Returns the index and lowest value in the array"""
    value = C[0]
    for i in range(len(C) - 1):
        if value > C[i + 1]:
            value = C[i + 1]
            index = i + 1
    print(C)
    print('The index of the lowest value is: ', value)
    print('The lowest value is: ', index)

if C == 1:
    for i in range(B):
        A.append(rand())
    find_the_lowest_value(A)

elif C == 2:
    for i in range(B):
        A.append(float(input('Enter a number: ')))
    find_the_lowest_value(A)

elif C != 1 or 2:
    print('Please enter the correct number')