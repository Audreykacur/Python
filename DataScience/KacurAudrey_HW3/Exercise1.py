# implement Newton's algorithm for computing the square root of a positive integer given by the user
n = float(input("Enter an integer you would like to square root: "))
print(n)
if n < 0:
    n = n-n-n
    print("The value you entered was negative. \nThis program converts the number you entered into a positive number and square roots it :)")
x0 = n
y = n

while (y > 0.00000001):  # use a precision (threshold) value of 0.00000001
    x1 = (x0 + (n/x0))/2  # newtons algorithm
    y = x0-x1
    x0 = x1
    print(x1)
