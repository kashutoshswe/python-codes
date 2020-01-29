''' 
Author : Ashutosh Kumar
Version : 1.0
Description : Selecting certain feilds for output
Email : ashutoshkumardbms@gmail.com
'''

import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
mycol = mydb['customers']

# 1st empty {} is find everything
for x in mycol.find({}, {"_id": 0, "name": 1, "address": 1}):
    print(x)

print(" Another Way !")
# another way, exclude Address
for x in mycol.find({}, {"address": 0}):
    print(x)