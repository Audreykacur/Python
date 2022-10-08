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


def names():  # names of the telephone directory are listed
    print(list(telephone.keys()))


def numbers():  # telephone numbers are listed
    print(list(telephone.values()))


while (True):  # use functions for each one of the four different operations - use an infinite loop
    option = int(input("Would you like to 1. Add\n                  2. Remove\n                  3. Modify\n                  4. Search for a telephone number(you need to provide a name)\n                  5. Display all the names\n                  6. Display all the numbers\n                  7. Exit\n                  Input: "))
    if option == 1:
        add()
    elif option == 2:
        remove()
    elif option == 3:
        modify()
    elif option == 4:
        search()
    elif option == 5:
        names()
    elif option == 6:
        numbers()
    elif option == 7:
        print("You have chosen to exit")
        break
    else:
        print("the number you entered is invalid please enter a number as your option")
    print(telephone, "\n")
