"""
Author : Ashutosh Kumar
Version : 1.0
Description : Inserting Sports in Collection
Email : ashutoshkumardbms@gmail.com
"""
import pprint
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['aggregation']
mycol = mydb['sport']

result = mydb.sport.insert_many(
    [
        {"_id": "Ram", "joined": "2020-01-10", "likes": ["tennis", "cricket"]},
        {"_id": "Mary", "joined": "2020-01-11", "likes": ["tennis", "cricket", "hockey"]},
        {"_id": "Abdul", "joined": "2020-01-11", "likes": ["tennis", "football"]},
        {"_id": "Beena", "joined": "2020-01-12", "likes": ["table tennis", "basketball"]},
        {"_id": "Joy", "joined": "2020-01-13", "likes": ["cricket"]},
        {"_id": "Reetu", "joined": "2020-01-13", "likes": ["cricket", "tennis"]},
        {"_id": "Aman", "joined": "2020-01-14", "likes": ["tennis"]},

    ]
)

# limit : 3 means only show the 1st three results

myOutput = mydb.sport.aggregate(
    [
        {"$unwind": "$likes"},
        {"$group": {"_id": "$likes", "number": {"$sum": 1}}},
        {"$sort": {"number": -1}},
        {"$limit": 3},
    ]
)

for doc in myOutput:
    pprint.pprint(doc)

print("Records Inserted !")
