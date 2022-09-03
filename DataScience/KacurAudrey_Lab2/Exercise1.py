import myFunctions as myFun  # import function to the program

# Ask user to enter two float numbers
x = float(input("Please enter a floating point number: "))
y = float(input("Please enter a second floating point number: "))

while True:  # infinite loop
    calculation = (
        input("Please enter one of the following numerical operations+, -, *, / :"))
    if (calculation == "+"):
        myFun.addition(x, y)
    elif (calculation == "-"):
        myFun.subtraction(x, y)
    elif (calculation == "*"):
        myFun.multiplication(x, y)
    elif (calculation == "/"):
        myFun.division(x, y)
    else:
        # re-asks the user for the operation to be performed
        print("Nope: Enter a different operation")
