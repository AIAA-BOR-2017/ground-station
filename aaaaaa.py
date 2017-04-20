import serial
import time
from xbee import ZigBee
import PacketParsing as pp
import Data as da

sensordata = da.SensorData()
curimg = da.ImageFrame()
imagedata = da.ImageData()

serial_port = serial.Serial('COM3', 9600)

def print_data(data):
    """
    This method is called whenever data is received
    from the associated XBee device. Its first and
    only argument is the data contained within the
    frame.
    """
    '''
    packet = pp.convertPacket(packet)
    if pp.isTelemetry(packet):
        #telnum += 1
        sensordata.addFrame(da.SensorFrame(pp.telemetryDataAssembler(packet, 0)))
    else:
        if curimg.addData(pp.imageDataAssembler(packet)): #this statement has a side-effect of adding data to the image
            imagedata.addImage(curimg)
    '''
    print('packet received')
    data = pp.convertPacket(data['rf_data'].decode('utf-8'))
    print(pp.telemetryDataAssembler(data,0))

xbee = ZigBee(serial_port, callback=print_data, escaped=True)

while True:
    try:
        time.sleep(0.01)
    except KeyboardInterrupt:
        break

xbee.halt()
serial_port.close()
