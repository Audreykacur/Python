# Similarly to Ex. 1
import pandas as pd
grades_dict = {'Wally': [87, 96, 70], 'Eva': [100, 87, 90], 'Sam': [
    94, 77, 90], 'Katie': [100, 81, 82], 'Bob': [83, 65, 85]}
for entry, grade in grades_dict.items():
    Name = entry
grades = pd.DataFrame(grades_dict)
list = []
# you can use len(grades) to get the number of rows of the DataFrame
for item in range(len(grades)):
    # ask the user to enter the names of the rows(indices)
    x = input(f"Please enter row name {item} name: ")
    list.append(x)
grades.index = list
# in addition, using the sort_index() method, ask user whether they wish to sort by rows or by columns and whether to sort in ascending or descending order
bye = bool(
    input("Do you want to sort in 1. ascending or (press enter). descending order?"))
given = int(input("Do you wish to sort by 0. rows or 1. columns"))
# print("Name(sstudent Name)", Name)
if (given == 1):
    ugh = x
else:
    ugh = Name  # name of student
    # use the sort_values() method and ask user to enter values for all its three arguments
print(grades.sort_values(by=ugh, axis=given, ascending=bye))  # no
# note: if you sort by rows (ex. axis = 0) the by argument has to be followed by the name of a student : if you sort by columns (ex. axis = 1) the by argument has to be followed by the name of the assignment
