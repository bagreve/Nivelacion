# roles
# rol1: Las dimensiones deben calzar
import numpy as np

a = np.arange(25) 
a = a.reshape(5,5)

b = np.array([2,3,20])

#print a+b, no calzan

# rol2: 
#todos los operadores matematico se aplican elemento por elemento 
#rol3:
# todos los operadores de reduccion se aplican a todo el arreglo a no ser ue se epecifique
# rule4:
# nan son importante, usalos con cuidado. los valores que faltan se propagan a no ser que se explicite

nan = np.nan+6
print nan
nan1= np.nansum([1,np.nan,9])
print nan1
print  a
mask = np.where(a%3 == 0,a ,np.nan)
print a[a%3==0].sum()

# ej de rol 2:
a = np.array([1,2,3])
print np.sum(a)        # metodo




a = np.arange(24).reshape(6,4)
print a.mean(axis=0).shape
print a.mean(axis=1).shape
channel_means = a.mean(axis=1)


# para terminar el video usa un data que no entrega, llamado 'Wind' 













