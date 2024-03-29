def has_divider(n, i, j):
    if i > j:
        return False
    elif n % i == 0:
        return True
    else:
        return has_divider(n, i + 1, j)


def prime(n):
    return n > 1 and not (has_divider(n, 2, n - 1))
