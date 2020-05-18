def check_if_prime(n):
    if n % 2 == 0:
        return False
    for x in range(3, (int(n ** 0.5) + 1), 2):
        if n % x == 0:
            return False
        else:
            continue

    return True


print(check_if_prime(203))