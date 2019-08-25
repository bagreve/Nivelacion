import numpy as np
from scipy.misc import imread, imsave, imresize
import matplotlib.pyplot as plt

z = np.array([1,2,3,4,5])							# se crea un array del 1 al 5
print z < 3											# y se pide que z sea menor que 3 tirando true or false 
print z > 3											# de igual forma que sea mayor que 3 
photo = imread('skimage/ardilla.jpg') 				# se llama la foto de la ardilla
photo_masked = np.where(photo > 100,255,100)		# en este caso se le crea un filtro cambiando los colores
plt.imshow(photo_masked)							# todos los que sean mayores a 100 se reemplazan por 255 y los que son 
plt.show()											# menores se reemplazan con 0
