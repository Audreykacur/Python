def mySquareRoot(num):  # computes the square root of a number
    # if number entered is negative find the absolute value
    if num < 0:
        num = num-num-num
    # compute the square root
    num = num ** .5
    print(num)


num = int(input("Enter a value you would like to square root: "))
mySquareRoot(num)
