def myPower(x, y):
    # computes the power of a number given the base and exponent
    sum = 1
    while (y > 0):
        sum = sum * x
        y = y-1
        continue
    print(sum)


# asks the user to enter a base (integer)
x = int(input("Please enter a integer value for the base value: "))

# asks the user to enter an exponent (integer)
y = int(input("Please enter a integer value for the exponent value: "))

myPower(x, y)
