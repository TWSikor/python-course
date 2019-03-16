#2 Find X & Y that satisfy: X is divisible by Y and both X & Y are even. (0.5p)

while True:

    X = int(input('Please enter a number: '))
    Y = int(input('Please enter a number: '))

    divisibility =  True if X % Y == 0 and X % 2 == 0 and Y % 2 == 0 else False

    if divisibility == True:
        print('X is divisible by Y and both X & Y are even')
    else:
        print('Please enter other X and Y')