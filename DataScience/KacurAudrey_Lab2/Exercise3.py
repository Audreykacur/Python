def myMinimum(x=8, y=2, z=10):  # finds the minimum of 3 numbers
    if (x < y) & (x < z):
        return x
    if (y < x) & (y < z):
        return y
    if (z < y) & (z < x):
        return z  # return the minimum value to main program
    else:
        print("Something went wrong")


print(myMinimum())  # print returned value
print(myMinimum(100))
print(myMinimum(100, 12))
print(myMinimum(100, 12, 1))
