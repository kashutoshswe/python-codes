"""
Author : Ashutosh Kumar
Version : 1.0
Description : 1st Unwind, then make colours as key, then count their occurrence , then we are sorting according to count,
if same count is present then we are sorting according to key.
Aggregation Example

Email : ashutoshkumardbms@gmail.com
"""
import pymongo
import pprint
from bson.son import SON

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['aggregation']
mycol = mydb['colours']

pipeline = [
    {"$unwind": "$tags"},
    {"$group": {"_id": "$tags", "count": {"$sum": 1}}},

    # This sort is dependent on the count and id we have provided as our filters
    {"$sort": SON([("count", -1), ("_id", -1)])},
]

pprint.pprint(list(mydb.colours.aggregate(pipeline)))
