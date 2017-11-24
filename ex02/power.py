
>>> def power(a,n):
    x = n - 1
    result = a
    if n == 0:
        result = 1
    while x > 0: 
        result = result*a
        x = x - 1
    return result
