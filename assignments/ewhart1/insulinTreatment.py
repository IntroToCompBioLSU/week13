#!/usr/bin/env python

import matplotlib.pyplot as plt

fig = plt.figure()
fig.suptitle("Blood Glucose Levels Following Insulin Injection in Non-Diabetic Subject", fontsize=18)
plt.xlabel("Minutes Post-Injection", fontsize=14)
plt.ylabel("Glucose (mg/dL)", fontsize=14)
plt.plot([0,5,10,20,30,40,50,60], [104,98,85,70,57,44,36,51])
plt.axis([0, 60, 0, 110])
plt.show()
