''' 
Author : Ashutosh Kumar
Version : 1.0
Description : Join books and Reviews documents/Collection
Email : ashutoshkumardbms@gmail.com
'''

import pymongo
import datetime

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['booklibrary']
mycol = mydb['reviews']

result = [{'$lookup': {
    "from": "books",
    "localField": "book_id",
    "foreignField": "book_id",
    "as": "book_comments"
}}]

for doc in mycol.aggregate(result):
    print(doc)

