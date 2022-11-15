import pandas as pd
import numpy as np

grades_dict = {'Wally': [87, 96, 70], 'Eva': [100, 87, 90], 'Sam': [
    94, 77, 90], 'Katie': [100, 81, 82], 'Bob': [83, 65, 85]}

grades = pd.DataFrame(grades_dict)
# write your own describe function that produces the same 8 statistical results, for each one of the columns, that the built-in describe() function does.
describeDict = {'count': [], 'mean': [], 'std': [],
                'min': [], '25%': [], '50%': [], '75%': [], 'max': [], }
name = []
for item in grades_dict.keys():
    name.append(item)


def describe2():
    for column in range(len(grades.columns)):
        countem = grades.iloc[:, column:(column+1)]  # count
        describeDict['count'].append(len(countem))
        items = 0  # mean
        sum = 0  # std
        nums = []
        min = grades.iloc[0, column]  # min
        max = grades.iloc[0, column]  # max

        for row in range(len(grades)):
            if min > (grades.iloc[row, column]):  # min
                min = grades.iloc[row, column]
            if max < grades.iloc[row, column]:  # max
                max = grades.iloc[row, column]

            items += grades.iloc[row, column]  # mean
            nums.append(grades.iloc[row, column])
        nums.sort()

        # print the middle number if even print (the number above + below /2)
        x = int(len(nums)/2)
        for i in range(len(nums)):
            if len(nums) % 2 == 0:  # if even
                found = (nums[x] + nums[x+1])/2
            else:  # if odd
                found = nums[x]
        average = items / len(countem)  # mean

        # Note 1: Use the sample standard deviation formula (that is, the denominator is: N-1)
        for row in range(len(grades)):
            sum += ((grades.iloc[row, column] - average)**2)
        std = (sum / (len(countem)-1))**.5
        describeDict['std'].append(std)
        describeDict['mean'].append(average)
        describeDict['min'].append(min)
        describeDict['max'].append(max)
        describeDict['25%'].append(np.percentile(nums, 25))
        describeDict['50%'].append(found)
        describeDict['75%'].append(np.percentile(nums, 75))
    DfDesDict = pd.DataFrame(describeDict)
    DfDesDict.index = name
    print(DfDesDict)


describe2()
