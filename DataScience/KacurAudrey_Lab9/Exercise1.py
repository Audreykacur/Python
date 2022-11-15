# Given the DataFrame of slide 241
import pandas as pd

grades_dict = {'Wally': [87, 96, 70], 'Eva': [100, 87, 90], 'Sam': [
    94, 77, 90], 'Katie': [100, 81, 82], 'Bob': [83, 65, 85]}

grades = pd.DataFrame(grades_dict)

list = []
# you can use len(grades) to get the number of rows of the DataFrame
for item in range(len(grades)):
    # ask the user to enter the names of the rows(indices)
    x = input(f"Please enter row name {item} name: ")
    list.append(x)
grades.index = list

# sort_index() method, ask user whether they wish to sort by rows or by columns
given = axis = int(
    input("Would you like to sort the data by \n0: rows \n1: columns\n"))

# whether to sort in ascending or descending order
GoingUp = bool(input(
    "Do you wish to sort the Data in Ascending or Descending order? \n1: Ascending \nPress enter key: Descending\n "))

print(grades.sort_index(axis=given, ascending=GoingUp))
