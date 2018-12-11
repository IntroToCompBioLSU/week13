#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

#Comparing the weekly earnings of people based on education recieved

#Weekly Income based on education for people age 25 and older
Education = ('Doctoral degree', 'Professional degree', 'Masters degree', 'Bachelors degree', 'Associates degree', 'some college, no degree', 'high school diploma, no college')
y_pos = np.arange(len(Education))
Income = (plt.xticks([712, 744, 836, 1173, 1401, 1836, 1743]))

ax.barh(y_pos, Income, align='center', color='green')

#Setting labels for axes
ax.set_yticks(y_pos)
ax.set_yticklabels('Education')
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Weekly Income')
ax.set_title('Education vs. Weekly Income')

plt.show()
