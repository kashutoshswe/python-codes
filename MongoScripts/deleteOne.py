''' 
Author : Ashutosh Kumar
Version : 1.0
Description : Delete One record, if in case of multiple records delete 1st one
Email : ashutoshkumardbms@gmail.com
'''


import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
mycol = mydb['customers']

myquery = {"address":"Mountain 21"}
mycol.delete_one(myquery)

print(" Delete Done ")