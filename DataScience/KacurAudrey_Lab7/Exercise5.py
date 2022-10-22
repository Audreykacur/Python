import matplotlib.pyplot as plt

# two dictionaries
COSC1310grades = {"HW1": 35, "HW2": 49, "HW3": 74, "HW4": 67, "HW5": 75}
COSC3360grades = {"HW1": 89, "HW2": 93, "HW3": 74, "HW4": 82, "HW5": 93}

# you can use the built in functions to extract the keys and values from the dictionaries
ThirteenKeys = list(COSC1310grades.keys())
ThirteenValues = list(COSC1310grades.values())

SixtyKeys = list(COSC3360grades.keys())
SixtyValues = list(COSC3360grades.values())

# set the range of values of the y-axis using: plt.ylim(0,100)


fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
ax1.set_ylim([0, 100])
ax2.set_ylim([0, 100])

# two plots on a single graph - One plot for each dictionary
# the x and y values correspond to the key and value of each dictionary
ax1.plot(ThirteenKeys, ThirteenValues, "g",
         label="COSC1310 Grades", linewidth=5, color='b')
ax2.plot(SixtyKeys, SixtyValues, 'c',
         label="COSC3360 Grades", linewidth=5, color='k')

plt.title("Homework Grades")
plt.ylabel("Grade received")  # add labels to the graph
plt.xlabel("Assignment")
# plt.legend()  # add a legend
plt.show()


# create two graphs with one plot each
# use the subplot function
