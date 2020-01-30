''' 
Author : Ashutosh Kumar
Version : 1.0
Description : Find data using Regular Expressions
Email : ashutoshkumardbms@gmail.com
'''

import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
mycol = mydb['customers']

# regex expression for 1st letter S
myquery = {"address": {"$regex": "^S"}}
mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)
