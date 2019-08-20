# La actividad final trata sobre encontrar la suma de todos los numeros multiplos de 3 y 5
# y que la suma sea menos que 100

lista3 = []							# Se crean dos listas vacias para llenarlas con los multiplos 
lista5 = []							# de 3 y 5
sumatotal = 0						# Se crea un contador para revisar que la restriccion de bajo 100 se cumpla,
for i in range(1,1000):				# con un for range se crea una lista de tamano x, con el fin de recorrer 
	if sumatotal + i < 100:			# todos los numeros naturales. Luego se pone la restriccion que la sumatotal
		if i % 3 == 0:				# mas el elemento que se esta corriendo de la lista sea menor que 100 para 
			lista3.append(i)		# no tener que pasar por todos los numeros de la lista.
			sumatotal += i 			# Se chequea que el elemento i sea multiplo de 3 o 5 y se agrega al final de la  
		elif i % 5 == 0:			# lista mientras se suma a la suma total
			lista5.append(i)
			sumatotal += i

	elif sumatotal > 100:			# Si sumatotal es mayor que 100, el for sufre un quiebre y se detiene. 
		break

print lista3						# Se imprime la lista 3
print lista5						# Se imprime la lista 4
print sumatotal						# Se imprime la sumatotal	


