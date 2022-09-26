# create your own count and index functions

def count(args):  # counts the elements passed as argument
    return (tul1.count(args))


def index(args):  # index returns the first index of the parameter passed
    return (tul1.index(args))


tul1 = (9, 3, 0, -4, 8, 7, 10, -1, 5)
print(tul1)
value = int(input("What value would you like to look for in the tuple above: "))
print(f"The value {value} is in the tuple {count(value)} times")
print(f"The value {value} is at the index {index(value)} ")
