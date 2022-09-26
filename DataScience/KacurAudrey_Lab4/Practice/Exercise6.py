print("First lambda: ", end=" ")
def result(x): return x*x  # x*x is the only expression allowed


print(result(8))

print("Second lambda:", end=" ")  # does not go to new line
def result2(x, y): return x+y


print(result2(10, 20))


print("Third lambda: ", end=" ")  # does not go to new line
def result3(x, y, z): return x+y+z


print(result3(10, 20, 50))


# print("First lambda: ")
# result = lambda x: x*x #x*x is the only expression allowed
# print (result(8))

# print("Second lambda: ", end=" ") #does not go to new line
# result2 = lambda x, y: x+y
# print (result2(10,20))


# print("Third lambda: ", end =" ") #does not go to new line
# result3 = lambda x, y, z: x+y+z
# print (result3(10, 20, 50))
