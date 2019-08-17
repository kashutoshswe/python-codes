'''

Author : Ashutosh Kumar
PRN : 19030142009

Assignment: Read all the usernames from the /etc/passwd file and list users
which do not have bash as their default shell

'''

fp = ""
try:
    # opening file in read mode
    fp = open('/etc/passwd', 'r')

    # extracting every user from the file
    for line in fp:
        # writing it to the new file
        if 'bash' not in line:
            print(line.split(':')[0])


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
        fp.close()
    except AttributeError:
        print("File not opened ")


