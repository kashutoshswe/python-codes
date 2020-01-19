''' 
Author : Ashutosh Kumar
Version : 1.0
Description : Insert many records using Python
Email : ashutoshkumardbms@gmail.com
'''

import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
mycol = mydb['customers']

mylist = [{"name": "Amy", "address": "Apple st 652"},
          {"name": "Hannah", "address": "Mountain 21"},
          {"name": "Sandy", "address": "Main Road 989"},
          {"name": "Betty", "address": "Sideway 1633"}
          ]

x = mycol.insert_many(mylist)

# print list of the _id values of the inserted documents
print(x.inserted_ids)
