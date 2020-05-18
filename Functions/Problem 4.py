# Alternative 1

def gcd(lst):
    lst.sort()
    s = lst[-1]
    l = 0
    while l < len(lst):
        for x in lst:
            if x % s != 0:
                s -= 1
                l = 0
                break
            else:
                l += 1
    return s


# Alternative 2

def gcd_pair(a, b):
    # finds the max common dividor

    for i in range(min(a, b), 0, -1):
        if a % i == b % i == 0:
            return i


def gcd2(lst):
    d = 0
    for i, x in enumerate(lst):
        if i < len(lst) - 1:
            d = gcd_pair(x, lst[i + 1])
    return d


print(gcd([270, 192]))
print(gcd([3, 6, 27]))
print(gcd([238, 1054, 187]))
print(gcd2([270, 192]))
print(gcd2([3, 6, 27]))
print(gcd2([238, 1054, 187]))