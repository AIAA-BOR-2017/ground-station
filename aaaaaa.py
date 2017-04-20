import serial
import time
from xbee import ZigBee

serial_port = serial.Serial('COM3', 9600)

def print_data(data):
    """
    This method is called whenever data is received
    from the associated XBee device. Its first and
    only argument is the data contained within the
    frame.
    """
    print (data['rf_data'].decode('utf-8'))

xbee = ZigBee(serial_port, callback=print_data, escaped=True)

while True:
    try:
        time.sleep(0.001)
    except KeyboardInterrupt:
        break

xbee.halt()
serial_port.close()
