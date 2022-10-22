#list = [row],[row],[row]
# [column, column] -> in the row box

# create a 2D list 3 rows and 2 columns with various values
TwoDimList = [[0, 2], [7, 5], [99, 5.3]]

print("The current list: ")
for row in TwoDimList:
    for column in row:
        print(column, end=" ")
    print()

# ask the user which element of the array they wish to modify
y = int(input("Which column [0,1] of the array would you like to modify: "))
x = int(input("Which row [0,1,2] of the array would you like to modify: "))
mod = int(
    input(f"What value would you like to put in the place of {TwoDimList[x][y]} : "))

TwoDimList[x][y] = mod

print("The current list: ")
for row in TwoDimList:
    for column in row:
        print(column, end=" ")
    print()
