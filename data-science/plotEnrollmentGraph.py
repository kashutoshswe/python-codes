"""
Author : Ashutosh Kumar
Version : 1.0
Description : Plotting Enrollment Graph
Email : ashutoshkumardbms@gmail.com
"""

import pymongo
import matplotlib.pyplot as plt

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
mycol = mydb['bar']

yearArray = [0] * 5
enrollmentArray = 5 * [0]

i = 0
for k in mycol.find({}, {"_id": 0, "year": 1, "enrollments": 1}):
    yearArray[i] = k["year"]
    enrollmentArray[i] = k["enrollments"]
    i = i + 1

plt.bar(yearArray, enrollmentArray, color='blue', edgecolor='black')
plt.xticks(yearArray)
plt.xlabel('Year', fontsize=16)
plt.ylabel('Enrollments', fontsize=16)
plt.title('Barchart -  Enrollments', fontsize=20)
plt.show()
