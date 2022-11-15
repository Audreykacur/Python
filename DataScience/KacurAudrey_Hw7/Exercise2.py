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

# after having created panda series from exercise 2
# create 5 lists from the panda series, one for each grade, A->F
A = list(pSerGrades[(pSerGrades >= 80) & (pSerGrades <= (100+EC))])
B = list(pSerGrades[(pSerGrades >= 80) & (pSerGrades < 90)])
C = list(pSerGrades[(pSerGrades >= 70) & (pSerGrades < 80)])
D = list(pSerGrades[(pSerGrades >= 60) & (pSerGrades < 70)])
F = list(pSerGrades[(pSerGrades >= 0) & (pSerGrades < 60)])

slices = [len(A), len(B), len(C), len(D), len(F)]
# create a pie chart where the slices are the number of elements in each one of the lists of A,B,C,D,E,F
# for colors r,g,b,y,m, start at 90 degrees, use shadow, explode the F grades in the pie chart
plt.pie(slices, labels=['A', 'B', 'C', 'D', 'F'], colors=[
        'r', 'g', 'b', 'y', 'm'], startangle=90, shadow=True, explode=(0, 0, 0, 0, 0.05), autopct='%1.1f%%')
plt.title("Homework Grades")
plt.show()
