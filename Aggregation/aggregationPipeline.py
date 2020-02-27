"""
Author : Ashutosh Kumar
Version : 1.0
Description : Other than sum we can use average as a function also, Here no duplicates, so no unwind
Email : ashutoshkumardbms@gmail.com
"""

import pymongo
import pprint

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['aggregation']
mycol = mydb['customers']

result = mydb.customers.insert_many(
    [
        {"cust_id": "A123", "amount": 500, "status": "A"},
        {"cust_id": "A123", "amount": 400, "status": "A"},
        {"cust_id": "B212", "amount": 200, "status": "A"},
        {"cust_id": "A123", "amount": 300, "status": "D"},
        {"cust_id": "A123", "amount": 500, "status": "A"},
        {"cust_id": "B212", "amount": 250, "status": "A"},
    ]
)

result = mydb.customers.aggregate(
    [
        {"$match": {"status": "A"}},
        {"$group": {"_id": "$cust_id", "Average": {"$avg": "$amount"}}}
    ])

for doc in result:
    pprint.pprint(doc)
