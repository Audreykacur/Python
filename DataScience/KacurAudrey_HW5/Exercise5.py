li = [9, "Robot", 3.14, 8, "Vision"]

# use a filter() function along with a lambda to filter out irrelevant data types
# your new list should contain only integers
print(list(filter(lambda x: (type(x) == int or type(x) == float), li)))  # print list
