pi = 4  # Computes the value of pi from the following infinite series
denom = 3
# print a table that shows the value of pi approximated
print("_________________________________________")
print("Iteration:           equation:             value:      ")
print("           0                   4                  4    ")
for x in range(0, 1000000):  # 10793
    if (pi != 3.1415000095284658):  # How many approximately of this series do you have to use to get 3.1415
        if x % 2:
            pi = pi + (4/(denom))
            print(
                f"|           {x+1}      |       + 4/{denom}      |     {pi}    ")

        else:
            pi = pi - (4/(denom))
            print(
                f"|           {x+1}      |       - 4/{denom}      |     {pi}    ")
        denom += 2
print("_________________________________________________________________________________")
print(10//3)
