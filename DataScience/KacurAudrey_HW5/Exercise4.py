li = [9, "Robot", 3.14, 8, "Vision"]


def int_dataTypes(x):
    if type(x) == int or type(x) == float:
        return x


# use a filter() function along with a function names int_dataTypes() to filter out irrelevant data types
result = list(filter(int_dataTypes, li))
print(result)  # your new list should contain only integers
