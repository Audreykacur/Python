def upperCaseCharacters(myStr):  # prints the uppercase characters
    y = 0
    upperChar = 0
    for x in myStr:
        # print(myStr[y])
        # print(ord(myStr[y]))
        if ((ord(myStr[y]) < 91) & (ord(myStr[y]) > 64)):
            print(myStr[y])
            upperChar += 1
        y += 1
    return upperChar


myStr = input("Please enter a string: ")

upperChar = upperCaseCharacters(myStr)

print("You have ", upperChar, " uppercase characters in your string")
