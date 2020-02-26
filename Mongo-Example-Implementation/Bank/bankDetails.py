"""
Author : Ashutosh Kumar
Version : 1.0
Description : Provide Bank Data
Email : ashutoshkumardbms@gmail.com
"""

import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
mycol = mydb['bank']

mylist = [
    {"_id": 1, "day": 1, "NumberOfDeposits": 245},
    {"_id": 2, "day": 2, "NumberOfDeposits": 326},
    {"_id": 3, "day": 3, "NumberOfDeposits": 180},
    {"_id": 4, "day": 4, "NumberOfDeposits": 226},
    {"_id": 5, "day": 5, "NumberOfDeposits": 445},
    {"_id": 6, "day": 6, "NumberOfDeposits": 319},
    {"_id": 7, "day": 7, "NumberOfDeposits": 260},

]

x = mycol.insert_many(mylist)

# print list of the _id values of the inserted documents :
print(x.inserted_ids)