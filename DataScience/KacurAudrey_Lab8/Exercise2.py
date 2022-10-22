# from matplotlib import pyplot as plt - i have a mac on vscode
import matplotlib.pyplot as plt
import numpy as np

# create a numpy array with 120 elements and values that range from -1 to +10
arr = np.linspace(-1, 10, num=120)
y = np.tan(arr)  # np.tan() built-in function

# plot the tan trigonometric function
plt.plot(arr, y)
plt.title("Tan Trigonometric")  # add a title
plt.xlabel("X Values (-1 to 10)")  # add labels
plt.ylabel("Tangent of X")
plt.show()  # plot x, y
