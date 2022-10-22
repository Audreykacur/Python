import numpy as np
import matplotlib.pyplot as plt

# ask the user to enter a min, max and step values for the x-axis
min = 10  # int(input("please enter a value for the minimum x-axis value: "))
max = 20  # int(input("please enter a value for the maximum x-axis value: "))
step = 2  # int(input("please enter a value for the step x-axis value: "))

# use the np.arange() function with the three values the user entered in order to create an array named x
x = np.arange(min, max, step)

# for the y array use the eval() function and ask user to enter an expression
y = eval(input("Enter an expression that you would like to complete on the x values: "))

plt.plot(x, y, color='b', label='y to x')
plt.title("Value after expression")
plt.xlabel("Value of x")
plt.ylabel("Value of y")
plt.legend()
plt.show()

# Note 1: eval() is a powerful function that can parse a string and convert it into an expression, that is, eval(expression) where expression = ’x**2’ will raise all x values to the power of 2

# Note 2: For more examples with the eval() function you may check the online tutorials on programiz and geeksforgeeks
