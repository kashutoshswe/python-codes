"""
Author : Ashutosh Kumar
Version : 1.0
Description :  Search using Or Condition
Email : ashutoshkumardbms@gmail.com
"""

import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['booklibrary']
mycol = mydb['books']

print(" List Books ... Enter Author, Publisher, and Price Range to search ")

user_title = input("Book title : ")
user_author = input(" Book Author ")
user_min_price = int(input(" Minimum Price : "))
user_max_price = int(input(" Maximum Price  : "))

myquery = {
    "$or":
        [
            {"title": {"$eq": user_title}},
            {"author": {"$eq": user_author}},
            {"price": {"$gte": user_min_price, '$lte': user_max_price}} # Here it will check for an And condition       
        ]
}

searchedDoc = mycol.find(myquery)

if searchedDoc is None:
    print(" No Books found for the matching criteria ")
else:
    for doc in mycol.find(myquery):
        print(doc)
