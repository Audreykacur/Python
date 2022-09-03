# estimate the value of the mathematical constant e by using the formula below

import math
#


def factorial(x):  # computes the factorial
    factSum = x
    #print(f"factorial of {x}!:", end=" ")
    for number in range(0, x-1):
        #print(x, end=" * ")
        x -= 1
        factSum *= x
    # print(f"{x} = {factSum}")  # print results
    return factSum


e = 1
for x in range(1, 11):
    y = factorial(x)
    # print(y)
    b = int(1)/int(y)
    e += b
    print("e: ", e)
