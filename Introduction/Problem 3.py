def givenx(x):
    x=abs(x)
    if x % 6 == 0:
        print('Divisible by 6!')
    if x % 3 == 0 and x % 2 != 0:
        print('Divisible by 3!')
    if len(str(x)) % 2 == 0:
        print('Even number of digits')


givenx(-15)
