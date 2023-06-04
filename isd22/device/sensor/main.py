import os
import sys
import time
import deviceName
import deviceId
import math
sys.path.append(".")
import threading
import pymongo
from datetime import datetime
from rgbLed.breathingLed import BreathingLed
from rgbLed.statusIndicator import error, measuring
from _tsl2591 import lux
from sensirion_i2c_driver import I2cConnection, LinuxI2cTransceiver
from sensirion_i2c_sen5x import Sen5xI2cDevice
from sen5X import sensirion
from _bme680 import read_hPa
from _bme680 import initialize_sensor
from _bme680 import calculate_altitude
from _mhz19 import*
from mic import *
from pymongo import MongoClient

#Establish connection with MongoDB Atlas
client = MongoClient("mongodb URI") #to be replaced
db = client["innovation"]
collection = db["sensordatas"]

device_Id = deviceId.generate_and_load_id()
device_Name = deviceName.generate_name()
      
def main():
    print("Metropolia: Innovation project")
    time.sleep(0.5)
    print("Quality Air Sensor")
    time.sleep(0.5)
    print("Measuring...")

    with LinuxI2cTransceiver('/dev/i2c-1') as i2c_transceiver:
        device = Sen5xI2cDevice(I2cConnection(i2c_transceiver))
        # Perform a device reset (reboot firmware)
        device.device_reset()
        # Start measurement
        device.start_measurement()
           
    while True:
        with LinuxI2cTransceiver('/dev/i2c-1') as i2c_transceiver:
            device = Sen5xI2cDevice(I2cConnection(i2c_transceiver))
            values = device.read_measured_values()
        
        #sensirion()
        # Class Mic instance
        mic = Mic()
  
        #Leer y mostrar el resultado
        noise = mic.read()
        # Close Audio secuence
        mic.close()  
        
        # Wait until next result is available
        time.sleep(5)

        # Current time
        now = datetime.now()

        # parsing into ISO 8601 format
        iso8601_format = now.isoformat()


        # Create a diccionary, data
        data = {} 

        # feed values into data
        data['device'] = device_Id
        data['time'] = iso8601_format 
        data['pm10'] = float(values.mass_concentration_10p0.physical)
        data['pm2_5'] = values.mass_concentration_2p5.physical
        data['pm1'] = values.mass_concentration_1p0.physical
        data['pm4'] = values.mass_concentration_4p0.physical
        data['lux'] = lux()
        data['temp'] = round(float(values.ambient_temperature.degrees_celsius),2)
        data['hum'] = values.ambient_humidity.percent_rh
        data['pres'] = read_hPa(initialize_sensor())
        data['alt'] = calculate_altitude(read_hPa(initialize_sensor()))
        data['co2'] = CO2()
        data['noise'] = noise
        #data['VOC_Index'] = values.voc_index.scaled
        #data['NOx_Index'] = values.nox_index.scaled

        #data_copy = data.copy()
        counter = 0
        
        for clave, valor in data.items():                    
           if isinstance(valor, float):                 
                 if math.isnan(valor):
                      print(f"The key '{clave}' has a value type: {valor}")
                      counter += 1 
                      break

       
        print (counter)
        print (data)               
        if counter == 0:
           print ("Posting data")
           collection.insert_one(data)


if __name__ == "__main__":
    thread = threading.Thread(target=BreathingLed)
    thread.start()
    main()