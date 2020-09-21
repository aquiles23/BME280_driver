raspbian: 
	gcc linux_userspace.c ../bme280.c -I ../ -lwiringPi -o bme280

bsd:
	cc bsd_userspace.c ../bme280.c -I ../ -o bme280

run:
	./bme280 /dev/i2c-1
clean:
	rm -v bme280
