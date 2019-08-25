# En este tutorial se ensena como se usa u la utilidad que tiene la libreria numpy
# 
import numpy as np 											# se llama a la libreria numpy para array
from scipy.misc import imread, imsave, imresize				# se llama a la libreria scipy para trabajar con fotos
import matplotlib.pyplot as plt 							# se llama a la libreria matplotlib para mostrar las fotos 

a = np. zeros(3)											# se crea un vector array de dimension 3 con 0 
print type(a)												# se imprime para ver que tipo de codigo es el vector
print type(a[0])											# se ve que tipo de codigo es cada elemento del array

z = np.zeros(10)											# se crea un vector de dimension 10 con 0
print z 													# se imprime el array
print z.shape 												# se imprime para ver las dimensiones que tiene
z = np.ones(10)												# se crea un array de dimension 10 con 1
print z 										
z = np.empty(3) 											# se crea un array vacio de dimension 3 
print z 												
z = np.linspace(2,10,5)										# linspace crea un array con 5 elementos del 2 al 10
print z

a_list = range(1,10) 										# se crea una lista del 1 al 10 
w = np.array(a_list)										# y se transforma a un array
print w						

b_list = [[9,8,7,6,5,4,3,2,1],[1,2,3,4,5,6,7,8,9]] 			# se crea una lista de listas
v = np.array(b_list) 										# se transforma a array
print v 													# y se puede ver que es sencillo cambiar cualquier tipo de lista
print v.shape        										# a array, y en esta fila se ve la forma que tiene

np.random.seed(0) 											# se crea la semilla para el random
z1 = np.random.randint(10, size=6)							# z1 son 6 numeros random del 1 al 10 con semilla 0
print z1 						
print z1[0]													# se imprime solo el primer elemento del array z1
print z1[0:2]												# se imprimen los priemros dos elementos del array
print z1[-1]												# se imprime solo el ultimo elemento del array

