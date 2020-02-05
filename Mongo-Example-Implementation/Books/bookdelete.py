''' 
Author : Ashutosh Kumar
Version : 1.0
Description : 
Email : ashutoshkumardbms@gmail.com
'''

import pymongo


def showRecords():
    for x in mycol.find():
        print(x)


myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['booklibrary']
mycol = mydb['books']
flag = 1
mydoc = ""

try:
    while 1 == flag:
        showRecords()
        title = input("Enter Book Title you want to Delete ")

        myquery = {"bookname": title}

        mydoc = mycol.find_one(myquery)

        if mydoc is not None:
            numofRecords = mycol.delete_one(myquery)
            print(" Book Deleted ! After Deletion ")
        else:
            print(" No records Deleted")

        showRecords()
        flag = int(input("Do you wish to continue ? 1 for yes ! 0 for No "))

except ValueError:
    print("Invalid Value")

except TypeError:
    print("Invalid Type ")
