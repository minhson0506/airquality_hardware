#!/usr/bin/env python

import time
from python_tsl2591 import tsl2591

def lux():
    tsl = tsl2591()  # initialize
    full, ir = tsl.get_full_luminosity()  # Read raw values (full spectrum and infared spectrum).
    lux = tsl.calculate_lux(full, ir)  # Convert raw values to Lux.
    return round(float(lux),2)

if __name__ == "__main__":
    lux()