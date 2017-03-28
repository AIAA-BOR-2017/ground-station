#Packet Parsing

def isTelemetry(packet):
    if (packet[0] < 64):
        print('is telemetry')
        #do telemetry stuff to packet here
    else:
        print('is image')
        #do image stuff to packet here
    print(packet[0])
        
def telemetryDataAssembler(packet):
    batV = packet[0]<<8 + packet[1]
    print(batV)
    print(packet[0])
    print(packet[1])

def receivePacket(rawPacket):
    'converts string packet to a list of 8-bit ints'
    packet = []
    for elt in rawPacket:
        packet.append(ord(elt))
    return packet
