O código usado no exercicio foi o [linux_userspace.c](./examples/linux_userspace.c)
o arquivo com as medias é gerado na pasta examples e tem o nome de medias.csv .

# Como executar

entre na pasta examples e digite:
	
	make raspbian
	make run

caso o i2c não se localize no /dev/i2c-1 , no lugar do 'make run' digite:

	./bme280 local_do_i2c

para excluir o execultável e o medias.csv digite

	make clean
