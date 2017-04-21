import serial
import time
from xbee import ZigBee
import PacketParsing as pp
import Data as da

sensordata = da.SensorData()
curimg = da.ImageFrame()
imagedata = da.ImageData()

serial_port = serial.Serial('COM3', 9600)
packetnum = 0

target = open('log.csv', 'w')
target.write("Packet Number,Time,Battery Voltage,Pressure,Temperature,Humidity,GPS")
target.write("\n")
print("Data Collection Started")

xbee = ZigBee(serial_port, escaped=True)
while True:
    try:
        data = xbee.wait_read_frame()
        data = pp.telemetryDataAssembler(data['rf_data'],packetnum)
        packetnum += 1
        target.write("%d,%d,%d,%d,%d,%d,%d" % data)
        target.write("\n")
        #print(data)
    
        print("Packet Number: %d Time: %d Battery Voltage: %d Pressure: %d Temperature: %d Humidity: %d GPS: %d" % data)
        print("Est. Points: %d" % data[0]*1)
    except KeyboardInterrupt:
        break

target.close()
#xbee.halt()
serial_port.close()

