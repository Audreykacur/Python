str1 = "Catherine"
li = [2, 3, 5]

tuple1 = (str1, li)
print(tuple1)

# modifies last element of list:
tuple1[1][-1] = "END"
print(tuple1)

liStr, liNumAndStrs = tuple1  # unpack sequence

print(liStr)  # catherine
print(type(liStr))  # str

print(liNumAndStrs)  # [2, 3, 'END']
print(type(liNumAndStrs))  # list
