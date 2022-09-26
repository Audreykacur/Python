# Ask the user to enter one of the following two options
# 1. Fahrenheit -> Celsius
# 2. Celsius -> Fahrenheit
option = int(input(
    "Enter 1. To convert Fahrenheit to Celsius\n      2. To convert Celsius to Fahrenheit        "))
# ask the user to enter the temp using float
temp = float(input('Please enter the temperature: '))

# pass the two input parameters to a lambda; return the converted temp use a if else in your lambda
# 1.609 kilometers makes a mile
# print(lambda temp, option: (temp * 1.609) if option == 1 else (temp / 1.609))
result = (lambda temp, option: ((temp - 32) * .5556)
          if (option == 1) else ((temp * 1.8) + 32))
print("option: ", option)
print(result(temp, option))
