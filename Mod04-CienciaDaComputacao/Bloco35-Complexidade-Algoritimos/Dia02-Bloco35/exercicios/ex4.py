def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)


mdc(60, 40)
