#Packet Parsing

import Data

def isTelemetry(packet):
    if (packet[0] < 64):
        print('is telemetry')
        #do telemetry stuff to packet here
    else:
        print('is image')
        #do image stuff to packet here
    print(packet[0])
        
def telemetryDataAssembler(packet, num):
    'converts telemetry packet to sensor frame'
    batV = (packet[0]<<8) + packet[1]
    time = (packet[2]<<8) + packet[3]
    pres = packet[4] #this is not complete
    altitude = packet[5] + packet[6] #this is not complete
    temp = (packet[7]<<8) + packet[8]
    hum = (packet[9]<<8) + packet[10]
    gps = packet[11] #this is not complete
    return (num, time, batV, pres, temp, hum, gps)

def imageDataAssembler(packet):
    'converts image packet to image section tuple'
    num = ((packet[0]&0b00111111)<<8) + packet[1]
    return (num, packet[2:])
    

def convertPacket(rawPacket):
    'converts string packet to a list of 8-bit ints'
    packet = []
    for elt in rawPacket:
        packet.append(ord(elt))
    return packet
