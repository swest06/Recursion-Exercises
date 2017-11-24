def capitalize(x):
    a = ord(x[0]) - 32
    a = chr(a)
    x = list(x)
    x[0] = a
    x = "".join(x)
    return str(x)

