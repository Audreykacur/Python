from functools import reduce

myList = [2, 3, -1, 4, 8, 9]

# use the reduce() function and a lambda expression to find the minimum number in the list
print(reduce(lambda x, min: x if x < min else min, myList))
