import time
from sensirion_i2c_driver import I2cConnection, LinuxI2cTransceiver
from sensirion_i2c_sen5x import Sen5xI2cDevice

def sensirion():        
       with LinuxI2cTransceiver('/dev/i2c-1') as i2c_transceiver:
            device = Sen5xI2cDevice(I2cConnection(i2c_transceiver))

            # Wait until next result is available
            print("Waiting for new data...")
            while device.read_data_ready() is False:
                time.sleep(0.1)

            #Read measured values -> clears the "data ready" flag
            values = device.read_measured_values()
            print(values)
            mc_4p0 = values.ambient_temperature.degrees_celsius
            print(mc_4p0)

            # Access a specific value separately (see Sen5xMeasuredValues)
            mass_concentration = values.mass_concentration_2p5.physical
            ambient_temperature = values.ambient_temperature.degrees_celsius

            # Read device status
            status = device.read_device_status()
            print("Device Status: {}\n".format(status))

       



