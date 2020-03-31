##################
# Allison and Pan (Group 4)
# Step 3 of Project 1
# This file receives the accelerometer data from the logger microbit
# and converts it into a tuple that can be graphed
#################

import microbit as mb
import radio

radio.on()  # Turn on radio
radio.config(channel=4, length =100)

print('Program Started')
mb.display.show(mb.Image.HAPPY, delay=1000, clear=True)

# Wait for start message before beginning printing
incoming = ''
while not incoming == 'start':
    incoming = radio.receive()
print('start')


while True:
    incoming = radio.receive() # Read from radio
    if incoming is not None: # message was received
        mb.display.show(mb.Image.HEART, delay=100, clear=True, wait=False)
        # creates a data point list, then converts it into a tuple that will be graphed
        datapoint = incoming.split(",")
        datatuple=(int(datapoint[0]),int(datapoint[1]),int(datapoint[2]),int(datapoint[3]))
        print(datatuple)
        mb.sleep(10)