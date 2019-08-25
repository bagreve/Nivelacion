import numpy as np
from scipy.misc import imread, imsave, imresize
import matplotlib.pyplot as plt

img = imread('skimage/ardilla.jpg')    				# se lee a la foto de la carpeta skimage
print (img.dtype,img.shape)							# se imprimen las caracteristicas de la foto como el tipo y dimensiones
plt.imshow(img)										# se llama a la foto
plt.show()											# y se imprime
plt.imshow(img[::-1])								# con el -1 se invierte el eje y invirtiendo la imagen
plt.show()
plt.imshow(img[:,::-1]) 							# se invierte el eje x, invirtiendo la imagen
plt.show()
plt.imshow(img[150:250, 250:400])					# se toman solo puntos especificos para hacer zoom en la cabeza de la 
plt.show() 											# ardilla
plt.imshow(img[::2,::2]) 							# se achican los ejes a la mitad
plt.show()
img_sin = np.sin(img)								# se imprime la matriz de la imagen con el fin de estudiarla con
print img_sin										# con diferentes funciones
print np.sum(img)									# suma del array
print np.prod(img)									# el producto
print np.mean(img)									# 
print np.std(img)									# desviacion estandar
print np.var(img)									# varianza
print np.min(img)									# minimo
print np.max(img)									# maximo
print np.argmin(img)								# el indice del minimo
print np.argmax(img)								# indice del maximo