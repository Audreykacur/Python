def greaterThanFive(x):
    print("In function")
    return x > 5


numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
result = filter(greaterThanFive, numbers)
print(type(result))
print(result)  # prints address of object filter
result = list(filter(greaterThanFive, numbers))  # function is called here
print(result)
