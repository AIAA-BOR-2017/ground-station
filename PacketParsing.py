#Packet Parsing

import Data

def isTelemetry(packet):
    if (~packet[0]&0b01000000):
        print('is telemetry')
        return True
    else:
        print('is image')
        return False
        
def telemetryDataAssembler(packet, num):
    'converts telemetry packet to sensor frame'
    batV = (packet[0]<<8) + packet[1]
    time = (packet[2]<<8) + packet[3]
    pres = (packet[4]<<4) + (packet[5]&0b11110000)
    altitude = ((packet[5]&0b00001111)<<8) + packet[6]
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
