import pandas as pd
# Given the following dictionary:

temps = {"Mon": [68, 89], "Tue": [71, 93], "Wed": [
    66, 82], "Thu": [75, 97], "Fri": [62, 79]}

# perform the following tasks:

# Convert the dictionary into the DataFrame named temperatures with ’Low’ and ’High’ as the indices, then display the DataFrame
temperatures = pd.DataFrame(temps, index=['Low', 'High'])
print(temperatures)

# Use the column names to select only the columns for ’Mon’ through ’Wed’
print(temperatures.iloc[:, 0:3])

print(temperatures.loc[:, ['Mon', 'Tue', 'Wed']])

# Use the row index ’Low’ to select only the low temperatures for each day
print(temperatures.iloc[0:1, :])

print(temperatures.loc['Low'])

# Set the floating-point precision to 2, then calculate the average temperature for each day
pd.set_option('precision', 2)
print(temperatures.mean())

# Calculate the average low and high temperatures (you can use the mean() built-in function)
print(temperatures.T.mean())
