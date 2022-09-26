grades = [90, 74, 87, 80]
# the algorithm should compute the average grade regardless of the length of the list
# use lambda to compute the average grade
average = lambda *args: sum(args) / len(args)
grades = [88, 75, 96, 55, 83]
print(average(*grades))

# grades = [90, 74, 87, 80]
# # the algorithm should compute the average grade regardless of the length of the list
# # use lambda to compute the average grade
# average = lambda *args: ("sum(args) / len(args)")
# grades = [88, 75, 96, 55, 83]
# print(average(*grades))
