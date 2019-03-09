#2 Find X & Y that satisfy: X is divisible by Y and both X & Y are even. (0.5p)

for i in range(0,100,2):
    x[i] = 0
    for j in range(0,100,2):
        y[j] = 0
        remainder = x % y
        while remainder != 0:
            if remainder == 0:
            return x, y