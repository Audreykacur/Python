import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

grades = []
num = 1
cond = True
EC = 0

while (cond == True):  # use an infinite loop
    print("\n")
    EC = float(input(
        "Is there extra credit for this assignment? If no enter 0\nEnter how many points are allotted for extra credit: "))
    # enter your homework grades (enter at least 10 grades) float
    x = float(input(f"Enter homework grade {num}: "))
    if (x > (100+EC)):
        print("The grade you entered is greater than the alloted percentage allowed for this assignment")
    elif (x < 0):  # Break the loop when grade < 0
        cond = False
        if (num < 11):
            print("Please enter at least 10 numbers. Reenter a valid grade.")
            cond = True
    else:
        grades.append(x)  # append the grades into the grades list
        num += 1

# since you know the length of the list you can create a new list using list comprehension that begins from 1
numOfGrades = np.array([a for a in range(1, len(grades)+1)])
# panda series out of numpy array
pSerGrades = pd.Series(grades, index=[numOfGrades])
# rename the indices to begin from 1 instead of 0
print(pSerGrades)
# print the descriptive statistics of the grades entered
print(pSerGrades.describe())
#  three plots within a single graph  plot, scatter, bar superimposed one over the other
plt.plot(numOfGrades, pSerGrades)
plt.scatter(numOfGrades, pSerGrades)
plt.bar(numOfGrades, pSerGrades)
plt.title("Homework Grades")
# the x-axis is the indices beginning with 1
plt.xlabel("Homework Assignment Number")
# y-axis is the grades entered
plt.ylabel("Grade received")
plt.show()
