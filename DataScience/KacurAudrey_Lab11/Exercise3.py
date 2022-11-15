import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
import numpy as np

# based on your dataset from Ex. 1 find the regression line using the built-in linregress() method (slides 331-334)

# Given the dataset: (-5,-10), (-1,-3), (3,5), (7,8),(5,7), (9,9)
# make x and y pull out the values from the data set
xli = [-5, -1, 3, 7, 5, 9]
x = np.array(xli)
yli = [-10, -3, 5, 8, 7, 9]
y = np.array(yli)

slope, intercept, r, p, std_err = stats.linregress(x, y)
# print: slope, y-intercept, r(correlation coefficient), p-value, standard error
print("Slope: ", slope, 'Y-intercept: ', intercept, "correlation (r): ",
      r, 'p-vale: ', p, 'Standard Error: ', std_err)

# find the parameters of the line (slope and y-intercept)
mymodel = (slope*x) + intercept

# plot the data points along with the regression line
plt.title('Regression line')
plt.ylabel('y-axis')
plt.xlabel('x-axis')
plt.scatter(x, y)
plt.plot(x, mymodel, color='r')
plt.show()
# Your algorithm should be able to work with any dataset not just a dataset of 5 data points
