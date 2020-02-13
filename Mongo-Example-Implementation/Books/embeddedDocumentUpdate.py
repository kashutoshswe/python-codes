"""
Author : Ashutosh Kumar
Version : 1.0
Description : Updating the embedded records
Email : ashutoshkumardbms@gmail.com
"""
import sys
import pymongo
import datetime


myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['booklibrary']
mycol = mydb['books']

user_book_title = ""
user_book_author = ""
user_book_publisher = ""
user_book_price = 0

print(" Add review comments to a Book ")
user_book_id = int(input("Book ID :"))

myquery = {"book_id": user_book_id}
searchedDoc = mycol.find_one(myquery)

# for doc2 in mycol.find(myquery)
if searchedDoc is not None:
    # Temporarily save and print current information
    current_title = searchedDoc.get("bookname")
    current_author = searchedDoc.get("author")
    current_publisher = searchedDoc.get("publisher")
    current_price = searchedDoc.get("price")
    current_strPrice = str(current_price)

    print("Title :" + current_title)
    print("Author  :" + current_author)
    print("Publisher :" + current_publisher)
    print("Price  :" + current_strPrice)

    print("Please provide the following information ")

    user_reviewer_name = input("Reviewer Name : ")
    user_review = input(" Your Review ")
    user_date = datetime.datetime.today().strftime("%d/%m/%y %I:%M %S %p")
    user_rating = int(input(" Your Book Rating : "))

    # Now updating document

    result = mycol.update_one(
        {"book_id": user_book_id},
        {
            "$push":
                {
                    "reviewer_name": user_reviewer_name,
                    "review_text": user_review,
                    "review_date": user_date,
                    "rating": user_rating
                }
        }
    )

    print(" Book Updated Successfully ")
    print(result)

else:
    print(" No Books with the given ID ")
    print("Terminating Program")
    sys.exit()
