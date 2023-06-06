# Air Quality Measurement
Metroploia University of Applied Sciences, Finland

# Innovation Project Based On International Sensor Development Project 2022-2023
Hochschule Osnabr√ºck University of Applied Sciences, Germany & Metropolia University of Applied Sciences, Finland

This bundle contains three folders, in orde to keep the same structure as ISD22. https://github.com/fkah98/isd22

# WiFi connection
### Raspberry pi configuration
`execute sudo raspi-config and indtroduce the SSID and password`<br />
or <br />
`Over ethernet connection through SSH add the SSID in etc/wpa_supplicant/wpa_supplicant.conf add the need` 

network={
	ssid="<SSID>"
	psk="<Password>"
}

# Device Id and Name
### generate_name()
`On the first start up a new Id and Name will be generated automatically, both values will be displayed on console and added to the data base.
If a new name or Id is needed the files id.text and name.txt must be deleted before re-launch the driver.

# Id Generating in file id.txt
### 
`execute deviceId.py`<br />
or <br />
`sudo python main.py` inside the device/sensor will generate the id automatically

# Name Generating in file name.txt
### 
`execute deviceName.py`<br />
or <br />
`sudo python main.py` inside the device/sensor will generate the name automatically.


#Dicctionary
### Value names and units
- `alt`: Altitdue above mean sea level in m
- `co2`: Carbon dioxide in ppm
- `hum`: Humidity in %RH
- `lux`: Lighting in lux
- `noise`:Loudness in dB
- `pm10`: Particel density of particulate Matter(PM) in size range 0.3µm to 10.0µm in µg/m3
- `pm2_5`: Particel density of particulate Matter(PM) in size range 0.3µm to 2.5µm in µg/m3
- `pm1`: Particel density of particulate Matter(PM) in size range 0.3µm to 1.0µm in µg/m3
- `pm4`: Particel density of particulate Matter(PM) in size range 0.3µm to 4.0µm in µg/m3
- `pres`: Pressure in hPa
- `temp`: Temperature in ∞C
 
### Data{}

# Establishing MongoDB Connection
### MongoDb Atlas

`client = MongoClient("mongodb URI")`
`db = client["innovation"]`
`collection = db["sensordatas"]`
`collection.insert_one(data)`

#Install Service
###install sensor.service
'this allows the script run after a reboot`

#STL files
`part required screws and spacers to be assembled`
	
4x Hex Standoff Threaded M2.5 Brass 1.181" (30.00mm)
<p align="center">
	<img width="150" src="https://github.com/minhson0506/airquality_hardware/assets/73076333/dd4b8dbb-5fd1-42c5-86fa-1fada26d376a">
</p>
2x HEX STANDOFF M3 NYLON 10.5MM
<p align="center">
	<img width="150" src="https://github.com/minhson0506/airquality_hardware/assets/73076333/d19bd7b6-3893-4a3e-9321-bc234bd826d1">
</p>
3x Hex Standoff Threaded M3 Brass 0.197" (5.00mm) Silver
<p align="center">
	<img width="150" src="https://github.com/minhson0506/airquality_hardware/assets/73076333/402080cc-9050-4804-a183-1b9a9e937e24">	
</p>

#Assembly pictures

Review the design file QualityAirSensor.dwf using the app https://www.autodesk.com/products/design-review/overview
<p align="center">
	<img width="350" height="250" src="https://github.com/minhson0506/airquality_hardware/assets/73076333/217a7fc2-a71b-4483-aeb2-6aa1e539e1cf">	
	<img width="250" height="250" src="https://github.com/minhson0506/airquality_hardware/assets/73076333/544fc437-3c83-48b0-a901-8d9ac6b41623">	
	<img width="250" height="250" src="https://github.com/minhson0506/airquality_hardware/assets/73076333/cf7af0b4-9e92-4b58-914b-409721caf33c">	
</p>
<p align="center">
	<img width="1000" alt="Picture 7" src="https://github.com/minhson0506/airquality_hardware/assets/73076333/71ad48a1-6142-411e-a6ca-61c36d4b211e">
</p>



