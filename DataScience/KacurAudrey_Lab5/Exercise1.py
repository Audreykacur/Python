tup1 = (1, 2, 3)  # create two tuples with 3 numbers in each
tup2 = (1, 2, 3)

# use a map and lambda
# add the respective elements to the tuples
# print the result
print(list(map(lambda tup1, tup2: tup1+tup2, tup1, tup2)))


# def addTup(tup1, tup2):
#     print(tup1, tup2)
#     for x in range(0, len(tup1)):
#         tup3[x] = tup1[x]+tup2[x]
#     return tuple(tup3)
# print(addTup(tup1, tup2))
