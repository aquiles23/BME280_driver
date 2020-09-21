O código usado no exercicio foi o [linux_userspace.c](./examples/linux_userspace.c)

# Como executar

entre na pasta examples e digite:
	
	make raspbian
	make run

caso o i2c não se localize no /dev/i2c-1 , no lugar do 'make run' digite:

	./bme280 local_do_i2c
