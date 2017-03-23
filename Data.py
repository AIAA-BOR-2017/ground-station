"""Data structures for Ground Station"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

class SensorFrame:
    'one frame of sensor data'

    def __init__(self, num, time, batV, pres, temp, hum, gps):
        self.packetnum = num
        self.timeSeconds = time
        self.batVoltage = batV
        self.pressure = pres
        self.tempC = temp
        self.humidity = hum
        self.gpsLoc = gps
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
    def addFrame(self, time, batV, pres, temp, hum, gps):
        self.data.append(SensorFrame(time, batV, pres, temp, hum, gps))
    def graphData(self, i, j):
        '0:time,1:voltage,2:pressure,3:temperature,4:humidity'
        x = []
        y = []
        for frame in self.data:
            x.append(frame.returnType(i))
            y.append(frame.returnType(j))
        return [x,y]

class ImageFrame:
    'one image'
    width = 640
    height = 480
    colors = 3

    def __init__(self):
        self.data = []
        self.data = [[[0 for x in range(self.colors)] for y in range(self.width)] for z in range(self.height)]

    def addData(self, packetNum, listPixels):
        'adds one packet of image data'
        #70 pixels per packet
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
            imd.addImage(self)
        
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
    print("image gen")
    for i in range(8778):
        imf.addData(i, [[0,255,255] for j in range(35)])
    print("gen finished")
    implt = np.asarray(imd.getImage(0).data, dtype = np.uint8)
    plt.axis("off")
    plt.imshow(implt)
    plt.show()

