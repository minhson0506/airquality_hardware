import threading
import sys
#sys.path.append("../../../isd22/device/rgbLed")

import board
import rgbLed.neopixel as neopixel
import time


def BreathingLed():
   
    true = 1
    while true:
        
        for i in range(0,10,1):
             pixels = neopixel.NeoPixel(board.D18 ,1)
             pixels[0] = (i,i,i)
             time.sleep(0.05)
        for i in range(10,-1,-1):
             pixels = neopixel.NeoPixel(board.D18 ,1)
             pixels[0] = (i,i,i)
             time.sleep(0.05)
       
        time.sleep(2)

if __name__ == '__main__':
    thread = threading.Thread(target=BreathingLed)
    thread.start()
