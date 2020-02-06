"""
Author : Ashutosh Kumar
Version : 1.0
Description : 
Email : ashutoshkumardbms@gmail.com
"""

import pymongo
import datetime

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['booklibrary']
mycol = mydb['reviews']

# d = datetime.datetime.strptime("2020-01-20T10:53:53.000Z", "%Y-%m-%dT%H:%M:%S.000Z")
d = datetime.datetime.now()

mydict = {"book_id": 0, "review_number": 1, "reviewer_name": "K yadav", "review_text": " This is one of the best books",
          "review_date": d, "rating": 5}

x= mycol.insert_one(mydict)

print(" Review Added ")