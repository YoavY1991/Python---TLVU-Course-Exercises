def finds_index_first_d_by_2(B, b):
    # finds the index of the first number ib B list which is divisble by b, if there is not,
    # it will print -1
    for n in B:
        if n % b == 0:
            return B.index(n)
            break
        else:
            continue

    return -1


B = [1, 2, 3, 4, 5]
b = 3
print(finds_index_first_d_by_2(B, b))