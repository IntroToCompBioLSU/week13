#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

Class = ('Anthro', 'CompBio', 'Ecology', 'PhysLab', 'BioChem')
y_pos = np.arange(len(Class))
grade = (99, 88, 85, 97, 79)
 
plt.bar(y_pos, grade, align='center', alpha=0.5, color='#9400D3')
plt.xticks(y_pos, Class)
plt.ylabel('Percentage')
plt.title('Grades for Fall 2019 Semester')
 
plt.show()