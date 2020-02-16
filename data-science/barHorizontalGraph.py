"""
Author : Ashutosh Kumar
Version : 1.0
Description : Creating a Horizontal bar graph
Email : ashutoshkumardbms@gmail.com
"""

import numpy as np
import matplotlib.pyplot as plt

city = ["Delhi", "Beijing", "Washingtion", "Tokyo", "Moscow"]
pos = np.arange(len(city))
Happiness_index = [60, 40, 70, 65, 85]

plt.barh(pos, Happiness_index, color='blue', edgecolor='black')
plt.yticks(pos, city)
plt.ylabel('City', fontsize=16)
plt.xlabel('Happiness_index', fontsize=16)
plt.title('Barchart -  Happiness Index across cities', fontsize=20)
plt.show()
