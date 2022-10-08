a = [0, 0, 0]
b = [0, 0, 0]
c = [0, 0, 0]

for x in range(3):  # ask the user to enter values to 3 different lists
    # 1st contain names
    a[x] = input(f"Enter the name of person {x+1}: ")
    # 2nd contain heights
    b[x] = input(f"Enter the height of person {x+1} (in inches): ")
    # 3rd contains weights
    c[x] = input(f"Enter the weight of person {x+1} (in lbs): ")

d = list(zip(a, b, c))  # zip function to zip three lists
print(d)  # print list
