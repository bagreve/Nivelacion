# En esta nivelacion se estudia el uso de otro tipo de loop llamado while y sus ventajas y desventajas
# en comparacion a el for loop.

total = 0										# En este primer ejemplo realiza un for para recordar  
for i in range(1,5):							# como se usaba de forma simple con un range
	total += i									# crea una variable total y al ir cambiando el i dentro 
print "ej 1:",total								# de el loop for va sumando el numero natural i 
												# del ciclo for. 
total2 = 0										# En el caso 2 se hace lo mismo que en el ejemplo 1
j = 1											# pero con un loop de while creando una variable extra
while j < 5:									# j, con el fin de terminar la funcion al ser igual a 5.
	total2 += j							
	j += 1							
print "ej 2:",total2							
							
given_list = [5,4,4,3,1,-2,-3,-5]				# En el tercer ejemplo se crea una lista de 8 elementos para 
total3 = 0										# sumarlos con el loop while en la variable llamada total3
i = 0							 				# dentro del while se especifican 2 condiciones que se deben cumplir
while i < len(given_list) and given_list[i] > 0:# la primera es que el contador i debe ser mas pequeno que el largo de  
	total3 += given_list[i]						# de la lista para que no genere un error en la fila de codigo 20, ya que 
	i += 1										# si no se pone esta condicion el while no se detiene y busca un elemento 
print "ej 3:",total3							# mas grande que la propia lista. La segunda condicion especifica que  
												# se quieren sumar solo los numeros naturales.
given_list2 = [5,4,4,3,1,-2,-3,-5]				# En el ejemplo 4 se hace lo mismo que en el ejemplo 3 pero con un for
total4 = 0										
for element in given_list2:							
	if element <= 0:							
		break								
	total4 += element							
print "ej 4:",total4							
							
total5 = 0										# El ejemplo 5 se sigue haciendo el mismo ejercicio, pero en en este caso
i = 0											# el while tiene condicion True, es decir, siempre corre, es por eso que 
while True :									# se necesita poner una condicion con break para detener el loop, al igual
	total5 += given_list2[i]					# que se hizo en el ejemplo 4
	i += 1							
	if given_list2[i] <= 0:							
		break
print "ej 5:",total5





















