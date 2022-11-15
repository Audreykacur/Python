import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = [1, 2, 3, 4, 5]
y = [1, 2, 4, 4, 6]
xx = np.ones(len(x))  # xx = [1, 1, 1, 1, 1], [1, 2, 3, 4, 5]
xx = np.vstack((xx, x))

# # Create two numpy arrays out of the two lists
y = np.array((y)).reshape(len(y), 1)  # makes vertical
a = xx.transpose()  # transpose a matrix

xtx = (np.matmul(xx, a))
xty = (np.matmul(xx, y))  # multiply matrices x and y

# multiply matrices x and y # inverse a matrix
nums = (np.matmul((np.linalg.inv(xtx)), xty))

# # Create a scatter plot of the data as well as the best-fit line using the equation y = mx+b
# # Equation from slide 323 should yield the y-intercept, b, and the slope, m, of the line.
# # Plot the best-fit line using the equation of the line: y = mx + b

Yequ = (nums[0]) + (nums[1]) * xx

# See the last 5 lines of code from slide 328 on how to plot the line given the equation of the line
plt.title('Least Squares Regression Line')
plt.ylabel('y-axis')
plt.xlabel('x-axis')
plt.scatter(x, y)
plt.plot(xx, Yequ, color='r')
plt.show()
# Your algorithm should be able to work for any number of data points not just for 5
