#!/usr/bin/env python

import bme680 

def initialize_sensor():
    try:
        sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
    except (RuntimeError, IOError):
        sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)
    #initialize and return the object sensor
    return sensor 

def read_hPa(sensor):
    if sensor.get_sensor_data():
        pressure = sensor.data.pressure
        return pressure

def calculate_altitude(pressure):
    sea_level_pressure = 1013.25  # Presi0n al nivel del mar en hPa
    altitude = 44330.0 * (1.0 - pow(pressure / sea_level_pressure, 0.1903))
    return round(float(altitude),2)

if __name__ == "__main__":
    sensor = initialize_sensor()
    pressure = read_hPa(sensor)
    altitude = calculate_altitude(pressure)
 
