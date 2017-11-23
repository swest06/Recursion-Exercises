Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def power(a,n):
    x = n - 1
    result = a
    if n == 0:
        result = 1
    while x > 0: 
        result = result*a
        x = x - 1
    return result
