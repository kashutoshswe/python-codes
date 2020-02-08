"""
Author : Ashutosh Kumar
Version : 1.0
Description : Create Embedded Document for Books and Reviews
Email : ashutoshkumardbms@gmail.com
"""

'''
Important Note : Mongo DB does not treat the reviews as separate records and it will treat it as independent record
This will treat the records as independent stored internally.
From the document's point of view only update happens which adds value to the array

Everytime we run this code it will insert a new record into the database
'''

import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['booklibrary']
mycol = mydb['books']

mydict = {"book_id": 2, "bookname": "title", "author": "author", "publisher": "publisher", "price": 500,
          "reviewer_name": ["add"], "review_text": ["add"],
          "review_date": ["20200102"], "rating": [5]
          }

x = mycol.insert_one(mydict)

print(" Database created !")
print(" List of databases after creating new one")
print(myclient.list_database_names())

# creating index
mycol.create_index([("book_id", pymongo.ASCENDING)], unique=True)
print("Index created !")
