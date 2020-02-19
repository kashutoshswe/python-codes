"""
Author : Ashutosh Kumar
Version : 1.0
Description : Plotting graph based on income
Email : ashutoshkumardbms@gmail.com
"""

import pymongo
import matplotlib.pyplot as plt

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
mycol = mydb['graphData']

workerNumberArray = [""] * 5
incomeArray = 5 * [0]

i = 0
for k in mycol.find({}, {"_id": 0, "workerNumber": 1, "income": 1}):
    workerNumberArray[i] = str(k["workerNumber"])
    incomeArray[i] = k["income"]
    i = i + 1

# x axis values
x = workerNumberArray
# Corresponding y axis values
y = incomeArray

# plotting the points
plt.plot(x, y)

# naming the x-axis
plt.xlabel('Worker Number')
# naming the y -axis
plt.ylabel('Income')

# giving the title to graph
plt.title('Income Graph')

# function to show the plot
plt.show()
