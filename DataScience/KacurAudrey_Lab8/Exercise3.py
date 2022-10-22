import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# create a 2x4 numpy array filled with zero's
Arr_Zeros = np.full((2, 4), 0, dtype=int)
rows = Arr_Zeros.shape[0]
columns = Arr_Zeros.shape[1]
# using a nested for loop enter integer grade values to the elements of the array
for r in range(rows):
    # assume the first row is fall semester and the second row is spring semester
    for c in range(columns):
        if r == 0:
            Arr_Zeros[r][c] = (int(input(
                f"Please enter the fall {c+1} semester grade in as decimal numbers: ")))
        if r == 1:
            Arr_Zeros[r][c] = (int(input(
                f"Please enter the spring {c+1} semester grade in as decimal numbers: ")))
# for keys use 'Fall" and "spring" and for values use the first and second rows from numpy array, respectively (using slicing to get the proper rows)
grade_dicton = {'Fall': Arr_Zeros[0, :], 'Spring': Arr_Zeros[1, :]}
print(grade_dicton)
# create a series using a dictionary
grade_ser = pd.Series(grade_dicton)
print(grade_ser)
# Ask user which semester they wish to plot
sem = input(
    "option 1. Spring \noption 2. Fall\nWhich semester would you like to plot: ")
# what line width
line = input("What line width would you like to use for your graph: ")
# and color they wish to use (the color should be case insensitive).
colors = (input("What color would you like to use for your graph: ")).lower()
# Add title, xlabel, ylabel to your plot (see Figure in the next page for a sample output)
x = int((grade_ser[sem].size)+1)
y = grade_ser[sem]
plt.plot(range(1, x), y, label=sem, linewidth=line, color=colors)
plt.xlabel('Assignments')
plt.ylabel('Grades')
if sem == "Fall":
    plt.title('Grades for Fall Semester')
else:
    plt.title('Grades for Spring Semester')
plt.show()
