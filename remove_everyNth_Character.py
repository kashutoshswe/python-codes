'''

Author : Ashutosh Kumar
PRN : 19030142009

1st Assignment - To remove every 10th letter from a file and copy the rest of the data into second file

'''

#opening file in read mode
fp = open("testdata.txt",'r')

#creating new file for new data
new_file = open("newdata.txt",'w')

#character which you can want to remove
skipped=int(input("Enter Character number to skip"))
copy_of_skip=skipped-1 #calculating index to remove character

#extracting each line
for line in fp:
    #providing index to be skipped
    skipped=copy_of_skip
    for char in line:
        #comparing each character
        if line.index(char) is not skipped:
            new_file.write(char)
        else:
            print(char,skipped)
            #calculating next index
            skipped=skipped+(copy_of_skip+1)








