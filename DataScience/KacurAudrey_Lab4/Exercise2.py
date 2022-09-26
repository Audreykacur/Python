str1 = "Computer Science"

# use a filter to filter out constants your output should only contain vowels

str1 = "Computer Science"


def lowerLetter(str1):
    for l in str1:
        if ord(l) == 97 or ord(l) == 65 or ord(l) == 69 or ord(l) == 101 or ord(l) == 105 or ord(l) == 73 or ord(l) == 111 or ord(l) == 79 or ord(l) == 85 or ord(l) == 117:
            return l


# the output should contain only uppercase characters
print(list(filter(lowerLetter, str1)))
