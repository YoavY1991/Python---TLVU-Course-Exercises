def is_in_range(lst, a, b):
    # a>b
    # checks if all abs number in lst are in range a,b (a<n<b)
    if len(lst) == [0]:
        return True
    for x in lst:
        if x < a or x > b:
            return False
        else:
            pass

    return True


print(is_in_range([-1, 4.7, 7], -2.4, 0))
print(is_in_range([1, 2, 3], 0, 5))

