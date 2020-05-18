def drop_duplicates(lst):
    # returns set in order
    return list(set(lst))


print(drop_duplicates([1, 2, 3, 2, 4]))


def drop_duplicates_in_place(lst):
    # this function will replace lst with a set list of its elements in order
    a = list(set(lst))
    while len(lst) > 0:
        lst.pop()
    for n in a:
        lst.append(n)


lst = [1, 2, 3, 2, 4]
drop_duplicates(lst)
print(lst)
drop_duplicates_in_place(lst)
print(lst)

