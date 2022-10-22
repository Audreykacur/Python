# from matplotlib import pyplot as plt - i have a mac on vscode
import matplotlib.pyplot as plt

# ask the user to enter the min and max values of a function (use int)
min = int(input("Enter the minimum number: "))
max = int(input("Enter the maximum number: "))

# create a range of numbers from min to max and assign it to a variable named x
x = [c for c in range(min, max+1)]

# y = the absolute value of the range using a list comprehension
y = [c if c >= 0 else c-c-c for c in x]
print(y)

plt.plot(x, y)
plt.title("Change to Absolute Value")  # add a title
plt.xlabel("True values")  # add labels
plt.ylabel("Absolute values")
plt.show()  # plot x, y
