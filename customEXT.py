"""

Author : Ashutosh Kumar
PRN : 19030142009

Assignment - Custom Extension of the given 2 lists, where we will extend the 1st list from the given position
with the second list

"""

try:
    l1 = [1, 2, 3, 4]
    l2 = [90, 11, 22]
    print(l1, l2)
    position = int(input("Enter Position From where you want to extend"))-1
    print(l1[0:position] + l2 + l1[position:])

except TypeError:
    print("Input given is incorrect")
except NameError:
    print("No such name defined")
except AttributeError:
    print("No such Attribute")
