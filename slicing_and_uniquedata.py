"""

Author : Ashutosh Kumar
PRN : 19030142009

Assignment: Read a path from the user and read the file line by line and then perform the given task
- the full path of the file which contains the following records
first_name,surname,phone
Salil,Parab,8392838274
Deepankar,Pundale,9837483849
...
...
Aashta,Shrivastava,7984788374


Print all lines if the first_name is unique. Ignore the line if first_name has been already printed.
Print surnames where the phone doesn't start with 9.
Print all lines where last_name is at least 4 characters and 3rd character is between a and m.
Print all lines where the phone number's first and last number is odd.

Print all lines where the first character of first_name and surname have at least 5 character difference. e.g
For Salil Parab, the difference is 3. Do not print this line.
For Deepankar Pundale, the difference is 12. Print this line.

"""


fp = ""
try:
    # opening file in read mode
    user_input = input("Enter File Path")
    fp = open(user_input, 'r')

    #various list declaration
    setOfFirstNames = []
    setOfFirstNamesLine = []
    surnames = []
    surnamesAtLeastFourChar = []
    oddPhoneNumbers = []
    characterDifference = []

    #string to check for a pattern
    alphabets = 'abcdefghijklm'

    # extracting every user from the file
    for line in fp:

        # each line removing \n
        line = line.strip('\n')

        # split the line into a list
        lineList = line.split(',')
        if lineList[0] != '\n':
            # for unique 1st names
            if lineList[0] not in setOfFirstNames:
                setOfFirstNames.append(lineList[0])
                setOfFirstNamesLine.append(line)

            # for surname whose phone number is not starting with 9
            if lineList[2][0] != '9':
                surnames.append(lineList[1])

            # for those surnames which are atleast 4 characters and whose 3rd character is in a to m
            if len(lineList[1]) >= 4 and lineList[1][2] in alphabets:
                surnamesAtLeastFourChar.append(line)

            # phone number starts and ends with odd number
            if int(lineList[2][0]) % 2 == 1 and int(lineList[2][len(lineList[2]) - 1]) % 2 == 1:
                oddPhoneNumbers.append(line)

            # character difference of 1st letter of 1st name and last name is > 5
            if abs(ord(lineList[0][0].upper()) - ord(lineList[1][0].upper())) > 5:
                characterDifference.append(line)

    # printing the lists
    print("Unique 1st Names\n", "\n".join(setOfFirstNamesLine) + "\n")
    print("Surnames whose phone does'nt start with 9 \n", "\n".join(surnames) + "\n")
    print("Last Name is atleast 4 Characters and 3rd Characters is Between a and m \n",
          "\n".join(surnamesAtLeastFourChar) + "\n")
    print("Phone Numbers 's 1st and Last Number is odd \n", "\n".join(oddPhoneNumbers) + "\n")
    print("Difference between 1st name and Surname 's 1st character is > 5 \n ", "\n".join(characterDifference) + "\n")

except FileNotFoundError:
    print("File not Found ")

except FileExistsError:
    print("File Already Exists")

except PermissionError:
    print("Permissison to open file is not granted ")

except IsADirectoryError:
    print("It is a directory")

except TypeError:
    print("Input given is incorrect")

except NameError:
    print("No such name defined")

except ValueError:
    print("Value Not Compatible")

finally:
    try:
        fp.close()
    except AttributeError:
        print("File not opened ")
