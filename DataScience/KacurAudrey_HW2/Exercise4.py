def myToUpper(stringOfChar):
    for i in range(len(stringOfChar)):
        stringOfChar[i] = ord(stringOfChar[i])  # Convert characters to ASCII
        if ((stringOfChar[i] > 96) & (stringOfChar[i] < 123)):
            stringOfChar[i] -= 32  # convert lowercase character to uppercase
        print(chr(stringOfChar[i]))  # print the uppercase characters
        stringOfChar[i] = chr(stringOfChar[i])  # convert ASCII to characters
    print(stringOfChar)  # print the entire list


stringOfChar = input("Please enter a string: ")  # ask user to enter a string
stringOfChar = list(stringOfChar)  # convert the string to a list
myToUpper(stringOfChar)  # pass the list to a function myToUpper
