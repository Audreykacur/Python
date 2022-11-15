import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Given the dataset: (-5,-10), (-1,-3), (3,5), (7,8),(5,7), (9,9)
# make x and y pull out the values from the data set
x = [-5, -1, 3, 7, 5, 9]
y = [-10, -3, 5, 8, 7, 9]
xx = np.ones(len(x))
xx = np.vstack((xx, x))

# find the regression line using Matrix Algebra Least Squares (slides 323-325)
# # Create two numpy arrays out of the two lists
y = np.array((y)).reshape(len(y), 1)  # makes vertical
# you can use the x.transpose() method to transpose a matrix
a = xx.transpose()  # transpose a matrix

# the np.matmul(x, y) method to multiply matrices x and y
xtx = (np.matmul(xx, a))
xty = (np.matmul(xx, y))  # multiply matrices x and y

# multiply matrices x and y # inverse a matrix
# the np.linalg.inv(x) to find the inverse of a matrix
nums = (np.matmul((np.linalg.inv(xtx)), xty))

# find the parameters of the line (slope and y-intercept)
m = (nums[1])  # slope
b = (nums[0])  # y-intercept

# Plot the data points along with the regression line
Yequ = b + m * xx

plt.title('Least Squares Regression Line')
plt.ylabel('y-axis')
plt.xlabel('x-axis')
plt.scatter(x, y)
plt.plot(xx, Yequ, color='r')
plt.show()
# Your algorithm should be able to work with any dataset not just a dataset of 5 data points
