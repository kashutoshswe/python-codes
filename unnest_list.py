"""

Author : Ashutosh Kumar
PRN : 19030142009

Assignment - To unnest a given Nested List which is to convert a multi-dimensional list into a single list with
all the values in the single list
"""

try:
    # Recursive function to flatten the list
    def unnest(l):
        new_list = []
        for item in l:
            if isinstance(item, list):
                new_list.extend(unnest(item))
            else:
                new_list.append(item)
        return new_list


    print(unnest([1, 2, [3, 4, [5, 6, 6, 6], 7, 8], 9, [10, 11]]))

except NameError:
    print("No such name defined")
except TypeError:
    print(" Type not defined")
except AttributeError:
    print("No such Attribute")
