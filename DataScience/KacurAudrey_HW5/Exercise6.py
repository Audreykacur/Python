# use any combination of lambda, filter, map
# convert the string element of the list to upper case
# your output should be ROBOTICS and should be string datatype not list
# your code should be one line
# you can use built in function ord() and chr() to convert a single character to ASCII and an ASCII character to character
# you can not use upper()
# you can use the function .join() to convert a list of single characters to a string
# ex. myL = ["v", "i", "s", "i", "o", "n"]
#    myStr = ".join(myL)
# you can try to filter out the non string data types then pass the string data type to a map function
# you can have a nested lambda expression
# lists = (list(filter(lambda x: (type(x) == str), myList)))  # print Robotics
# print((type(lists)))
# print(lists[0])
# separate = []
# w = map(lambda x: separate + lists[x], len(lists))
# myList = ["Robotics"]
# print(myList[0])
myList = [3, 9.45, "Robotics", 8, 1]
print("".join(list(map(lambda x: (chr(ord(x) - 32)) if (ord((x))
                                                        > 96 and ord((x)) < 123) else x, (list(filter(lambda x: (type(x) == str), myList)))[0]))))
# to uppercase a string
# def myFunction(x):
#     if (ord((x)) > 96 and ord((x)) < 123):
#         x = (chr(ord(x) - 32))
#         print(x)
#         return x
#     else:
#         print(x)
#         return x
# print(list(map(myFunction, myList[0])))

# turn the list of a string into an iterable string
# myList = str(myList[0])
# print(myList[0])
