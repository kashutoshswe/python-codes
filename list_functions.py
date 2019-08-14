"""
uthor : Ashutosh Kumar
PRN : 19030142009

Assignment - To read a function name from the user and if the function is present for the list then perform that function
on the list else print no such function exists

"""


userinput = ""
l = [1, 2, 3, 4]
try:
    userinput = input("Enter a function of list")
    if hasattr(list, userinput):
        if userinput == 'insert':
            position = input("Enter index at which you want to enter")
            val = input("Enter value to be Inserted ")
            executionOf = "l." + userinput + "(" + position + "," + val + ")"
            eval(executionOf)

        execution = "l." + userinput + "()"
        print(execution)
        eval(execution)

    else:
        print("No such function for list")

except TypeError as e:
    listOfMessage = str(e).split()

    if listOfMessage[4] == '1':
        print("User Function %s" % userinput)
        value = input("Enter the value for to perform Function")
        new_Str = "l." + userinput + "(" + value + ")"
        print(eval(new_Str))

    if listOfMessage[3] == "one":
        if listOfMessage[0] == "extend()":
            count = int(input("Enter how many value You want to extend"))
            p = []
            for i in range(count):
                value = input("Enter new list value no %d" % i)
                p.append(value)
            l.extend(p)

        else:
            print("User Function %s" % userinput)
            value = input("Enter the value for to perform Function")

            new_Str = "l." + userinput + "(" + value + ")"
            eval(new_Str)

finally:
    print(l)
