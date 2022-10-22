import matplotlib.pyplot as plt

fruitName = ['Apples', 'Oranges', 'Cherries', 'Watermelon']
fruitQuantity_2020 = [25, 25, 10, 18]
fruitQuantity_2021 = [22, 18, 9, 19]

# create 4 subplots
fig, ax = plt.subplots(nrows=2, ncols=2)

# plot
ax[0][0].plot(fruitName, fruitQuantity_2020, label='2020', color='b')
ax[0][0].plot(fruitName, fruitQuantity_2021, label='2021', color='c')
ax[0][0].set_title("Plot")
ax[0][0].legend()

# scatter
ax[0][1].scatter(fruitName, fruitQuantity_2020, label='2020', color='b')
ax[0][1].scatter(fruitName, fruitQuantity_2021, label='2021', color='c')
ax[0][1].set_title("Scatter")
ax[0][1].legend()

# stack
ax[1][0].plot([], [], label='2020', color='b')
ax[1][0].plot([], [], label='2021', color='c')
ax[1][0].stackplot(fruitName, fruitQuantity_2020,
                   fruitQuantity_2021, colors=['b', 'c'])
ax[1][0].set_title("Stack Plot")
ax[1][0].legend()

# pie
compress_fruit = [fruitQuantity_2020[i] + fruitQuantity_2021[i]
                  for i in range(len(fruitQuantity_2020))]  # for the pie chart add the respective elements from the two lists, resulting in one list
ax[1][1].pie(compress_fruit, labels=fruitName)
ax[1][1].set_title("Pie Plot")
plt.show()

# x-axis : list - fruit name
# y-axis : fruitQuantity_2020 and fruitQuantity_2021
