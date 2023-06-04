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






