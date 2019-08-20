# Introduccion en los for loops, en este capitulo de nivelacion
# se ensena a como usar for con el fin de simplificar el codigo
# y no hacerlo repetitivo si se necesitara por ejemplo nombra 
# cada elemento de una lista de 100 componentes, para esto simplememnte 
# se usa la funcion for

# ejemplo 1:
a = ["banana", "apple","kiwi"] 				# se imprime dos veces los elementos de la lista

for element in a:
	print element
	print element
print ""

# ejemplo 2:								# se imprime la suma de la lista b gracias a un contador
b = [20, 10, 5] 
total = 0
for e in b:
	total += e
print total
print ""

# ejemplo 3:								# se crea una lista a base de un range, del 1 al 4
c = range(1,5)
print c
print ""

# ejemplo 4:								# se suman los elementos de la lista creada por range
total2 = 0									# y un contador los va sumando
for i in range(1,5):
	total2 += i
print total2
print ""

# ejemplo 5:								# se suman los elementos multiplos de 3 de la lista  
total3 = 0									# creada por range y un contador los va sumando
for i in range(1,8):
	if i % 3 == 0:
		total3 += i 
print total3
