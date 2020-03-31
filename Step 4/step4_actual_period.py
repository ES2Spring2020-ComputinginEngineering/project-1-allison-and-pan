# Step  4 of Project 1
# Allison and Pan (Group 4)
# This file graphs acceleration vs time and theta vs time for each
# of the different pendulum lengths, and calculation the real-life period
# for each pendulum length
# Used Backup data and Code for this part of the project

# IMPORT STATEMENTS
import os
import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.signal as sig
import scipy.constants as cons

# GLOBAL VARIABLES
path = "/Users/allisoncremer/Documents/GitHub/project1-backupdata"

# CUSTOM FUNCTIONS

def create_acceleration_array(fin):
    # create_acceleration_array creates an array with the acceleration values
    # listed in the data file imported from mu (parameter)
    # returns the array of acceleration values
    # **edit: this function was used with our original data, before we 
    # decided to use the backup code to replace our high-error data
    array = np.loadtxt(fin, delimiter=',')
    print(array)
    return array

def create_angle_array(arr):
    # create_angle_array takes in an array of accelerations as a parameter
    # and calculates the angle for each acceleration
    # returns an array of the calculated angles
    # **edit: this function was used with our original data, before we 
    # decided to use the backup code to replace our high-error data
    timelist=[]
    thetalist=[]
    array=[]
    for info in arr:
        denom=math.sqrt(info[2]*info[2]+info[3]*info[3])
        num=info[1]
        timelist.append(info[0])
        thetalist.append(math.atan2(num,denom))
    array=np.array([timelist,thetalist])
    return array

def calculate_average_period(thetaarr, timearr):
    # calculate_average_period takes in an array of angles and an array
    # of time values as parameters
    # calculates the average period by finding the maximum angle values and 
    # the time between these angle values (filtering out false positives)
    # returns the average period for a pendulum length
    thetaarr=sig.medfilt(thetaarr)
    peaks=sig.find_peaks(thetaarr)
    periodtotal=0
    count=0
    for i in range(len(peaks[0])-2):
        index1=int(peaks[0][i])
        time1=timearr[index1]
        index2=int(peaks[0][i+1])
        time2=timearr[index2]
        period=time2-time1
        while period<1 and i<len(peaks[0])-2:
            i+=1
            time2=timearr[peaks[0][i+1]]
            period=time2-time1
        periodtotal+=period
        count+=1
    averageperiod=periodtotal/count
    return averageperiod




# MAIN
os.chdir(path)

data34cm = np.loadtxt('dataset1_34cm.csv', delimiter=',')
data43cm = np.loadtxt('dataset2_43cm.csv', delimiter=',')
data53cm = np.loadtxt('dataset3_53cm.csv', delimiter=',')
data62cm = np.loadtxt('dataset4_62cm.csv', delimiter=',')
data72cm = np.loadtxt('dataset5_72cm.csv', delimiter=',')

#Crop arrays to clean data rows
data34cm =  data34cm[500:1300,:]
data43cm =  data43cm[500:1300,:]
data53cm =  data53cm[500:1300,:]
data62cm =  data62cm[500:1300,:]
data72cm =  data72cm[500:1300,:]

#Calculate accelerations in G units from milliG (and time from milliseconds to seconds)
data34cm =  data34cm/1000
data43cm =  data43cm/1000
data53cm =  data53cm/1000
data62cm =  data62cm/1000
data72cm =  data72cm/1000

#Calculate Theta and Apply Median Filter (Window size =3)
theta34 = sig.medfilt(np.arctan2(data34cm[:,1], np.sqrt(data34cm[:,2] ** 2) + (data34cm[:,3] ** 2)), 3)
theta43 = sig.medfilt(np.arctan2(data43cm[:,1], np.sqrt(data43cm[:,2] ** 2) + (data43cm[:,3] ** 2)), 3)
theta53 = sig.medfilt(np.arctan2(data53cm[:,1], np.sqrt(data53cm[:,2] ** 2) + (data53cm[:,3] ** 2)), 3)
theta62 = sig.medfilt(np.arctan2(data62cm[:,1], np.sqrt(data62cm[:,2] ** 2) + (data62cm[:,3] ** 2)), 3)
theta72 = sig.medfilt(np.arctan2(data72cm[:,1], np.sqrt(data72cm[:,2] ** 2) + (data72cm[:,3] ** 2)), 3)

#Calculate accelerations in m/s^2 units (cons.g is 9.80665 m/s^2)
data34cm[:, 1:3] =  data34cm[:, 1:3]*cons.g
data43cm[:, 1:3] =  data43cm[:, 1:3]*cons.g
data53cm[:, 1:3] =  data53cm[:, 1:3]*cons.g
data62cm[:, 1:3] =  data62cm[:, 1:3]*cons.g
data72cm[:, 1:3] =  data72cm[:, 1:3]*cons.g

