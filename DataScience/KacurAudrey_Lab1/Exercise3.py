import math

sum = 0
while True:
    x = float(input("Enter a positive floating point number: "))
    if x == -999:
        break
    if x <= 0:
        continue
    else:
        sum += x
print(f"Sum = {sum}")
