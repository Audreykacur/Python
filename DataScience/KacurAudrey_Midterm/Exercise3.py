# from matplotlib import pyplot as plt - i have a mac on vscode
import matplotlib.pyplot as plt

Dictions = {"HW1": 93, "HW2": 85, "HW3": 94, "HW4": 90, "HW5": 82}

# create a plot with HW name = x and grades = y
plt.plot(Dictions.keys(), Dictions.values())

# find the min and max grades of the dictionary label those points
keyList = list(Dictions.keys())
valueList = list(Dictions.values())

minVal = valueList[0]
for x in range(len(valueList)):
    if minVal > valueList[x]:
        minVal = valueList[x]
        minIndex = x

maxVal = valueList[0]
for x in range(len(valueList)):
    if maxVal < valueList[x]:
        maxVal = valueList[x]
        maxIndex = x

# create two scatter plots with min and max values
plt.scatter(keyList[minIndex], minVal,
            label="Min Grade", color='r')  # red = min
plt.scatter(keyList[maxIndex], maxVal,
            label="Max Grade", color='g')  # green = max

plt.ylim(0, 100)  # set the limits of the y axis

# add the labels
plt.xlabel("HW Name")  # xlabel
plt.ylabel("Grade")  # ylabel
plt.title("HW grades plot")  # title
plt.legend()  # legend

plt.show()
