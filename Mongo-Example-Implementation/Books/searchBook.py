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
flag = 1
mydoc = ""

try:
    print(" Let's search for a Book  ! ")
    while 1 == flag:

        user_book_id = int(input("Enter Book ID "))
        myquery = {"book_id": user_book_id}
        mydoc = mycol.find(myquery)

        if mydoc is not None:
            obj = next(mydoc, None)
            if obj:
                print("Book is present ")
                current_title = obj["bookname"]
                current_author = obj["author"]
                current_publisher = obj["publisher"]
                current_Price = obj["price"]
                current_strPrice = str(current_Price)

                print("Title :" + current_title)
                print("Author :" + current_author)
                print("Publisher :" + current_publisher)
                print("Price :" + current_strPrice)

            else:
                print(" No such Records")

        else:
            print(" No such Book ")

        flag = int(input("Do you wish to continue ? 1 for yes ! 0 for No "))

except ValueError:
    print("Invalid Value")

except TypeError:
    print("Invalid Type ")
