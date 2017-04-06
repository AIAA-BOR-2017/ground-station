### main runtime file ###
#mostly pseudocode at this point

import PacketParsing as pp
import Data as da

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

telnum = 0
sensordata = da.SensorData()
curimg = da.ImageFrame()
imagedata = da.ImageData()

'''
import serial
import time
from xbee import XBee


serial_port = serial.Serial('/dev/ttyUSB0', 9600)
xbee = ZigBee(serial_port, callback=print_data)

def print_data(data):
    """
    This method is called whenever data is received
    from the associated XBee device. Its first and
    only argument is the data contained within the
    frame.
    """
    print (data)
'''

if __name__ == "__main__":
    #do a thing
    packet = ['a','a','a','a','a','a','a','a','a','a','a','a']
    if True: #packet received
        packet = pp.convertPacket(packet)
        if pp.isTelemetry(packet):
            telnum += 1
            sensordata.addFrame(da.SensorFrame(pp.telemetryDataAssembler(packet, telnum)))
        else:
            if curimg.addData(pp.imageDataAssembler(packet)):
                imagedata.addImage(curimg)
        

'''
xbee.halt()
serial_port.close()
'''
