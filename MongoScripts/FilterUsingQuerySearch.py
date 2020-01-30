''' 
Author : Ashutosh Kumar
Version : 1.0
Description : Search results which have values greater than S(compare with Ascii)
Email : ashutoshkumardbms@gmail.com
'''

import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
mycol = mydb['customers']

# greater than S, $ specifies that it is greater than S, S,T,U,V,W...

myquery = {"address": {"$gt": "S"}}
mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)
