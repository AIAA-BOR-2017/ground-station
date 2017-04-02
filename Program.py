### main runtime file ###
#mostly pseudocode at this point

import PacketParsing as pp
import Data as da
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

telnum = 0
sensordata = da.SensorData()
curimg = da.ImageFrame()
imagedata = da.ImageData()

if __name__ == "__main__":
    #do a thing
    if True: #packet received
        packet = pp.convertPacket(packet)
        if pp.isTelemetry(packet):
            telnum += 1
            sensordata.addFrame(da.SensorFrame(pp.telemetryDataAssembler(packet, telnum)))
        else:
            if curimg.addData(pp.imageDataAssembler(packet)):
                imagedata.addImage(curimg)
        
