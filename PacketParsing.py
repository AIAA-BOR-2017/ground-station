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
    batV = ((packet[1]<<8) + packet[2])*(3.7/891)
    time = ((packet[3]<<24) + (packet[4]<<16) + (packet[5]<<8) + packet[6])/1000
    pres = (packet[7]<<8) + packet[8]
    temp = (packet[9]<<8) + packet[10]
    hum = (packet[11]<<8) + packet[12]
    lux = (packet[13]<<8) + packet[14]
    state = packet[15]
    alt_th = packet[16]
    #gpslat = ((packet[16]<<8) + packet[17])/100 #this is not complete
    #gpslon = ((packet[18]<<8) + packet[19])/100
    
    return (num, time, batV, pres, temp, hum, lux,state, alt_th)#, 0,0) #gpslat, gpslon)

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
