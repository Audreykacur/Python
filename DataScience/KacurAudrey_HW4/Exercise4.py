def str2words(wordles):
    listWords = []
    wordle = ""
    for l in wordles:
        if ord(l) != 32:
            wordle += l
        if ord(l) == 32:  # convert the string/sentence into words
            listWords.append(wordle)  # place individual words into a list
            wordle = ""
    if listWords[-1] == "":
        listWords.pop()
    return (listWords)  # return the list to main program


wordles = input("Please enter a sentence: ")  # Ask he user to enter a sentence
wordles += " "
print(str2words(wordles))  # Pass sentence to function str2words()
