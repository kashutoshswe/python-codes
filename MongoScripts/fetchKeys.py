''' 
Author : Ashutosh Kumar
Version : 1.0
Description : 
Email : ashutoshkumardbms@gmail.com
'''


import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['booklibrary']
mycol = mydb['books']

mydoc = mycol.find()
for x in mydoc:
    l=list(x.keys())
    print(l)


