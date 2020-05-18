def adjacent_number_mult_sum(C):
    # returns the sum of the multiplication of adjacent numbers in list C
    sumis = 0

    for i, n in enumerate(C):
        if len(C) == 0:
            return 0
        elif len(C) == 1:
            return C[0]
        elif i < (len(C) - 1):
            sumis += n * C.index(i + 1)
        else:
            break

    return sumis


C = [0, 1, 2, 3, 4]

print(adjacent_number_mult_sum(C))