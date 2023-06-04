import sys
#sys.path.append("../../../isd22/")

import board
import neopixel
import time

def measuring():

    pixels = neopixel.NeoPixel(board.D18 ,1)
    pixels[0] = (0,0,10)

    for i in range(10,-1,-1):
         pixels = neopixel.NeoPixel(board.D18 ,1)
         pixels[0] = (0,0,i)
         time.sleep(0.02)
    

def error():

    pixels = neopixel.NeoPixel(board.D18 ,1)
    pixels[0] = (10,0,0)

    for i in range(10,-1,-1):
         pixels = neopixel.NeoPixel(board.D18 ,1)
         pixels[0] = (i,0,0)
         time.sleep(0.02)

error()




