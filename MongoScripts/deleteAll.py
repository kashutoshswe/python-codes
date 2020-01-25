''' 
Author : Ashutosh Kumar
Version : 1.0
Description : Delete All Records
Email : ashutoshkumardbms@gmail.com
'''


import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
mycol = mydb['customers']

x = mycol.delete_many({})
print(x.deleted_count,"Documents Deleted ")