# implement Newton's algorithm for computing the square root of a positive integer given by the user

# use a precision (threshold) value of 0.00000001

n = float(input("Enter an integer you would like to square root: "))
print(n)
x0 = n
y = n

while (y > 0.00000001):
    x1 = (x0 + (n/x0))/2
    y = x0-x1
    x0 = x1
    print(x1)
