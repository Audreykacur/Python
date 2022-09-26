def palindrome(words):
    possible = False
    words = words.upper()
    x = (len(words))
    li = -1
    fi = 0
    for w in words:
        if words[fi] == words[li]:
            possible = True
        if possible == False:
            continue
        if possible == True:
            return words
        fi += 1
        li -= 1


words = ["Anna", "hELLo", "rotor", "wow", "CS", "kayAK", "programming"]  # list
# you can use upper() to convert a string to uppercase or round() to round a number


# use the filter() function to filter out the non-palindrome words
# the output - only uppercase characters
print(list(filter(palindrome, words)))
