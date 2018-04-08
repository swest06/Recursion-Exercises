def power(a, n):
    if n == 0:
        return 0
    elif n == 1:
        return a
    else:
        return a * power(a, n-1)

