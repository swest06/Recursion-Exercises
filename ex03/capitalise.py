def capitalise(x):
    a = ord(x[0]) - 32
    a = chr(a)
    x = list(x)
    x[0] = a
    x = "".join(x)
    return str(x)


newline = []
line = str(input())
line = line.split(" ")
for i in line:
    newline.append(capitalise(i))
print(" ".join(newline))
