def average(*args):
    return sum(args) / len(args)


grades = [88, 75, 96, 55, 83]
result = average(*grades)
print(result)
