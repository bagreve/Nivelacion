import numpy as np
from scipy.misc import imread, imsave, imresize
import matplotlib.pyplot as plt

a_array = np.array([1,2,3,4,5])    							# se crea un array de dimension 5 con numeros del 1 al 5
b_array = np.array([6,7,8,9,10])							# de igual forma se crea otro arreglo del 6 al 10 
c_array = a_array + b_array									# se suman los arreglos, sumandose los elementos concidentes
d_array = a_array + 30										# se suma el array mas 30 sumandose cada elemento con 30
e_array = a_array * b_array									# al igual q sumando se multiplica cada elemento
f_array = a_array * 10										# y se multiplica como se suma con 30

total = 0													# dentro del video se usa el simbolo @, pero esta usando jupyter 
for i in range(0,len(e_array)):								# notebook es pore so que para lograr lo mismo fue necesario crear
	total += e_array[i]										# un loop for para sumar la multiplicacion

#g_aaray = a_array  b_array
print c_array,"\n", d_array,"\n", e_array, "\n", f_array	# esta linea fue la de impresion de todo lo anterior
print total

photo = imread('skimage/ardilla.jpg')						# se llama a la foto ardilla
plt.imshow(photo[:,:,0].T)									# y se usa la funcion de transposicion .T
plt.show()

x = np.array([2,1,4,3,5])									# se crea un arreglo del 1 al 5 en desorden
y = np.sort(x)												# con la funcion sort se ordenan los elementos del areglo x
print y										