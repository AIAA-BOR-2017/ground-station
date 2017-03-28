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
    
