"""
Author : Ashutosh Kumar
Version : 1.0
Description : Plotting bar graph in Python
Email : ashutoshkumardbms@gmail.com
"""

import numpy as np
import matplotlib.pyplot as plt

city = ["Delhi", "Beijing", "Washingtion", "Tokyo", "Moscow"]
pos = np.arange(len(city))
Happiness_index = [60, 40, 70, 65, 85]

plt.bar(pos, Happiness_index, color='blue', edgecolor='black')
plt.xticks(pos, city)
plt.xlabel('City', fontsize=16)
plt.ylabel('Happiness_index', fontsize=16)
plt.title('Barchart -  Happiness Index across cities', fontsize=20)
plt.show()
