# threshold is given as input by the user
threshold = int(input("Enter the threshold number: "))

a = [[77, 68, 86, 73],
     [96, 87, 89, 81],
     [70, 90, 86, 81]]  # 2D list
b = [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]


for row in range(len(a)):
    for col in range((len(a[row]))):
        # print("a[row][col]: ", a[row][col], "row: ", row, "col: ", col)
        if (a[row][col] > threshold):  # convert values above threshold to 255
            b[row][col] = 255
        else:  # convert value to 0 if they are below or same
            b[row][col] = 0

print(b)
