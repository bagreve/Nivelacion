# En la nivelacion numero 6,se ensana como usar y crear diccionarios

d = {}							# Se crea un diccionario vacio
d["George"] = 24				# se crean nuevos valores ligados a llaves , siendo George la llave y su edad el valor
d["Tom"] = 32					
d["Jenny"] = 20					
d[10] = 100						# no solo se pueden crear listas con llaves de strings y valores numericos, se pueden  
print d["George"]				# crear todas las combinaciones
print d[10]						# para imprimir un valor solo se llama al diccionario con la llave
for key, value in d.items():    # en este caso se quiere imprimir tanto las llaves como los valores en orden
	print "key:", key			# es por eso que se busca en internet y se encuentra el for aqui utilizado
	print "value:", value		# para imprimir lo deseado.
	print "" 
