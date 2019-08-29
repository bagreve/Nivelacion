# Esta nivelacion consiste en una introduccion a como y porque se usa numpy para principiantes
# Este video es mas completo que el anterior
import numpy as np 

a = [1,2,3,4]							# se crean dos lista de 4 elementos 
b = [10,11,12,13]						
print a + b								# si quiero sumarlas no las puedo sumar directamente
										# si lo hago, se concatenan
suma = []
for item1,item2 in zip(a,b):			# para hacerlo hay que hacer un for y sumarlos
	suma.append(item1+item2)
print suma

g =list(range(1000000))					# una diferencia importante a considerar, es el tiempo de proceso 
#print %timeit sum(g)					# que tarda en un loop de lista, en este caso tarda:7.13ms per loop


g_array = np.array(g)					# a diferencia de los arreglos que tardan en hacer lo mismo 
#print %timeit np.sum(g_array)			# 414 us por loop
# esto pasa porque numpy mete todos los elementos en una sola "pieza" a diferencia de las listas que cada elemento
# tiene su propia pieza, esto le da la libertad de poder ser de otro tipo de elementos a diferencia de un arreglo
# que todos los elementos son del mismo tipo, lo que hace que sea mas rapido ya que el programa no tine que chequear 
# que tipo de elemento es.

a = np.array([1,2,3,4])
b = np.array([10,11,12,13])
print a,b
print a+b
print a*b
print a.ndim
print a.shape         					# el shape es una tupla es decir con coma


print np.sin(a)
# El problema que tiene numpy es que es poco flexible:
a = np.array([1,2,3,4])					# si todos los elementos son int, al array sera int y todo lo que se agrege
print a.dtype							# se transformara en int							
a = np.array([1,2,3,4.0])				# si un elemento es un float todo el arreglo se transforma en float
print a.dtype
a = np.array([1,2,3,4.0+1j])			# al igual que si un elemento es un complejo, todo el arreglo es complejo
print a.dtype
# a no ser que oblige que tipo de elemento quiero
a = np.array([1,2,3,4], dtype=float)
print a,"\n"

c = np.array([[10,11,12],[20,21,22]]) 
print c
print c.dtype
print c.ndim
print c.shape
print c.size
print c.nbytes

# tener ojo porque que sean vectores no quiere decir que se comportan como tales, se ven como tales, pero en verdad no tienen dimensiones como matriz
# no se pueden transponer por ejemlo (solo vectores, matrices como tal funcionan bien)

print c[0,0]
print c[0]					# primera fila
print c[1]					# segunda fila
# asi funciona en 1D
print a[1:3]				# va desde el elemento uno al tres pero el tres no o comnsidera
print a[-2:3]				# el negativo hace que retroceda dentro del arreglo
print a[:3]					# parte desde el 0 hasta el tres, sin tomar el tres
print a[-2:]				# parte desde el menos dos hasta el final de la lista
print a[::2]				# considera todo el vector  y va de dos en dos
# asi en 2D
print c[0,1:2]				# se toma la fila 0 y el elemento uno
print c[1:,1:]				# se toma el primer elemento hacia adelante  
print c[:,1]				# todos los de la primera columna hasta
print c[1::,::1]			
# una ventaja importante de llamar de esta forma a elementos es que se mantiene la forma o dimencion que tiene si 
# se llamara directamente como: c[i] lo saca como int y no como array
