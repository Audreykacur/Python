from functools import reduce
# to sum the integers in a list
# reduce, lambda, filter

li = [10, "hi", 20, "Hello", 30, "world", 40]
# should be one line of code

print(reduce((lambda x, y: x+y), filter(lambda x: type(x) == int, li)))
