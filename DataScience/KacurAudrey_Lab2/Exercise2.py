import math
# estimate the value of the mathematical constant e


def factorial(x):  # computes the factorial
    factSum = x
    for number in range(0, x-1):
        x -= 1
        factSum *= x
    return factSum


e = 1
for x in range(1, 11):
    e += int(1)/int(factorial(x))
    print("e: ", e)
