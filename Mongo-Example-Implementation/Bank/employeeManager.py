''' 
Author : Ashutosh Kumar
Version : 1.0
Description : Creating a Employee Management Functions(Insert,Update,Delete)
Email : ashutoshkumardbms@gmail.com
'''
import sys

import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['empolyeedata']
mycol = mydb['employees']


def main():
    while 1:
        # select option to do CRUD operation
        selection = input('\n Select 1 to insert, 2 to update, 3 to read, 4 to delete , 5 to exit \n')

        if selection == '1':
            insert()
        elif selection == '2':
            update()
        elif selection == '3':
            read()
        elif selection == '4':
            delete()
        elif selection == '5':
            print('Exiting ... ')
            sys.exit()
        else:
            print('\n Invalid Selection \n')


# Function to insert data
def insert():
    try:
        employeeId = input('Enter Employee id : ')
        employeeName = input('Enter Name : ')
        employeeAge = input('Enter age :')
        employeeCountry = input('Enter Country :')

        mydb.employees.insert_one(
            {
                "id": employeeId,
                "name": employeeName,
                "age": employeeAge,
                "country": employeeCountry
            }
        )
        print("\n Inserted Data Successfully \n")

    except ValueError:
        print("Invalid Value")

    except TypeError:
        print("Invalid Type ")


# Function to read values
def read():
    try:
        empcol = mydb.employees.find()
        print('\n All data from EmployeeData Database \n')
        for emp in empcol:
            print(emp)

    except ValueError:
        print("Invalid Value")

    except TypeError:
        print("Invalid Type ")


# Function to update a record
def update():
    try:
        criteria = input('\n Enter id to update \n')
        name = input('\n Enter Name to update : \n')
        age = input('\nEnter age to update: \n')
        country = input('\nEnter Country to update :\n')

        mydb.employees.update_one(
            {"id": criteria},
            {
                "$set": {
                    "name": name,
                    "age": age,
                    "country": country
                }
            }
        )
        print("\n Record Updated successfully \n")

    except ValueError:
        print("Invalid Value")

    except TypeError:
        print("Invalid Type ")


# Function to delete record
def delete():
    try:
        criteria = input('\n Enter id to update \n')
        mydb.employees.delete_one({"id": criteria})
        print("\n Deletion successfully \n")

    except ValueError:
        print("Invalid Value")

    except TypeError:
        print("Invalid Type ")


if __name__ == '__main__':
    main()
