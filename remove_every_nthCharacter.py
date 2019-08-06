"""

Author : Ashutosh Kumar
PRN : 19030142009

Assignment - To remove every nth letter from a file and copy the rest of the data into second file

"""

new_file=""
fp=""
# opening file in read mode
try:
    file_name=input("Enter File Name")
    fp = open(file_name, 'r')
    # creating new file for new data
    new_file = open("newdata.txt", 'w')

    # character which you can want to remove
    skipped = int(input("Enter Character number to skip"))
    copy_of_skip = skipped - 1  # calculating index to remove character

    # extracting each line
    for line in fp:
        # providing index to be skipped
        skipped = copy_of_skip
        for char in line:
            # comparing each character
            if line.index(char) is not skipped:
                new_file.write(char)
            else:
                print(char, skipped)
                # calculating next index
                skipped = skipped + (copy_of_skip + 1)

except TypeError:
    print("Input given is incorrect")

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