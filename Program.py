### main runtime file ###
#mostly pseudocode at this point

import PacketParsing as pp
import Data as da

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import tkinter as tk
from tkinter import ttk, IntVar

telnum = 0
sensordata = da.SensorData()
curimg = da.ImageFrame()
imagedata = da.ImageData()


import serial
import time
from xbee import XBee
from xbee import ZigBee


#serial_port = serial.Serial('COM3', 9600)
#serial_port = serial.Serial('/dev/tty/usb0', 9600)
#xbee = ZigBee(serial_port, callback='print_data')
def img_graph(data):
    implt = np.asarray(data.data, dtype = np.uint8)
    plt.figure(1)
    plt.axis("off")
    plt.imshow(implt)

def telem_graph(data):
    plt.figure(2)
    plt.subplot(411)
    plt1 = data.graphData(0,1)
    plt.ylabel('voltage')
    plt.plot(plt1[0],plt1[1])
    plt.subplot(412)
    plt2 = data.graphData(0,2)
    plt.ylabel('pressure')
    plt.plot(plt2[0], plt2[1])
    plt.subplot(413)
    plt3 = data.graphData(0,3)
    plt.ylabel('temperature')
    plt.plot(plt3[0], plt3[1])
    plt.subplot(414)
    plt4 = data.graphData(0,4)
    plt.ylabel('humidity')
    plt.plot(plt4[0], plt4[1])

def print_data(data):
    """
    This method is called whenever data is received
    from the associated XBee device. Its first and
    only argument is the data contained within the
    frame.
    """
    '''
    packet = ['a','a','a','a','a','a','a','a','a','a','a','a']
    
    packet = pp.convertPacket(packet)
    if pp.isTelemetry(packet):
        telnum += 1
        sensordata.addFrame(da.SensorFrame(pp.telemetryDataAssembler(packet, telnum)))
    else:
        if curimg.addData(pp.imageDataAssembler(packet)):
            imagedata.addImage(curimg)
    '''
    print ('packet received')
    img_graph(curimg)
    telem_graph(sensordata)
    plt.draw()
    app.frame.packetcounter(2)
    print (data)
    

LARGE_FONT= ("Verdana", 12)


class GroundStationGUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Ground Station")
        
        
        container = tk.Frame(self)
        container.pack(fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_rowconfigure(1, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=1)
        container.grid_columnconfigure(2, weight=1)
        container.grid_columnconfigure(3, weight=1)
        container.grid_columnconfigure(4, weight=1)

        self.frames = {}

        frame = StartPage(container, self)
        self.frames[StartPage] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        #label = tk.Label(self, text="Ground Station", font=LARGE_FONT)
        #label.pack(pady=10,padx=10)
        
        button = ttk.Button(self, text="Turn Left",
                            command=lambda: print("turn left"))
        button.grid(row=0, column=0)
        
        button = ttk.Button(self, text="Take Picture",
                            command=lambda: self.packetcounter(1))
        button.grid(row=0, column=1)

        button = ttk.Button(self, text="Turn Right",
                            command=lambda: print("turn right"))
        button.grid(row=0, column=2)

        self.packetnumb = IntVar()
        labelpacket = ttk.Label(self, text="Packet Number: ")
        labelpacket.grid(row=0, column=3)
        labelpacketnum = ttk.Label(self, text=0, textvariable=self.packetnumb)
        labelpacketnum.grid(row=0, column=4)
        
    def packetcounter(self, val):
        self.packetnumb.set(val)


if __name__ == "__main__":
    #do a thing
    #while True:
    #    time.sleep(.01) #don't do this

    app = GroundStationGUI()
    telem_graph(sensordata)
    img_graph(curimg)
    plt.show(block=False)
    app.mainloop()



#xbee.halt()
#serial_port.close()
