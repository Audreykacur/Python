def primeNums(numbers):
    x = 0
    y = False
    x = numbers-1
    while x > 1:  # prime is a number divisible by one and itself only
        if numbers % x == 0:
            y = True
        x -= 1
    if y == False:
        return numbers


numbers = [23, 2, 9, 7, 14, 18, 3, 24, 16, 5, 8, 97]
# use the filter() function to filter out non-prime numbers
print(list(filter(primeNums, numbers)))  # output only prime numbers
