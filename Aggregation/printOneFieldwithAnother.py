"""
Author : Ashutosh Kumar
Version : 1.0
Description : Printing one Field with any other field
Email : ashutoshkumardbms@gmail.com
"""

import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['aggregation']
mycol = mydb['sport']

sports = mydb.sport.find()

for doc in sports:
    print(doc["_id"])
    print(doc["likes"])
