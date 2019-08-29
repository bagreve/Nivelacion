import numpy as np 
a = np.arange(25)
a = a.reshape(5,5)
print a

red = a[:,1::2]
print red,"\n"
yellow = a[4,:]
print yellow,"\n"
blue = a[1::2,:-2:2]
print blue,"\n"					# En este caso hay que tener cuidado, porque si le hago un cambio a red
red[-1,-1] = 0					# le hago un cambio a "a", siguen ligados, si quiero cambiarlo tengo que hacer
print a 						# un .copy() es util pero lo hace mas lento.




