# Ask the user to enter one of the following two options
# 1. miles -> kilometers
# 2. kilometers -> miles
option = int(input(
    "Enter 1. To convert miles to kilometers\n      2. To convert kilometers to miles        "))
# ask the user to enter the distance using float
distance = float(input('Please enter the distance: '))

# pass the two input parameters to a lambda; return the converted distance use a if else in your lambda
# 1.609 kilometers makes a mile
# print(lambda distance, option: (distance * 1.609) if option == 1 else (distance / 1.609))
result = (lambda distance, option: (distance * 1.609)
          if (option == 1) else (distance / 1.609))
print("option: ", option)
print(result(distance, option))
