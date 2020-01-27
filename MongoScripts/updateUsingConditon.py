''' 
Author : Ashutosh Kumar
Version : 1.0
Description : Updating all records where conditions match
Email : ashutoshkumardbms@gmail.com
'''

import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
mycol = mydb['customers']

myquery = {"address":{"$regex":"^N"}}
newValues = { "$set":{"name":"Minnie"}}

mycol.update_many(myquery,newValues)
# print "customers after update

for x in mycol.find():
    print(x)