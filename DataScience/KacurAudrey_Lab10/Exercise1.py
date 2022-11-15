# Ask user to enter a line of text as a string
text = input("Enter a line of text: ")

# tokenize the string with the split method()
# output the tokens in reverse order using the reversed() and join() functions
# use space characters as delimiters
result = (" ".join([item for item in reversed(text.split())]))
print(result)
