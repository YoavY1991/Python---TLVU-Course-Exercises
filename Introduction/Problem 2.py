def expression(x):
    # This function returns the following expression (1/(x-2)**0.5)
    if x == 2:
        return 'Divison by Zero!'
    elif x < 2:
        return 'Imaginary number!'
    else:
        return 1 / (x - 2) ** 0.5


print(expression(8.25))