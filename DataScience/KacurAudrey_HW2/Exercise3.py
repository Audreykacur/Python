def countWords(stringOfChar):
    y = 1
    for x in stringOfChar:
        if (x == " "):
            y += 1
    return y  # return to the main program the number of words in the string


stringOfChar = input("Enter a string: ")  # Ask user to enter a string

wordCount = countWords(stringOfChar)  # pass string to the function countWords
print("The number of words in the string is: ", wordCount)
