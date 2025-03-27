# Complete project details at https://RandomNerdTutorials.com/micropython-bme680-esp32-esp8266/

from machine import Pin, I2C
from time import sleep
from bme680 import *

# ESP32 - Pin assignment
i2c = I2C(scl=Pin(7), sda=Pin(6))
# ESP8266 - Pin assignment
#i2c = I2C(scl=Pin(5), sda=Pin(4))

bme = BME680_I2C(i2c=i2c)
initialtime= time.ticks_ms()

while True:
    
    currenttime= time.ticks_ms() #Every time it passes here, gets the current time
    if time.ticks_diff(time.ticks_ms(), initialtime) > 5000: # this IF will be true every 3000 ms
        initialtime= time.ticks_ms() #update with the "current" time
                
        try:
            temp = str(round(bme.temperature, 2)) + ' C'
            #temp = (bme.temperature) * (9/5) + 32
            #temp = str(round(temp, 2)) + 'F'
            
            hum = str(round(bme.humidity, 2)) + ' %'
            
            pres = str(round(bme.pressure, 2)) + ' hPa'
            
            gas = str(round(bme.gas/1000, 2)) + ' KOhms'

            print('Temperature:', temp)
            print('Humidity:', hum)
            print('Pressure:', pres)
            print('Gas:', gas)
            print('-------')
        except OSError as e:
            print('Failed to read sensor.')
 
  