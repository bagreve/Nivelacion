# slice con masks
import numpy as np 

a = np.arange(36) 
a = a.reshape(6,6)
print a,"\n"


beta = a[[0,1,2,3,4],[1,2,3,4,5]]
print beta,"\n"

alpha = a[3:,[0,2,5]]
print alpha,"\n"

mask = np.array([1,0,1,0,0,1],dtype=bool)
print mask

# para generar un copy:
# si los tomo como slice quedan ligados a la variable original
# si se toman directo se hace un copy

a = np.array([10,1,20])
subset = a[[0,2]]				# toma el primer y ultimo elemento en este caso
								# para poder generar otro arreglo
print a.flags.owndata
print subset.flags.owndata
print a is subset

subset[0] = -1
print subset, "\n"
print a, "\n"

a = np.arange(25) 
a = a.reshape(5,5)

print a[ a%3==0 ]				# para generar un booleano tengo que igualarlo a 0

output = np.empty_like(a, dtype="float")
print output

output1 = output.fill(np.nan)
print output1
mask = a % 3 == 0					# creo el mask para saber las posiciones de true 
output[mask] = a[mask]    			# tomo las posiciones y reemplazo los nans con los valores de a
print output

print np.where(a%3 == 0,a ,np.nan)  # toma el booleano si es verdadero toma el elemento de a y si es falso toma nan


