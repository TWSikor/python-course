#3 Check if X is divisible by Y (do it in one line of code), print 'X is divisible by Y' or 'X is not divisible by Y'. (1p)
#Ad 3 Hint- use the "ternary operator" as we did calculating xIsEvenLog above.

X = int(input('Please enter a number: '))
Y = int(input('Please enter a number: '))

divisibility =  True if X % Y == 0 else False

if divisibility == True:
    print('X is divisible by Y')
else:
    print('X is not divisible by Y')