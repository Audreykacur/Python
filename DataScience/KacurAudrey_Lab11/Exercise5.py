import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats
import csv
hours = []
grade = []
with open('/Users/audreykacur/ClassWork/Fall 2022/Python/DataScience/KacurAudrey_Lab11/grades.csv', 'r', newline='') as grades:
    reader = csv.reader(grades)
    for record in reader:
        x, y = record
        hours.append(float(x))
        grade.append(float(y))
# Given the Grades.csv file, where the first column is hours studied and the second column is grades

# read it's data and place them into two numpy arrays
x = np.array(hours)
y = np.array(grade)


# find the regression line using the built-in linregress() method (slides 331-334)
# plot the data points along with the regression line
# print: slope, y-intercept, r(correlation coefficient), p-value, standard error
slope, intercept, r, p, std_err = stats.linregress(x, y)
print("Slope: ", slope, 'Y-intercept: ', intercept, "correlation (r): ",
      r, 'p-vale: ', p, 'Standard Error: ', std_err)

# find the parameters of the line (slope and y-intercept)
mymodel = (slope*x) + intercept

# predict a students grade given 10.5 hours of study
print(slope*(10.5)+intercept)

# plot the data points along with the regression line
plt.title('Grades')
plt.ylabel('y-axis')
plt.xlabel('x-axis')
plt.scatter(x, y)
plt.plot(x, mymodel, color='r')
plt.show()
