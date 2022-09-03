def myFind(listOfChars):  # finds the characters in a string
    occurrences = 0
    index = 0
    for x in listOfChars:
        if (listOfChars[index] == Chars):
            # Print the index at which the character appears in the string
            print(f"{Chars} appears in the string at index: {index}")
            occurrences += 1
        index += 1
    if (occurrences == 0):
        print(f"{Chars} never appears in the string you entered. ")
    # print the number of occurrences of the character in the string
    print(f"{Chars} appears in the string {listOfChars} {occurrences} times. ")


listOfChars = input("Enter a string: ")  # ask user to enter a string
# ask user to enter a single character
Chars = input("Enter a single character you are looking for in the string: ")
myFind(listOfChars)  # pass the string to the function myFind
