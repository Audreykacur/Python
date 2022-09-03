# video 8: first script ;)
print('\nHello world')

print('new\n')

# video 11: DataTypes
# Integers             int
# Floating point      float
# strings              str
# lists                list
# Dictonaries          dict
# tuples               tup
# sets                 set
# booleans             bool

# video 11: modulo - tells you how many numbers are remaining when dividing it
# 10/4 = 2.5 with 2 numbers remaining that are not evely divisible
# 10%4 = 2
print("10 % 4 =", 10 % 4)

# video 14
a = 5
a += a
print(a)
print(type(a))

myIncome = 100
myTaxRate = 0.08
myTaxes = myIncome*myTaxRate
print(myTaxes, "\n")

# video 15: slicing
# [start:stop:step]
print("Hello world")
print("How many letters are in the above statement?", len("Hello world"))

# video 16
myString = "Hello world"
print(myString[0])     # indexing 'H'
print(myString[-4])    # reverseIndexing 'o'
print(myString[6:])    # splitIndex 'world'
print(myString[:6])    # splitIndex 'Hello'
print(myString[::3])   # prints every three letters 'Hlwl'
print(myString[::-1])  # prints the list backwards


# video 17
# take the string (name = "sam") and make name = Pam
name = "Sam"
am = (name[1:])
Pam = "P" + am
print(Pam)

x = "Hello world"
print("x = Hello world")
# Look into python string methods
print("x.upper() = " + x.upper())
print("x.upper() = " + x.lower())

# split creates lists out of strings
y = x.split(' ')
print("x.split() = ", end="")
print(y)
z = x.split('l')
print("x.split(l) = ", end="")
print(z)
# NOTE: the , end=" " makes it so the next print statement does not create a new line


# video 19
# string interpolation - stick a variable into a string

# .format() method
print('This is a string {}'.format("INSERTED"))
# can call the inserted words based off of index position
print("The {2} {1} {0}".format("fox", 'brown', 'quick'))
# use key words
print("The {q} {b} {f}".format(f='fox', b='brown', q='quick'))

# float formatting '{value:width.precision}
# value is the double variable name that you would like to print
# width is how much white space you want (used for pretty formatting)
# precision is how many decimal places you would like to print
result = 100/777
print("The original result formatting = ", end="")
print(result)
print("The result was {r:.2}".format(r=result))

# formatted string literal (fstring)
name = "Audrey"
print(f"Hello, my name is {name}")
age = 21
print(f"Hello i am {name} and i am {age}")

# video 21: Lists [1,2,3]
myList = [1, 2, 3]
print("myList = [1, 2, 3]")
mySecondList = ["string", 100, 23.2]
print("len(myList) = ", end=" ")
print(len(myList))
myThirdList = ["one", "two", "three"]
a = myThirdList[0]
print("myThirdList[0] = " + a)
b = (myThirdList[1:])
print("myThirdList[1:] = ", end=" ")
print(b)
print("myList + myThirdList = ", end=" ")
print(myList + myThirdList)

# to append is to add an item to the end of a list
myList.append("walnuts")
print("myList.append('walnuts') = ", end=" ")
print(myList)

# to pop is to remove an item from the end of a list
poppedItem = myList.pop()
print("myList.pop() = ", end=" ")
print(poppedItem)

# to pop a indexed item in a list
poppedItem2 = myList.pop(1)
print("myList.pop(1) = ", end=" ")
print(poppedItem2)

# sort a list
letterList = ['z', 'f', 't', 'w', 'a', 'f']
numberList = [7, 3, 9, 0]
print("letterList = ['z', 'f', 't', 'w', 'a', 'f']")
letterList.sort()
print("letterList.sort() = ", end=" ")
print(letterList)

# reverse a list
print("numberList = [7, 3, 9, 0]")
numberList.reverse()
print("numberList.reverse() = ", end=" ")
print(numberList)

print("\n")
# video 23: Dictionaries - objects retrieved by key name
# {'Key1':'value1', 'Key2':'value2'}

myDict = {'Key1': 'Value1', "Key2": "Value2"}
print("myDict = ", end=" ")
print(myDict)

prices_lookup = {'apple': 2.99, 'oranges': 1.99, 'milk': 5.80}
print("prices_lookup['apple'] = ", end=" ")
# to look up how much an apple cost
print(prices_lookup['apple'])

print("\n")
# im tired of printing everything so no more of that
d = {'K1': 123, 'K2': [0, 1, 2], 'K3': {'insideKey': 100}}
print(d['K3']['insideKey'])

d1 = {'Key101': ['a', 'b', 'c']}
print(d1)
# this doesnt work idk why yet
# d['Key101'][2].upper()
# print(d1)
d1["k3"] = 200
print(d1)
print(d.keys())
print(d.values())
print(d.items())

print("\nvideo 25:tuples")
myTuples = (1, 2, 3)
myLists = [1, 2, 3]
print(len(myTuples))
myTuples = ('One', 2, 12, 2, 99, "One", "One")
print(myTuples[-1])
print(myTuples.count("One"))  # how many times it appears in the tuple
print(myTuples.index("One"))  # the index of the first occurrence

# use this when you want to keep data integrity

print("\nVideo 26: Sets")
# unordered collection of unique elements
# - only one representative of the same object
myset = set()
myset.add(1)
print(myset)
myset.add(2)
print(myset)
myset.add(a)
print(myset)
my1List2 = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3]
# even tho the list has multiple of each letter a set only store the value one time
print(set(my1List2))

print("\nVideo 27: Booleans in python")
# operators the convey a true or false statement
print(True)
print(type(False))
print(1 > 3)

b = None
print


print("\nFiles")
# myfile = open('testText.txt')
# myfile.read() #prints anything in the text file
# myfile.seek(0) #resets the curser to the beginning of the file
# myfiles.readlines() #prints the file data in the lines it has

# to open a file anywhere on your computer
myfile = open('/Users/audreykacur/Python2022/testText.txt')
print(myfile.read())  # prints anything in the text file
print(myfile.seek(0))  # resets the curser to the beginning of the file
print(myfile.readlines())  # prints the file data in the lines it has
myfile.close()  # make sure you close the file or you will get errors later on
# ORR
with open('/Users/audreykacur/Python2022/testText.txt') as myfile:
    print(myfile.read())
    print(myfile.seek(0))
    print(myfile.readlines())
    # you don't have to worry about closing the file this way

#
with open('/Users/audreykacur/Python2022/testText.txt', mode='w') as myfile:
    # modes: r = read; w = overwrite; a = append; r+ = read and write; w+ writing and reading(over writes existing files or creates a new file)
    contents = myfile.read()

# % % writeFile myNewFile.txt
# ONE ON FIRST
# TWO ON SECOND
# THREE ON THIRD

# with open("myNewFile.txt", mode='r') as f:
#     print(f.read())

# with open('myNewFile.txt', mode = 'a') as f:
#     f.write("\nFOUR ON FOURTH")

# with open("myNewFile.txt", mode='r') as f:
#     print(f.read())

# with open('myNewFile2.txt', mode = 'w') as f:
#     print(f.write("I created this file"))

# with open("myNewFile2.txt", mode='r') as f:
#     print(f.read())
