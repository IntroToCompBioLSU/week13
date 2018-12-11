#!/usr/bin/env python
import matplotlib.pyplot as plt
Generations=10
y=[10]
z=[10]
for gen in range(Generations):
    y.append(y[-1]*2)
    z.append(z[-1]*1.5)
print (y)
list = [round(x) for x in z]
print (list)
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(y,'b.-',label='non-glycolytic pathway')
ax.plot(list,'g--', label='glycolytic pathway')
ax.legend(['A simple line','A'])
ax.set_ylim (0,6000)
ax.set_title('Number of cancer cells in non-glycolytic pathway and glycolytic pathways')
ax.set_ylabel('Number of cells')
ax.set_xlabel('Number of cell divisions')
ax.legend(loc='upper left')
plt.show()
