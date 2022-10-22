# from matplotlib import pyplot as plt - i have a mac on vscode
import matplotlib.pyplot as plt
import numpy as np

# Create a numpy array with values from -1 to +10 and a step of 0.1
arr = np.arange(-1, 10, .1)
y = np.cos(arr)  # np.cos() built-in function

# Plot the cos trigonometric function
plt.plot(arr, y)
plt.title("COS Trigonometric")  # add a title
plt.xlabel("X Values (-1 to 10)")  # add labels
plt.ylabel("Cosine of X")
plt.show()  # plot x, y
