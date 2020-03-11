"""
Author : Ashutosh Kumar
Version : 1.0
Description : Calculating Mean,Median,Mode for the Bank Details
Email : ashutoshkumardbms@gmail.com
"""
import ast
import collections
import json

import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
mycol = mydb['bank']

# print only values
print("Deposit values ")
for x in mycol.find({}, {"_id": 0, "NumberOfDeposits": 1}):
    print(x["NumberOfDeposits"])

# print field name and value in mongodb format
for x in mycol.find({}, {"_id": 0, "NumberOfDeposits": 1}):
    y = ast.literal_eval(json.dumps(x))
    print(y)

deposit_array = 7 * [0]
i = 0
for x in mycol.find({}, {"_id": 0, "NumberOfDeposits": 1}):
    deposit_array[i] = x["NumberOfDeposits"]
    i = i + 1

print("Here are our deposit values")
# Now print array
for i in range(0, len(deposit_array)):
    print(deposit_array[i])

# length of array will be required multiple times so we are storing it
length_of_Array = len(deposit_array)

# Calculate Mean
deposit_sum = sum(deposit_array)
mean = deposit_sum / length_of_Array
# Rounding it to 2 decimal places
print("Mean is :" + str(round(mean, 2)))

# Calculate median
deposit_array.sort()

if length_of_Array % 2 == 0:
    first_median = deposit_array[length_of_Array // 2]
    second_median = deposit_array[length_of_Array // 2 - 1]
    median = (first_median + second_median) / 2
else:
    median = deposit_array[length_of_Array // 2]

print("Median is :" + str(median))

# Calculate Mode
data = collections.Counter(deposit_array)
data_list = dict(data)

max_value = max(list(data.values()))
mode_val = []
for num, freq in data_list.items():
    if freq == max_value:
        mode_val.append(num)

if len(mode_val) == length_of_Array:
    print("No mode in the list")
else:
    print("Mode is " + ','.join(map(str, mode_val)))


'''
Find at-least 3 examples practical situation where they can be used
Find extreme cases of where to use.
'''