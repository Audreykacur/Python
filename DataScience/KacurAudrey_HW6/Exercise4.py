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
# of each semester using slicing=
fall = arr_zeros[:-1, :]
print("fall: ", fall)
spring = arr_zeros[1:, :]
print("spring: ", spring)
# min()
minf = np.min(fall)
print("Fall minimum: ", minf)
mins = np.min(spring)
print("Spring minimum: ", mins)
# max()
maxf = np.max(fall)
print("Fall maximum: ", maxf)
maxs = np.max(spring)
print("Spring maximum: ", maxs)
# mean mean()
meanf = np.mean(fall)
print("Fall mean: ", meanf)
means = np.mean(spring)
print("Spring mean: ", means)
# standard deviation std()
stdf = np.std(fall)
print("Fall std: ", stdf)
stds = np.std(spring)
print("Spring std: ", stds)
