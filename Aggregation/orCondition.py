"""
Author : Ashutosh Kumar
Version : 1.0
Description : Performing Or condition using Mongo
Email : ashutoshkumardbms@gmail.com
"""

import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['empolyeedata']
mycol = mydb['employees']

empcol = mydb.employees.find()
print("Finding OR Condition")

# All data
for emp in empcol:
    print(emp)

# With Or Condition
empcol = mydb.employees.find(
    {
        "$or":
            [
                {"age": {"$gte": "50"}},
                {"country": {"$eq": "India"}}
            ]
    }
)

print("\n Selected data from employee Database  \n")
for emp in empcol:
    print(emp)
