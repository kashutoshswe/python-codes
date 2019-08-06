"""

Author : Ashutosh Kumar
PRN : 19030142009

Assignment - Program reads dictionary which contains student id and room number pair
and creates another dictionary which contains room number as keys which represent list of students staying in that room
"""


try:
    #crearing a dictionary with values
    dict={
    1:104,
    2:101,
    3:101,
    4:102,
    5:103,
    6:103,
    7:102,
    8:104,
    9:101,
    10:104
    }


    rooms_dict={}
    for values in set(dict.values()):
        rooms_dict[values]=[]

    for keys in dict.keys():
        rooms_dict[dict[keys]].append(keys);

    print(rooms_dict)

except NameError:
    print("No such name defined")
except TypeError:
    print(" Type not defined")
except AttributeError:
    print("No such Attribute")
