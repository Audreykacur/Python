def upperCaseCharacters(myStr):  # prints the uppercase characters
    y = 0
    upperChar = 0
    for x in myStr:
        if ((ord(myStr[y]) < 91) & (ord(myStr[y]) > 64)):
            print(myStr[y])  # prints the found uppercase character
            upperChar += 1  # counts how many uppercase characters there are
        y += 1  # Increments the index
    return upperChar  # Returns the number of uppercase characters found


myStr = input("Please enter a string: ")
upperChar = upperCaseCharacters(myStr)
print("You have ", upperChar, " uppercase characters in your string")
