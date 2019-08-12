"""

Author : Ashutosh Kumar
PRN : 19030142009

Assignment - To read a file name and N-grams(How many grams do you want to distribute) from the user
Then read the file line by line and convert each line into the given N-gram format

Sample Input : This is a test sentence
Sample Output :
1. For 2 gram
output : This is
         is a
         a test
         test sentence


2.For 3 gram
output : This is a
         is a test
         a test sentence

3.For 4 gram
output : This is a test
         is a test sentence

"""

user_file = ""
try:
    user_file = input("Enter File Name")
    user_file=open(user_file,'r')
    gram = int(input("Enter how many grams "))
    for line in user_file:
        start=0
        p=line.split()
        for i in range(0,(len(p)-(gram-1))):
            print(' '.join(p[start:(start+gram)]))
            start = start+1

except NameError:
    print("No such name defined")

except TypeError:
    print(" Type not defined")

except AttributeError:
    print("No such Attribute")

except IndexError:
    print("Out of Index")

except ValueError:
    print("Invalid Value")

except FileNotFoundError:
    print("File not Found ")

except FileExistsError:
    print("File Already Exists")

except PermissionError:
    print("Permissison to open file is not granted ")

except IsADirectoryError:
    print("It is a directory")

finally:
    try:
        user_file.close()
    except AttributeError:
        print("File not opened ")