#Graphs of Accelerations and Theta for each pendulum length
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize=[10,8], sharex=True)
ax1.plot(data34cm[:,0], data34cm[:,1], "#9467bd")
ax1.set_title('X Accel vs Time, Length 34cm')
ax1.set_ylabel ('Acceleration (m/s^2)')    
ax2.plot(data34cm[:,0], data34cm[:,2], "#17becf")
ax2.set_title('Y Accel vs Time')
ax2.set_ylabel ('Acceleration (m/s^2)')
ax3.plot(data34cm[:,0], data34cm[:,3], "#2ca02c")
ax3.set_title('Z Accel vs Time')
ax3.set_ylabel ('Acceleration (m/s^2)')
ax4.plot(data34cm[:,0], theta34[:], "#ff7f0e")
ax4.set_title('Theta vs Time')
ax4.set_ylabel ('Theta (rad)')
plt.xlabel('Time (s)')
plt.tight_layout()
plt.show()

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize=[10,8],sharex=True)
ax1.plot(data43cm[:,0], data43cm[:,1], "#9467bd")
ax1.set_title('X Accel vs Time, Length 43cm')
ax1.set_ylabel ('Acceleration (m/s^2)')    
ax2.plot(data43cm[:,0], data43cm[:,2], "#17becf")
ax2.set_title('Y Accel vs Time')
ax2.set_ylabel ('Acceleration (m/s^2)')
ax3.plot(data43cm[:,0], data43cm[:,3], "#2ca02c")
ax3.set_title('Z Accel vs Time')
ax3.set_ylabel ('Acceleration (m/s^2)')
ax4.plot(data43cm[:,0], theta43[:], "#ff7f0e")
ax4.set_title('Theta vs Time')
ax4.set_ylabel ('Theta (rad)')
plt.xlabel('Time (s)')
plt.tight_layout()
plt.show()

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize=[10,8],sharex=True)
ax1.plot(data53cm[:,0], data53cm[:,1], "#9467bd")
ax1.set_title('X Accel vs Time, Length 53cm')
ax1.set_ylabel ('Acceleration (m/s^2)')    
ax2.plot(data53cm[:,0], data53cm[:,2], "#17becf")
ax2.set_title('Y Accel vs Time')
ax2.set_ylabel ('Acceleration (m/s^2)')
ax3.plot(data53cm[:,0], data53cm[:,3], "#2ca02c")
ax3.set_title('Z Accel vs Time')
ax3.set_ylabel ('Acceleration (m/s^2)')
ax4.plot(data53cm[:,0], theta53[:], "#ff7f0e")
ax4.set_title('Theta vs Time')
ax4.set_ylabel ('Theta (rad)')
plt.xlabel('Time (s)')
plt.tight_layout()
plt.show()

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize=[10,8],sharex=True)
ax1.plot(data62cm[:,0], data62cm[:,1], "#9467bd")
ax1.set_title('X Accel vs Time, Length 62cm')
ax1.set_ylabel ('Acceleration (m/s^2)')    
ax2.plot(data62cm[:,0], data62cm[:,2], "#17becf")
ax2.set_title('Y Accel vs Time')
ax2.set_ylabel ('Acceleration (m/s^2)')
ax3.plot(data62cm[:,0], data62cm[:,3], "#2ca02c")
ax3.set_title('Z Accel vs Time')
ax3.set_ylabel ('Acceleration (m/s^2)')
ax4.plot(data62cm[:,0], theta62[:], "#ff7f0e")
ax4.set_title('Theta vs Time')
ax4.set_ylabel ('Theta (rad)')
plt.xlabel('Time (s)')
plt.tight_layout()
plt.show()

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize=[10,8],sharex=True)
ax1.plot(data72cm[:,0], data72cm[:,1], "#9467bd")
ax1.set_title('X Accel vs Time, Length 72cm')
ax1.set_ylabel ('Acceleration (m/s^2)')    
ax2.plot(data72cm[:,0], data72cm[:,2], "#17becf")
ax2.set_title('Y Accel vs Time')
ax2.set_ylabel ('Acceleration (m/s^2)')
ax3.plot(data72cm[:,0], data72cm[:,3], "#2ca02c")
ax3.set_title('Z Accel vs Time')
ax3.set_ylabel ('Acceleration (m/s^2)')
ax4.plot(data72cm[:,0], theta72[:], "#ff7f0e")
ax4.set_title('Theta vs Time')
ax4.set_ylabel ('Theta (rad)')
plt.xlabel('Time (s)')
plt.tight_layout()
plt.show()

print("The period for 34 cm is",calculate_average_period(sig.medfilt(theta34),data34cm[:,0]))
print("The period for 43 cm is",calculate_average_period(sig.medfilt(theta43),data43cm[:,0]))
print("The period for 53 cm is",calculate_average_period(sig.medfilt(theta53),data53cm[:,0]))
print("The period for 62 cm is",calculate_average_period(sig.medfilt(theta62),data62cm[:,0]))
print("The period for 72 cm is",calculate_average_period(sig.medfilt(theta72),data72cm[:,0]))
