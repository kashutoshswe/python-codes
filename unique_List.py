"""

Author : Ashutosh Kumar
PRN : 19030142009

Assignment - To Remove duplicate elements from the list and create a unique list

"""

try :
    #list declaration
    list=[]
    count=int(input("Enter the size of the list"))
    for index in range(0,count):
        value=int(input("Enter Value in the list"))
        list.append(value)

    #Unique list creation
    unique = []
    for data in list:
        if data not in unique:
            unique.append(data)
    print(unique)

except NameError:
    print("No such name defined")
except TypeError:
    print(" Type not defined")
except AttributeError:
    print("No such Attribute")


