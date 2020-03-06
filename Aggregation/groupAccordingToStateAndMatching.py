"""
Author : Ashutosh Kumar
Version : 1.0
Description : Grouping according to state and then finding state with population >100
Then we are finding the biggest city and smallest city in the State.

Email : ashutoshkumardbms@gmail.com
"""

import pymongo
import pprint

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['aggregation']
mycol = mydb['population']

result = mydb.population.insert_many(
    [
        {"_id": 1, "city": "Pune", "state": "MH", "pop": 68},
        {"_id": 2, "city": "Mumbai", "state": "MH", "pop": 240},
        {"_id": 3, "city": "Nashik", "state": "MH", "pop": 22},
        {"_id": 4, "city": "Nagour", "state": "MH", "pop": 28},
        {"_id": 5, "city": "Bhopal", "state": "MP", "pop": 30},
        {"_id": 6, "city": "Indore", "state": "MP", "pop": 45}
    ]
)

# sum and then a condition(similar to having SQL having clause
myOutput = mydb.population.aggregate(
    [
        {"$group": {"_id": "$state", "totalPop": {"$sum": "$pop"}}},
        {"$match": {"totalPop": {"$gte": 100}}}
    ]
)

for doc in myOutput:
    pprint.pprint(doc)

# least and most populated city in each state
myOutput = mydb.population.aggregate(
    [
        {
            "$group":
                {
                    "_id": {"state": "$state", "city": "$city"},
                    "pop": {"$sum": "$pop"}
                }
        },
        {"$sort": {"pop": 1}},
        {"$group":
            {
                "_id": "$_id.state",
                "biggestCity": {"$last": "$_id.city"},
                "biggestPop": {"$last": "$pop"},
                "smallestCity": {"$first": "$_id.city"},
                "smallestPop": {"$first": "$pop"}
            }
        }
    ]
)

for doc in myOutput:
    pprint.pprint(doc)
