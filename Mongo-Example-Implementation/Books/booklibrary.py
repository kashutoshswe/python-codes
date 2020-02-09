''' 
Author : Ashutosh Kumar
Version : 1.0
Description : To create a Book Library Database
Email : ashutoshkumardbms@gmail.com
'''

import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['booklibrary']
mycol = mydb['books']
flag = 1

newPrimaryKey = mycol.count()

# creating index
mycol.create_index([("book_id",pymongo.ASCENDING)],unique=True)

try:
    while 1 == flag:
        title = input("Enter Book Title")
        author = input("Enter Book Author")
        publisher = input("Enter Book Publisher")
        price = int(input("Enter Book Price"))

        #mydict = {"__id":1 ,"book_id": newPrimaryKey, "bookname": title, "author": author, "publisher": publisher, "price": price}
        mydict = {"book_id": newPrimaryKey, "bookname": title, "author": author, "publisher": publisher, "price": price}

        x = mycol.insert_one(mydict)
        print("Record Inserted ")
        newPrimaryKey = newPrimaryKey + 1
        flag = int(input("Do you wish to continue ? 1 for yes ! 0 for No "))


except pymongo.errors.DuplicateKeyError:
    print("Duplicate Key Error ")

except ValueError:
    print("Invalid Value")

except TypeError:
    print("Invalid Type ")
