import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

grades_dict = {'Wally': [87, 96, 70], 'Eva': [100, 87, 90], 'Sam': [
    94, 77, 90], 'Katie': [100, 81, 82], 'Bob': [83, 65, 85]}

grades = pd.DataFrame(grades_dict)


plt.ylim(0, 100)

plt.plot(grades.T.iloc[:, 0:1], color='red', linestyle='--', marker='*',
         markerfacecolor='red', markersize=6, label='Test1')

plt.plot(grades.T.iloc[:, 1:2], color='green', linestyle='-.', marker='*',
         markerfacecolor='green', markersize=6, label='Test2')

plt.plot(grades.T.iloc[:, 2:], color='blue', linestyle='-', marker='*',
         markerfacecolor='blue', markersize=6, label='Test3')


plt.title("Student Grades")
plt.xlabel("Student Names")
plt.ylabel("Grades")
plt.legend()
plt.show()
