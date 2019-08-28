import numpy as np 		

data = np.loadtxt("blocTemperaturaAmbiente.txt",dtype=np.uint8, delimiter =",", skiprows=1) # se pueden llamar archivos txt para luego usarlos
print data

a = np.arange(10)					# se hace un vector del 0 al 9
print a
#a = np.random.shuffle(a)			# deberia alterar el vector haciendole un shuffle aleatoriamente pero tira error
#print a
print np.random.choice(a[9])		# toma aleatoriamente el elemento nueve del vector
#np.random.random_intergers[5,10,2]


