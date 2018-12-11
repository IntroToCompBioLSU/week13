#!/usr/bin/env python

#week 13
#Pick two plot types from this gallery, figure out how to plot them, and
#create a figure with both plots on it.

#importing matplotlib.pyplot and numpy
import matplotlib.pyplot as plt
import numpy as np 


fig, ax = plt.subplots(2, 1, figsize=(10, 10)) 
#setting the figure size to 10 inches by 10 inches
#entire figure has 2 axes (2 graphs) by 2 axes (2 graphs)


#Neuron Fiber Recruitment
#data for the effects of stimulus voltage on the percentage of neurons within a nerve fired
pnf=([0.5,10,12,13,20,25,30,35,50,60,70,80,70,90,100,30]) #percentage of neurons fired values
sv=([50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]) #stimulus voltage values

ax[0].bar(sv, pnf, width=10.0) #construction of bar graph at axes [0,0]
ax[0].set_ylabel("Percentage of Neurons Fired") #setting y axis label
ax[0].set_xlabel("Stimulus Voltage (mV)") #setting x axis label
ax[0].set_title("Effects of Stimulus Voltage on \n Nerve Fiber Recruitment \n within Skeletal Muscle") #setting title of graph

#Muscle Stretch
#data for the effects of stress on skeletal muscle contractile activity
stretch = ([0,1,2,3,4,5,6,7,8,9,10]) #stretch imposed on the muscle values
ca=([30,50,60,70,80,90,120,80,20,9,0])#contraction amplitude values

ax[1].fill(stretch, ca, "r") #construction of filled curve at axes [0,1]
ax[1].set_ylabel("Contraction Amplitude (N)") #setting y axis label
ax[1].set_xlabel("Stretch Imposed (mm)") #setting x axis label
ax[1].set_title("Effects of Stretch on Contractile Activity \n of Skeletal Muscle") #setting title of graph

plt.show() #displays figure consisting of subplots

# DB: Good! I just adjusted to consist of only 2 subplots in this case.