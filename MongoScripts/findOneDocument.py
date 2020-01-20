''' 
Author : Ashutosh Kumar
Version : 1.0
Description : Find one document, which has being 1st inserted is given back
Email : ashutoshkumardbms@gmail.com
'''

import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
mycol = mydb['customers']

x= mycol.find_one()
print(x)
