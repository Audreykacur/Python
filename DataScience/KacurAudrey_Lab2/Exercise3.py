def myMinimum(x=8, y=2, z=10):  # finds the minimum of 3 numbers
    # use len(args) to get the number of variable arguments passed
    if (x < y) & (x < z):
        return x
    if (y < x) & (y < z):
        return y
    if (z < y) & (z < x):
        return z
    else:
        print("Something went wrong")
    # return the minimum value to main program


# print returned value
print(myMinimum())
print(myMinimum(100))
print(myMinimum(100, 12))
print(myMinimum(100, 12, 1))
