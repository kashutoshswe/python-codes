# Copy a single file
import shutil

while (True):
    choice = int(input("\nEnter 1 for File copy,\n 2 for Folder Copy ,\n 3 for Moving file or folder"))
    if (choice == 1):
        source = input("Enter Source of the file")
        destination = input("Enter Destination of the file")

        ch = int(input("Do you want to rename your file?"))
        if (ch == 1):
            rename = input("New Name")
            rename = destination + '\\' + rename
            shutil.copy(source, destination, rename)
        else:
            shutil.copy(source, destination)

    # Copy an entire folder
    elif(choice == 2):
        source = input("Enter Source of the folder")
        destination = input("Enter Destination of the folder")
        shutil.copytree("source", "destination")

    # Move a folder
    elif (choice == 3):
        source = input("Enter Source of the folder")
        destination = input("Enter Destination of the folder")
        shutil.move("source", "destination")

    else:
    print("Wrong Choice")

    choice = int(input("Do You want to Continue? 1 for Yes 0 for No"))
    if(choice!=1)
        break