"""
Author : Ashutosh Kumar
Version : 1.0
Description : Using matplotlib to draw graph
Email : ashutoshkumardbms@gmail.com
"""

import matplotlib.pyplot as plt

# x axis values
x = [1, 2, 3]

# Corresponding y axis values
y = [2, 4, 1]

plt.plot(x, y)

# naming the X-axis
plt.xlabel('X-axis')

# naming the Y-axis
plt.xlabel('Y-axis')

# giving a title to my graph
plt.title('My first graph !')

# Function to show the plot
plt.show()
