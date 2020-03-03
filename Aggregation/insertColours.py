"""
Author : Ashutosh Kumar
Version : 1.0
Description : Inserting Colours in a Collection
Email : ashutoshkumardbms@gmail.com
"""

import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['aggregation']
mycol = mydb['colours']

result = mydb.colours.insert_many(
    [
        {"code": 1, "tags": ["red", "blue"]},
        {"code": 2, "tags": ["green", "blue"]},
        {"code": 2, "tags": ["red", "green", "yellow"]},
        {"code": 2, "tags": ["yellow", "blue"]},
        {"code": 3, "tags": ["red", "blue"]},
        {"code": 3, "tags": ["green", "yellow"]},
        {"code": 3, "tags": ["red", "blue"]},
        {"code": 3, "tags": ["red"]},
        {"code": 4, "tags": ["white"]},
        {"code": 4, "tags": ["black"]},
        {"code": 5, "tags": []},
    ]
)

print("Records Inserted !")
