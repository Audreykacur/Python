# in the function convert any lower case character to uppercase and print the entire list
def myToUpper(stringOfChar):
    for i in range(len(stringOfChar)):
        stringOfChar[i] = ord(stringOfChar[i])
    # for x in range(len(stringOfChar)):
        if ((stringOfChar[i] > 65) & (stringOfChar[i] < 123)):
            stringOfChar[i] -= 32
        print(chr(stringOfChar[i]))
        stringOfChar[i] = chr(stringOfChar[i])
    print(stringOfChar)


stringOfChar = input("Please enter a string: ")  # ask user to enter a string
# convert the string to a list using the list() function ex list(myStr)
stringOfChar = list(stringOfChar)
myToUpper(stringOfChar)  # pass the list to a function myToUpper
# in the function convert any lower case character tto uppercase and print the entire list
