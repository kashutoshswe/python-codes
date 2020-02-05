'''
Author : Ashutosh Kumar
Version : 1.0
Description :
Email : ashutoshkumardbms@gmail.com
'''

import pymongo


def showRecords(book_id):
    for x in mycol.find(book_id):
        print(x)


myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['booklibrary']
mycol = mydb['books']
flag = 1
mydoc = ""

try:
    print(" We are editing a book ! ")
    while 1 == flag:
        user_book_id = int(input("Enter Book ID "))
        myquery = {"book_id": user_book_id}

        mydoc = mycol.find_one(myquery)

        if mydoc is not None:
            current_title = mydoc.get("bookname")
            current_author = mydoc.get("author")
            current_publisher = mydoc.get("publisher")
            current_Price = mydoc.get("price")
            current_strPrice = str(current_Price)

            print("Title :" + current_title)
            print("Author :" + current_author)
            print("Publisher :" + current_publisher)
            print("Price :" + current_strPrice)

            print("Please provide new values ! Press Enter if unchanged ")

            user_book_title = input("Enter Updated Book Title")
            user_book_author = input("Enter Updated Book Author")
            user_book_publisher = input("Enter Updated Book Publisher")
            user_book_price = int(input("Enter Updated Book Price"))

            if user_book_title:
                current_title = user_book_title

            if user_book_author:
                current_author = user_book_author

            if user_book_publisher:
                current_publisher = user_book_publisher

            if user_book_price:
                current_Price = user_book_price

            # Now Update in Database
            result = mycol.update_one(
                {"book_id": user_book_id},
                {
                    "$set": {"bookname": current_title,
                             "author": current_author,
                             "publisher": current_publisher,
                             "price": current_Price,
                             }
                }
            )

            print("Book Updated Successfully ")
            #showRecords(user_book_id)

        else:
            print("Book Not found \n\n")

        flag = int(input("Do you wish to continue ? 1 for yes ! 0 for No "))

except ValueError:
    print("Invalid Value")

except TypeError:
    print("Invalid Type ")
