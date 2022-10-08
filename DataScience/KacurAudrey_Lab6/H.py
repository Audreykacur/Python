
phoneBook = {}

ans = 0

while (1):

    print('\n1. look for a a contact')
    print('2. Add a contact')
    print('3. Remove a contact')
    print('4. Modify a contact')
    print('5. Print entire PhoneBook')
    print('6. Search by phoneNumber')
    print('7. Quit')
    ans = int(input())
    if ans == 1:
        print("who would you like to look up?: ")
        print("Enter a Name: ")
        name = input()
        if name in phoneBook:
            print("The number is", phoneBook[name])
        else:
            print(name, "Does not exist: ")
    elif ans == 2:

        print(" You selected add a contact")
        print("Enter name: ")
        name = input()
        print("Enter Number: ")
        phone = input()
        phoneBook[name] = phone

    elif ans == 3:
        print("Who would you like to remove? ")
        print("Enter a name: ")
        name = input()
        if name in phoneBook:
            del phoneBook[name]
        else:
            print(name, "Hmm.. not seeing this name?")
    elif ans == 4:
        print("Enter a name: ")
        name = input()
        print("Enter the number: ")
        number = input()
        phoneBook[name] = number
        print(phoneBook)

        if name in phoneBook:
            del phoneBook[name]
        else:
            print(name, "Hmm.. not seeing this name?")
    elif ans == 5:
        print("Printing list...")
        print(phoneBook)
    elif ans == 6:
        print("who would you like to look up?: ")
        print("Enter a Number: ")
        number = input()
        for name, number1 in phoneBook.items():
            if number1 == number:
                print(name)

    elif ans == 7:
        print("Bye!")
        break
