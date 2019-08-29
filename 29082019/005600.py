# uso de mascaras
import numpy as np 

a = np.array([3,-1,-2, 4,-6,8])
print a
print a < 0					# mask es un array de True y False
negatives = a < 0
print a[negatives]			# que se puede usar como variables
print a[a<0]

a[a < 0] =0					# al usarse como variable se puede operar con el arreglo 
print a

print (a<8).any()

print (a>3) & (a<8) 

print a[(a>3) & (a<8)]

positions = np.nonzero(negatives)
print positions							# imprime las posiciones de True

a = np.array([10,1,20])
b = np.array([2,3,20])
print a>b
