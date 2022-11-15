# 250, 500, 1000, 2000, 3000,4000 # house square feet

# 50000,100000,200000, 400000, 600000, 800000 # house prices

# create noise derived from a standard normal (Gaussian) distribution function (ex. one with 0 mean and 1 standard deviation)

# Multiply the noise derived by 30000 and then add it to the dependent variable

# Use Ordinary Least Squares to find the regression line parameters, estimate the SSE (Sum of Squared Error), and find the Correlation Coefficient.

# Plot the data points with and without noise, along with the regression lines with and without noise, and predict house prices for the following square feet: 200, 1250, 2710, 5100

# Note 1: The following line of code produces 6 numbers from a normal distribution with 0 mean and 1 standard deviation: randomNumbers = np.random.normal(0.0, 1.0, 6)


# Note 2: Declare your arrays as: np.float64() instead of np.array or use e.g., np.array([250.]) in at least one element so as to be treated as a float array and multiplying it with an int array will also result in a float array

# Note 3: Do not use any built-in functions, apart from np.mean(), to estimate the: regression line, SSE, correlation coefficient; you can use them, though, for verification with your own results
