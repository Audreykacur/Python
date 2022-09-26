# create your own count and index functions

def count(args):  # counts the elements passed as argument
    print("args: ", args)
    amountOfArgs = 0
    for x in args:
        amountOfArgs += 1
    return amountOfArgs


def index(args):  # index returns the first index of the parameter passed
    return args[0]


tul1 = (9, 3, 0, -4, 8, 7, 10, -1, 5)

print(count(tul1))
print(index(tul1))
