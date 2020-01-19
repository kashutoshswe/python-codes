import pymongo
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
mycol = mydb['customers']

mydict ={"name": "Python", "address":"Python"}
x= mycol.insert_one(mydict);

print(" Data Inserted ")