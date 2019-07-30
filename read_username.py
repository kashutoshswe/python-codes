'''

Author : Ashutosh Kumar
PRN : 19030142009

Assignment: Read all the usernames from the /etc/passwd file

'''

#opening file in read mode
fp=open('/etc/passwd','r')

#creating new file for usernames
new_file=open('usernames.txt','w')

#extracting every user from the file
for line in fp:
    #writing it to the new file
    new_file.write(line.split(':')[0]+'\n')


#closing file stream
fp.close()
new_file.close()
