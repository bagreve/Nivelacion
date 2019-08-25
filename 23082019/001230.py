# Este es el ejercicio final del quinto video de nivelacion, que consiste en sumar todos los numeros 
# negativos de la lista, tanto con for como con while.

given_list3 = [7,5,4,4,3,1,-2,-3,-5,-7]		# Se crea la lista
total6 = 0									# se crea la variable total6 para poder ir sumando
i = 0										# y un contador que sea menor que el largo de la lista
while i <= (len(given_list3) - 2):			# menos 2, debido a que no queremos que corra hasta una 
	i += 1									# cantidad superior que elementos en la lista y 
	if given_list3[i] <= 0:					# se pone al condicion que solo los menore a 0 se sumen
		total6 += given_list3[i]
print "ej 6:",total6

total7 = 0									# se crea otra variable total7 para sumar los numeros,
for i in range(0,len(given_list3)):			# con el loop for se crea una lista del 0 a la cantidad
	if given_list3[i] <= 0:					# de elentos de la lista menos 1, quedando perfecto para 
		total7 += given_list3[i]			# la condicion del if y que no tire error.
print "ej 7:",total7						# dentro del if se condiciona que solo los numeros negativos 
											# se sumen.
