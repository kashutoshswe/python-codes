'''

Author : Ashutosh Kumar
PRN : 19030142009

Assignment: Read all the usernames from the /etc/passwd file

'''

new_file,fp=""
try:
    #opening file in read mode
    fp=open('/etc/passwd','r')

    #creating new file for usernames
    new_file=open('usernames.txt','w')

    #extracting every user from the file
    for line in fp:
        #writing it to the new file
        new_file.write(line.split(':')[0]+'\n')


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
        new_file.close();
        fp.close()
    except AttributeError:
        print("File not opened ")
