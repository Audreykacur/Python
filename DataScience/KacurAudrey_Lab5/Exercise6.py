from functools import reduce


li = [10, "hi", 20, "Hello", 30, "world", 40]
# using only map, filter, and lambda
# print the string of elements of the list in uppercase


print(list(map((lambda x: x.upper()),
      filter(lambda x: type(x) == str, li))))
