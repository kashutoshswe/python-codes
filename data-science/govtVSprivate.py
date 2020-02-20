"""
Author : Ashutosh Kumar
Version : 1.0
Description : Plotting Stat graph for Goverment vs Non-goverment companies
Email : ashutoshkumardbms@gmail.com
"""

import pymongo
import matplotlib.pyplot as plt

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
mycol = mydb['govermentVSprivate']

yearArray = 5 * [0]
numberOfGovtCompaniesArray = 5 * [0]
numberOfNonGovtCompaniesArray = 5 * [0]

Type = ['Govt', 'Non Govt']

i = 0
for k in mycol.find({}, {"_id": 0, "year": 1, "numberOfGovtCompanies": 1, "numberOfNonGovtCompanies": 1}):
    yearArray[i] = k["year"]
    numberOfGovtCompaniesArray[i] = k["numberOfGovtCompanies"]
    numberOfNonGovtCompaniesArray[i] = k["numberOfNonGovtCompanies"]
    i = i + 1

plt.bar(yearArray, numberOfGovtCompaniesArray, color='blue', edgecolor='black')
plt.bar(yearArray, numberOfNonGovtCompaniesArray, color='red', edgecolor='black')

plt.xticks(yearArray)
plt.xlabel('Year', fontsize=16)
plt.ylabel('Number of Companies', fontsize=16)
plt.title('Stacked Barchart -  Enrollments', fontsize=20)

# Type to show that it is a Stacked Graph
plt.legend(Type, loc=2)
plt.show()
