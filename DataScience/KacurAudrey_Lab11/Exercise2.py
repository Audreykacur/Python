# based on your dataset from Ex. 1 find the regression line using Ordinary Least Squares (slides 326-328)
# you can use the mean() built in function
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Given the dataset: (-5,-10), (-1,-3), (3,5), (7,8),(5,7), (9,9)
# make x and y pull out the values from the data set
xli = [-5, -1, 3, 7, 5, 9]
x = np.array(xli)
yli = [-10, -3, 5, 8, 7, 9]
y = np.array(yli)

# find the regression line using Matrix Algebra Least Squares (slides 323-325)
#y = wo + w1*x
#wo = intercept
#w1 = slope
# y = predicted output

# find the parameters of the line (slope and y-intercept)
w1 = ((np.mean(x*y))-(np.mean(x)*np.mean(y))) / \
    ((np.mean(x**2))-(np.mean(x)**2))  # slope
w0 = np.mean(y) - (w1 * np.mean(x))  # y-intercept
print(w0, w1)

# Plot the data points along with the regression line
Ymodel = w0 + (w1*x)
print(Ymodel)

plt.title('Least Squares Regression Line')
plt.ylabel('y-axis')
plt.xlabel('x-axis')
plt.scatter(x, y)
plt.plot(x, Ymodel, color='r')
plt.show()
# Your algorithm should be able to work with any dataset not just a dataset of 5 data points
