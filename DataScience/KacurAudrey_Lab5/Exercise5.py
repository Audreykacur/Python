from functools import reduce

li = [10, "hi", 20, "Hello", 30, "world", 40]
# using only reduce, filter, and lambda
# find the minimum integer in the list
# reduce()import

# print(reduce((lambda x, y: x < y | y < x), filter(lambda x: type(x) == int, li)))

print(reduce((lambda x, y: x if x < y else y),
      filter(lambda x: type(x) == int, li)))
