def series_sum(n,d):
    list1 = [1]
    while len(list1)<n:
        list1.append(list1[-1]+d)
    return sum(list1)


print(series_sum(5,2))