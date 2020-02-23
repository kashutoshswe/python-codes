"""
Author : Ashutosh Kumar
Version : 1.0
Description : Mapping variance and Standard Deviation
Email : ashutoshkumardbms@gmail.com
"""

import pymongo
import json
import ast
import _collections
import matplotlib.pyplot as plt
from statistics import stdev
from fractions import Fraction as fr

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
mycol = mydb['sales']

mobiles_Array = 7 * [0]
books_array = 7 * [0]
soaps_array = 7 * [0]
laptops_array = 7 * [0]

i = 0
for k in mycol.find({}, {"_id": 0, "mobiles": 1, "books": 1, "soaps": 1, "laptops": 1}):
    mobiles_Array[i] = k["mobiles"]
    books_array[i] = k["books"]
    soaps_array[i] = k["soaps"]
    laptops_array[i] = k["laptops"]
    i = i + 1

print("The Standard Deviation of Mobile is %s" % (stdev(mobiles_Array)))
print("The Standard Deviation of Books is %s" % (stdev(books_array)))
print("The Standard Deviation of Soaps is %s" % (stdev(soaps_array)))
print("The Standard Deviation of Laptop is %s" % (stdev(laptops_array)))
