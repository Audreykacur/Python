def greetingFunction(name, greeting):

    print(greeting, name)


name = str(input("Please enter your name: "))
greeting = str(input("Please enter a greeting: "))
li = [name, greeting]


# result = lambda li:(f"{li[1]} my name is {li[0]}")
def result(li): return (f"{li[1]} my name is {li[0]}")
# my IDE does not like lambda functions so it turns it into a function
# the comment to the right of this line is my lambda function i ran in an online compiler


print((result(li)))

# name = str(input("Please enter your name: "))
# greeting = str(input("Please enter a greeting: "))
# li = [name, greeting]

# result = lambda li:(f"{li[1]} my name is {li[0]}")
# print((result(li)))
