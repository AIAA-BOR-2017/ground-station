import serial
import time
from xbee import ZigBee
import PacketParsing as pp
import Data as da

#sensordata = da.SensorData()
#curimg = da.ImageFrame()
#imagedata = da.ImageData()

serial_port = serial.Serial('COM3', 9600)
packetnum = 0

target = open('log.csv', 'w')
target.write("Packet Number,Time,Battery Voltage,Altitude,Temperature,Humidity,Lux,State,alt_th")
target.write("\n")
print("Data Collection Started")

xbee = ZigBee(serial_port, escaped=True)
while True:
    try:
        data = xbee.wait_read_frame()
        if len(data['rf_data']) == 1:
            print("Current State: %d" % data['rf_data'][0])
        else:
            data = pp.telemetryDataAssembler(data['rf_data'],packetnum)
            packetnum += 1
            target.write("%d,%d,%f,%d,%d,%d,%d,%d,%d" % data)
            target.write("\n")
            #print(data)
            points = 50 + packetnum + (data[7] == 3)*100
            print("Packet Number: %d Time: %d Battery Voltage: %f Altitude: %d Temperature: %d Humidity: %d Lux: %d State: %d alt_th: %d" % data)
            print("Est. Points: %d" % points)
    except KeyboardInterrupt:
        break

target.close()
#xbee.halt()
serial_port.close()

