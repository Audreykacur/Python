def myFunction(*args):  # variable number of arguments/parameters
    result = sum(args)
    return result


print(myFunction(10, 2))
print(myFunction(10, 2, 3, 10, 5))
