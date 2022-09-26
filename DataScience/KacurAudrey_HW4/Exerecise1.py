def srts(x): return x**.5  # lambda expression that computes the square root
#srts = lambda x: x**.5 #my lambda saves as a function 

# including floating points
# the number squared is a user entered input
number = float(input("Please enter a number you would like to square root: "))
# use the operator **
print(srts(number))
