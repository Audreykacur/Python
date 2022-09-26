def myToUpper(myStr):  # convert any lower case characters to upper case and print string
    str1 = ""
    y = 0
    for x in myStr:
        # converts numbers to ASCII integers to Characters
        if ((ord(myStr[y]) < 123) & (ord(myStr[y]) > 96)):
            str1 += chr(ord(myStr[y]) - 32)
        else:
            str1 += (myStr[y])
        y += 1
    print(str1)  # print the entire list


myStr = input("Please enter a string: ")  # Ask user to enter a string
upperChar = myToUpper(myStr)  # pass string to function myToUpper
