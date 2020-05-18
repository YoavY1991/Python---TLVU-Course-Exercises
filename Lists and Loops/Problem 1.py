def squarelist(integer):
    return list(x**2 for x in range(1,integer+1))


print(squarelist(6))