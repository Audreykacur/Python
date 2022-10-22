# Create two empty lists\
HWname = []
HWgrade = []

# ask user how many HW grades they wish to enter
numOfGrades = int(input("How many grades would you like to enter: "))

# Using a single for loop enter the HW names and grades into the respected lists
# use int for the grades
for x in range(0, numOfGrades):
    EnteredHwName = input(f"Please enter Hw {x+1} name: ")
    EnteredHwGrade = int(input(f"Please enter {EnteredHwName} Grade: "))

    HWname.insert(x, EnteredHwName)
    HWgrade.insert(x, EnteredHwGrade)

# create an empty dictionary named gradesDictionary
gradesDictionary = {}

# using a separate loop, place elements of the HWname list into the keys component of the dictionary
for x in range(numOfGrades):
    gradesDictionary[HWname[x]] = HWgrade[x]
# HWgrade list elements into the value component of the dictionary

print(gradesDictionary)
