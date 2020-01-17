import pymongo
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
print(myclient.list_database_names())

dblist = myclient.list_database_names()
if 'mydatabase' in dblist:
    print(" The Database Exists !")
else:
    print(" mydatabase Database not found")