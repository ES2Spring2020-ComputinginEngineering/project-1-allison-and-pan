# Step Two of Project 1
# Allison and Pan
# This file graphs the theoretical periods vs. lengths of  the pendulum
# We worked alone on this assignment

# IMPORT STATEMENTS
import matplotlib.pyplot as plt
import math
import numpy as np

# GLOBAL VARIABLES
lengths=[.34,.43,.53,.62,.72]
lengths_array=np.array(lengths)

# CUSTOM FUNCTIONS
def swing_period(lengths):
    # swing_period takes in an array of lengths as a parameter
    # returns an array of periods calculated for each length
    periods=[]
    for i in range(len(lengths)):
        period=2*math.pi*math.sqrt(lengths[i]/9.8)
        periods.append(period)
    periodarray=np.array(periods)
    return periodarray
        
def graph_values(lengths,periods):
    # graph_values takes an array of lengths and an array of periods as parameters
    # graphs length vs period for a theoretical model
    plt.plot(lengths, periods)
    plt.ylabel("Period(s)")
    plt.xlabel("Length (m)")
    plt.axis([0,1,0,2])
    plt.show()
    
periods=swing_period(lengths)
print("The period for 34 cm is: ",periods[0])
print("The period for 43 cm is: ",periods[1])
print("The period for 53 cm is: ",periods[2])
print("The period for 62 cm is: ",periods[3])
print("The period for 72 cm is: ",periods[4])
graph_values(lengths, periods)
    
    