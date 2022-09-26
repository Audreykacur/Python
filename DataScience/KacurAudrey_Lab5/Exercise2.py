li = [10, "hi", 20, "Hello", 30, "world", 40]
# using only map, filter, and lambda
# multiply the integers in the list by 2
# should be one line of code
# check if items in the list are integers type(x)==int

print(list(map(lambda x: x*2, filter(lambda x: type(x) == int, li))))
