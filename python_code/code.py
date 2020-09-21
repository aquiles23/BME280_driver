import smbus2
import bme280
from  lcd_16x2_i2c import RPi_I2C_driver
from time import *

porta_i2c = 1
endereco = 0x76

bus = smbus2.SMBus(porta_i2c)
calibracao_paramentros = bme280.load_calibration_params(bus, endereco)
mylcd = RPi_I2C_driver.lcd()

# timer = 0

while True:
	dado = bme280.sample(bus, endereco, calibracao_paramentros)
	temp = round(dado.temperature,2)
	hum = round(dado.humidity,2)
	press = round(dado.pressure,2)

	mylcd.lcd_clear()
	mylcd.lcd_display_string(f"aquiles T:{temp}", 1)
	mylcd.lcd_display_string(f"U:{hum} P:{press}",2)
	sleep(1)
	# timer +=1
'''
print("ID: " + str(dado.id))
print("Data/Hora: " + str(dado.timestamp))
print("Temperatura: " + str(dado.temperature))
print("Umidade: " + str(dado.humidity))
print("Pressão atmosférica: " + str(dado.pressure))

#sleep(1)
mylcd.lcd_clear()
'''
