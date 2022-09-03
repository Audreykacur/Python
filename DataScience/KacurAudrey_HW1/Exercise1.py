
def myFactorialWithForLoop(x):  # compute the factorial using a for loop
    sum = x
    print(f"for   loop - factorial of {x}!:", end=" ")
    for number in range(0, x-1):
        print(x, end=" * ")
        x -= 1
        sum *= x
        # print results
    print(f"{x} = {sum}")


def myFactorialWithWhileLoop(x):  # compute the factorial using a while loop
    sum = x
    print(f"while loop - factorial of {x}!:", end=" ")
    while x > 1:
        print(x, end=" * ")
        x -= 1
        sum *= x
        # print results
    print(f"{x} = {sum}")  # print results


# main program
# asks user to enter an integer
x = int(input("Enter a value you would like to factorial: "))
myFactorialWithForLoop(x)  # pass the integer to myFactorialWithForLoop
myFactorialWithWhileLoop(x)  # pass the integer to myFactorialWithWhileLoop
