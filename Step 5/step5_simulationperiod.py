# Allison and Pan (Group 4)
# Step 5 of Project 1
# This file creates a numerical simulation for a pendulum utilizing physics
# equations, and graphs position, velocity, and acceleration vs. time

# IMPORT STATEMENTS
import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.signal as sig

# GLOBAL VARIABLES
gravity = 9.8
damping = .99993

# CUSTOM FUNCTIONS
def update_system(acc,pos,vel,time1,time2,armlength):
    # position and velocity update below
    dt = time2-time1
    velNext = (vel+acc*dt)*damping
    posNext = pos+vel*dt
    accNext = -1*(gravity/armlength)*math.sin(pos)
    return posNext,velNext,accNext

def print_system(time,pos,vel,acc):
    print("TIME:         ", time)
    print("POSITION:     ", pos)
    print("VELOCITY:     ", vel)
    print("ACCELERATION: ", acc, "\n")

def create_graph(time, pos, vel, acc):
    plt.figure(3, figsize=(15,10))
    # position subplot
    plt.subplot(3,1,1)
    plt.plot(time, pos, '#9467bd') 
    plt.xlabel('Time (seconds)')
    plt.ylabel('Position (m)')
    plt.title('Position vs Time')
    plt.xlim((0, 35)) 
    plt.grid()
    # velocity subplot
    plt.subplot(3,1,2)
    plt.plot(time, vel, '#17becf') 
    plt.xlabel('Time (seconds)')
    plt.ylabel('Velocity (m/s)')
    plt.title('Velocity vs Time')
    plt.xlim((0, 35)) # set x range to -1 to 8
    plt.grid()
    # acceleration subplot
    plt.subplot(3,1,3)
    plt.plot(time, acc, '#2ca02c') 
    plt.xlabel('Time (seconds)')
    plt.ylabel('Acceleration (m/s^2)')
    plt.title('Acceleration vs Time')
    plt.xlim((0, 35)) # set x range to -1 to 8
    plt.grid()
    plt.tight_layout()
    plt.show()
    
def find_peaks(arr):
    time = np.array(arr[0])
    y = np.array(arr[1])
    y_filt = sig.medfilt(y)
    y_pks, _ = sig.find_peaks(y)
    y_filt_pks, _ = sig.find_peaks(y_filt)
    return time, y, y_filt

def create_peak_graph(time, y, y_filt):
    plt.figure(3, figsize=(15,10))
    plt.subplot(2,2,1)
    plt.plot(time, y, 'r-', time[y_pks], y[y_pks], 'b.')
    plt.title('Original')
    plt.subplot(2,2,3)
    plt.plot(time, y_filt, 'r-', time[y_filt_pks], y_filt[y_filt_pks], 'b.')
    plt.title('Original Median Filtered')
    plt.tight_layout()
    plt.show()

def find_avg_period(atime, atheta):
    time = np.array(atime)
    theta = np.array(atheta)
    theta=sig.medfilt(theta)
    peaks=sig.find_peaks(theta)
    periodtotal=0
    count=0
    for i in range(len(peaks[0])-2):
        index1=int(peaks[0][i])
        time1=time[index1]
        index2=int(peaks[0][i+1])
        time2=time[index2]
        period=time2-time1
        while period<1 and i<len(peaks[0])-2:
            i+=1
            time2=time[peaks[0][i+1]]
            period=time2-time1
        periodtotal+=period
        count+=1
    averageperiod=periodtotal/count
    return averageperiod

#MAIN
# initial conditions
lengths = [.34, .43, .53, .62, .72] 
for armlength in lengths:
    print('\n\n' + str(armlength) + 'm:\n')
    pos = [(math.pi*7/6)]
    vel = [0]
    acc = [0]
    time = np.linspace(0,35,35001)
    print_system(time[0],pos[0],vel[0],acc[0])
    i = 1
    while i < len(time):
        # update position and velocity using previous values and time step
        posNext, velNext, accNext = update_system(acc[i-1],pos[i-1],vel[i-1],time[i-1],time[i],armlength)
        pos.append(posNext)
        vel.append(velNext)
        acc.append(accNext)
        #print_system(time[i],pos[i],vel[i], acc[i])
        i += 1
    create_graph(time, pos, vel, acc)
    print('The simulated period for', armlength, 'm is', find_avg_period(time, pos), 's')

