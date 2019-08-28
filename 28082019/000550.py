import numpy as np

a = np.array([2,3,4])			# crea un array con tres elementos de una lista
print a
a = np.arange(2,13,2)			# cra un arreglo que inicia con el dos y va de dos en dos hasta alcanzar (13-1)
print a
a = np.linspace(2,12,6)			# crea un array con seis elementos iniciando del 2 hasta el 12
print a
a = a.reshape(3,2)				# reorganiza al array a con el fin de cambiarlo a un arreglo de arreglos 3X2
print a

print "Cuantos elementos tiene:",a.size,"\n","La forma que tiene:", a.shape
print  "El tipo de codigoes:",a.dtype
print "El tamano en bytes:", a.itemsize

b = np.array([(1.5,2.,3),(4,5,6)])	# crea una matriz array de 3X3
print b 							# 

print a < 4, "\n"					# imprime True si el elemento de la matriz es menor a 4
print a * 3, "\n"					# multiplica toda la matriz por tres, esto es muy conveniente en comparacion con una lista de listas 
print a, "\n"						# por que no es necesario crear un for para recorrer todos los elementos 
a *= 3								# Al igual que para modificar completamente al arreglo solo se opera con el arreglo.
print a, "\n"

a = np.zeros((3,4))					# se crea un matriz de arreglos llenos con ceros
print a
print a.dtype						# esto ayuda a saber que tipo de elemento tiene el arreglo int, float, booleano y cuantos bytes

a = np.ones((2,3))					# crea una matriz de 2X3 de array con unos
print a

a = np.ones(10)						# es un vector de 10 elementos con unos
print a

a = np.array([2,3,4], dtype = np.int16) # se crea un arreglo pero se obliga el tipo de elemento ue posee en un int16
print a,a.dtype							# se chequea el tipo 
print a.itemsize						# se chequea el tamano del item

a = np.random.random((2,3))				# con numpy tambien se puede crear elementosaleatorios en 
print a 								# este caso dentro de una matris de 2x3 y numeros random del 0 al 1

a = np.random.randint(0,10,5)			# se puede hacer un vector de cinco elementos , del 0 al 10
print a
print a.sum()							# obtener su suma
print a.min()							# en menor elemento
print a.max()							# el maximo elemento
print a.mean()							# el promedio
print a.var()							# varianza
print a.std()							# desviacion estandar

a = np.random.randint(1,10,6)			# se hace el vector
print a
a = a.reshape(3,2)						# y se reorganiza para crear una matriz 2x3
print a

print a.sum(axis=1)						# para sumar los horizontales
print a.sum(axis=0)						# para sumar los verticales

