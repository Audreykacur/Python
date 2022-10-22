# create a list of numbers from 10 to 20
listOfNumbers = {10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
# out of the list create two sets
#   the first set "set A" contains the numbers 10 to 20 inclusive
setA = {c for c in listOfNumbers}
#   the second set "set B" contains the odd numbers (use set comprehension)
setB = {c for c in listOfNumbers if c % 2 != 0}

x = True


def option():  # ask the user which set they wish to carry out the operation
    letter = int(input(
        "1. Set A\n2. Set B\nEnter the value corresponding to the list which you would like to work with: "))
    if (letter == 1):
        return setA
    elif (letter == 2):
        return setB
    else:
        print("Enter a valid option")
        option()


def Add():
    print("You have chosen to add a value to the list.")
    setLetter = option()
    print(setLetter)
    addToSet = int(input("Enter a number you would like to add to a list: "))
    setLetter.add(addToSet)


def Remove():
    print("You have chosen to remove a value from the list.")
    setLetter = option()
    print(setLetter)
    addToSet = int(input("Enter a number you would like to add to a list: "))
    setLetter.remove(addToSet)


def Union():
    print("You have chosen to union two sets to find all the unique elements. ")
    print(setA.union(setB))


def Intersection():
    print("You have chosen intersection too find which elements the two sets have in common. ")
    print(setA.intersection(setB))


def diff():
    print("You have chosen difference this will tell you which numbers are in Set A that are not in Set B")
    print(setA.difference(setB))


def symdiff():
    print("You have chosen symmetric difference this will tell you which elements are not common between the two lists")
    print(setA.symmetric_difference(setB))


def disjoint():
    print("You have chosen disjoint this will tell you if there are common elements or not")
    if (setA.isdisjoint(setB)):
        print("No common elements")
    else:
        print("Common elements")


while (x):
    print("\nSet A: ", setA)
    print("Set B: ", setB)
    choice = int(input("\n1. Add a value to a list\n2. Remove a value to a list\n3. Perform a union\n4. intersection\n5. difference\n6. symmetric difference\n7. disjoint between the two sets\n\nEnter the number corresponding to the option you would like: "))

    if (choice == 1):
        Add()
    elif (choice == 2):
        Remove()
    elif (choice == 3):
        Union()
    elif (choice == 4):
        Intersection()
    elif (choice == 5):
        diff()
    elif (choice == 6):
        symdiff()
    elif (choice == 7):
        disjoint()
    else:
        print("You entered an invalid number and exited the option menu; Please try again")
        exit()
