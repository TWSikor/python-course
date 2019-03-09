#2 ask the user for a number and print its factorial (1p)

number = int(input('Please enter a number which is >= 0 (e.g. 0, 1, 2, 3, ....): '))

def factorial(number):
    if number < 0:
        print('Please enter the correct number (>=0)')
    elif number == 0:
        return 1
    else:
        return number * factorial(number - 1)

print(factorial(number))