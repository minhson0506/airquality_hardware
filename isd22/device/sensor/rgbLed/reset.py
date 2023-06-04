import board
import neopixel

def Reset():
    pixels = neopixel.NeoPixel(board.D18 ,1)
    pixels[0] = (0,0,0)


