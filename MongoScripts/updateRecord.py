''' 
Author : Ashutosh Kumar
Version : 1.0
Description : Updating a Record
Email : ashutoshkumardbms@gmail.com
'''

import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
mycol = mydb['customers']

myquery = {"address": "Python"}
newValues = {"$set": {"address": "New Address"}}

mycol.update_one(myquery, newValues)
# print "customers after update

for x in mycol.find():
    print(x)
