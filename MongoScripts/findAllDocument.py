''' 
Author : Ashutosh Kumar
Version : 1.0
Description : Find all documents and print them(similar to Select * )
Email : ashutoshkumardbms@gmail.com
'''


import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
mycol = mydb['customers']

for x in mycol.find():
    print(x)
