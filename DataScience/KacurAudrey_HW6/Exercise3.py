import numpy as np
# create a 2x4 numpy array filled with zeros
arr_zeros = np.zeros((2, 4), dtype=int)
rows = arr_zeros.shape[0]
columns = arr_zeros.shape[1]

# using a nested for loop enter int grade values to all elements of the array
for r in range(rows):
    for c in range(columns):
        # assume the first row is fall semester and the second row is spring semester
        if r == 0:
            arr_zeros[r][c] = int(
                input(f"Enter the fall semester grade for column {c}: "))
        else:
            arr_zeros[r][c] = int(
                input(f"Enter the spring semester grade for column {c}: "))

# change the shape of the array to 4 x 2
for r in range(rows):
    for c in range(columns):
        # assume the first row is fall semester and the second row is spring semester
        print(arr_zeros[r][c], end="")
    print("\n")

# using slicing create an array that consists of the elements of the first column of the reshaped array and a second array that consists of the elements of the second column of the reshaped array
reshapenArr = arr_zeros.reshape(4, 2)
print("Reshapen: ", reshapenArr)

firstColumn = reshapenArr[:, :-1]
print(firstColumn)
secondColumn = reshapenArr[:, 1:]
print(secondColumn)
