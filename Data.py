"""Data structures for Ground Station"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

class SensorFrame:
    'one frame of sensor data'

    def __init__(self, data):
        'data = (num, time, batV, pres, temp, hum, gps)'
        self.packetnum = data[0]
        self.timeSeconds = data[1]
        self.batVoltage = data[2]
        self.pressure = data[3]
        self.tempC = data[4]
        self.humidity = data[5]
        self.gpsLoc = data[6]
    def returnType(self, i):
        '0:time,1:voltage,2:pressure,3:temperature,4:humidity'
        if i == 0:
            return self.timeSeconds
        elif i == 1:
            return self.batVoltage
        elif i == 2:
            return self.pressure
        elif i == 3:
            return self.tempC
        else:
            return self.humidity
        
class SensorData:
    'all data collected'

    def __init__(self):
        self.data = []
    def addFrame(self, frame):
        self.data.append(frame)
    def graphData(self, i, j):
        '0:time,1:voltage,2:pressure,3:temperature,4:humidity'
        x = []
        y = []
        for img in self.data:
            x.append(img.returnType(i))
            y.append(img.returnType(j))
        return [x,y]

class ImageFrame:
    'one image'
    width = 640
    height = 480
    colors = 3

    def __init__(self):
        self.data = []
        self.data = [[[0 for x in range(self.colors)] for y in range(self.width)] for z in range(self.height)]

    def addData(self, packet):
        'adds one packet of image data --- packet = (packetNum, listPixels)'
        #70 pixels per packet
        packetNum = packet[0]
        listPixels = packet[1]
        xLoc = (packetNum*len(listPixels))%self.width
        yLoc = int((packetNum*len(listPixels))/self.width)

        for i in range(len(listPixels)):
            xPix = xLoc + i
            yPix = yLoc
            if xPix >= self.width:
                xPix -= self.width
                yPix += 1
            if yPix >= 480:
                yPix = 479
            #print("X: ", xPix, " Y: ", yPix)
            self.data[yPix][xPix] = listPixels[i]
        if packetNum == 8777:
            #imd.addImage(self)
            return True
        else:
            return False
        
class ImageData:
    def __init__(self):
        self.images = []

    def addImage(self, img):
        'adds an image'
        self.images.append(img)

    def getImage(self, i):
        'returns the selected image'
        return self.images[i]
    
if __name__ == "__main__":
    imf = ImageFrame()
    imd = ImageData()
    sd = SensorData()
    sd.addFrame(SensorFrame((0, 1, 1, 1, 1, 1, [0,0,0])))
    sd.addFrame(SensorFrame((0, 2, 1, 3, 2, 2, [0,0,0])))
    sd.addFrame(SensorFrame((0, 3, 2, 3, 4, 3, [0,0,0])))
    print("image gen")
    for i in range(8778):
        imf.addData((i, [[0,255,255] for j in range(35)]))
    print("gen finished")
    implt = np.asarray(imd.getImage(0).data, dtype = np.uint8)
    plt.figure(1)
    plt.axis("off")
    plt.imshow(implt)

    plt.figure(2)
    plt.subplot(411)
    plt1 = sd.graphData(0,1)
    plt.ylabel('voltage')
    plt.plot(plt1[0],plt1[1])
    plt.subplot(412)
    plt2 = sd.graphData(0,2)
    plt.ylabel('pressure')
    plt.plot(plt2[0], plt2[1])
    plt.subplot(413)
    plt3 = sd.graphData(0,3)
    plt.ylabel('temperature')
    plt.plot(plt3[0], plt3[1])
    plt.subplot(414)
    plt4 = sd.graphData(0,4)
    plt.ylabel('humidity')
    plt.plot(plt4[0], plt4[1])
    
    plt.show()
