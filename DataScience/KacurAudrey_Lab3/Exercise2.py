li = [9, 3, 0, -4, 8, 7, 10, -1, 5]
print(li)

# ask the user to give you the following three indices start stop step
x = int(input("Please enter a starting number for the above list: "))
y = int(input("Please enter a stopping number for the above list: "))
z = int(input("Please enter a step number for the above list: "))

print(li[x:y:z])  # print the list
