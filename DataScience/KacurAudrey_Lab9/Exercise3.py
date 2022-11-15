import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Using the same DataFrame from Ex. 1
grades_dict = {'Wally': [87, 96, 70], 'Eva': [100, 87, 90], 'Sam': [
    94, 77, 90], 'Katie': [100, 81, 82], 'Bob': [83, 65, 85]}

StudentName = grades_dict.keys()
# length
x = 1
lengths = []
for item in StudentName:
    lengths.append(x)
    x += 1

dFrame = pd.DataFrame(grades_dict)
#  plot 5 box plots one for each student within a single graph
plt.boxplot((dFrame.T))

# your algorithm should produce box plots for any number of columns not just 5

# note: rename the x-axis data to students' names using:
plt.xticks(lengths, StudentName)
plt.show()
# The values in these two arguments should be retrieved automatically and should work for any number of students not just 5
