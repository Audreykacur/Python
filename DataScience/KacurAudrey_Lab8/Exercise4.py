import pandas as pd
import numpy as np

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

# using a 2x4 numpy array from ex. 3 -->> Arr_Zeros filled with fall and spring integer grades

# first flatten it to 1D array using deep copy.
flat = Arr_Zeros.flatten()

# create a panda series that consists of the elements of the 1D array.
pandaSer = pd.Series(flat)

# print series and produce descriptive statistics of series by calling the respective built-in method
print(pandaSer)
print(pandaSer.describe())
