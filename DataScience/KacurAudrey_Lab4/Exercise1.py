def myFind(numbers, num):
    # find any occurrence of the number in the list
    x = 0
    listIndex = []
    for n in numbers:
        if n == num:
            listIndex.append(x)  # add index the number is found to list
        x += 1
    if listIndex == "":
        return (f"The number {num} was not found in the index. Try again")
    return listIndex

    # print(numbers.index(num))


numbers = [9, -3, 7, 2, 1, 2, 9, 9, 8, 2, 0, 0, 9, 2]
num = int(input("Please Enter a Number: "))  # ask user to enter a number

# pass list and num to function myFind() and print list
print(myFind(numbers, num))
