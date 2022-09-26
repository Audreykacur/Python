li = [10, "hi", 20, "Hello", 30, "world", 40]
# multiply the integers in the list by 2
# should be one line of code
# check if items in the list are integers type(x)==int

# list comprehension to produce the same output
# use a loop

print([x for x in li if type(x) == int])
