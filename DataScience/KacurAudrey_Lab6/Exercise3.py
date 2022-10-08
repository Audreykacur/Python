telephone = {"Audrey": 1111111111, "Grace": 2222222222, "Amy": 3333333333,
             "Madelyn": 4444444444}  # create a telephone dictionary


def add():
    key = str(input(
        "Please enter the name of the person who's number you would like to add: "))
    # ask user whether they wish to add, remove, modify, search for a telephone number (given the name), or exit
    value = int(input("Please enter the number you would like to add: "))

    telephone[key] = value


def remove():
    key = str(input(
        "Please enter the name of the person who's number you would like to remove: "))
    telephone.pop(key)


def modify():
    key = str(input(
        "Please enter the name of the person who's number you would like to modify: "))
    value = int(
        input("Please enter the number you would like to change it to: "))
    telephone[key] = value


def search():
    key = str(input(
        "Please enter the name of the person who's number you would like to find: "))
    print(telephone[key], "\n")


while (True):  # use functions for each one of the four different operations - use an infinite loop
    option = int(input("Would you like to 1. add\n                  2. remove\n                  3. modify\n                  4. search for a telephone number(you need to provide a name)\n                  5. exit\n                  Input: "))
    if option == 1:
        add()
        print(telephone, "\n")
    elif option == 2:
        remove()
        print(telephone, "\n")
    elif option == 3:
        modify()
        print(telephone, "\n")
    elif option == 4:
        search()
        print(telephone, "\n")
    elif option == 5:
        print("You have chosen to exit")
        break
    else:
        print("the number you entered is invalid please enter a number as your option")
