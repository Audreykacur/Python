def myF():
    x = 3
    y = 5
    z = 8
    return (x, y, z)  # it returns a tuple (parenthesis can be omitted)


tuple1 = myF()  # similar to the line below
print(tuple1[0])
print(id(tuple1[0]))
x, y, z = myF()  # similar to the line above: unpacking a tuple
print(x, y, z)
print(id(x))

x = -3  # x is not the same variable as x above
print(x, y, z)
print(id(x))
