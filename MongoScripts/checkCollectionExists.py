import pymongo
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']

colllist = mydb.list_collection_names()
if "customers" in colllist:
    print(" Collection Customers Exists ")
else:
    print(" Collection Does not Exists ")
