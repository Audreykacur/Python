str1 = "Computer Science"


def lowerLetter(str1):
    for l in str1:
        if ord(l) > 64 and ord(l) < 91:
            return l


# the output should contain only uppercase characters
print(list(filter(lowerLetter, str1)))
