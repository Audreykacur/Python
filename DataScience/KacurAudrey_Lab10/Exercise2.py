# Ask user to enter a line of text as a string
text = input("Enter a line of text: ")

# Tokenize the string using space characters as delimiters
# Output only those words ending with the letters 'ed' (see slides 275-276)
print(list(filter(lambda word: word.endswith('ed') or word.endswith(
    'ed,') or word.endswith('ed.'), text.split())))


# for word in text.split():
#     if word.endswith('ed'):
#         print(word)
