import numpy as np
# En el octavo video de nivelacion se ensena sobre las ventajas de la libreria numpy por sobre el uso de listas 
my_list =[1,2,3,4,5,6,7,8,9]
my_array = np.array(my_list)
# Con el uso de numpy no es necesario correr la lista para operar con ella, logrnadose solo con una linea de codigo:
for i in range(len(my_list)):			# lista
	my_list[i] *= 3

my_array *= 3							# array
print my_array

# el uso de array hace que el programa sea mas rapido, porque todos los elementos son float y no necesita ir chequeando uno por uno
# para asegurarse que al operar sean del mismo tipo de elemento.
# el numpy array usa menos memoria, porque las listas nesecitan un pointer data que los lleve al data, a diferencia de los array ,
# que se asignan a un data directamente usando el mismo bloque de memoria

# Sobre los arreglos se pueden aplicar diferentes funciones como type, size, shape, data

# otro punto importante son la cantidad y tipo de desimales o numeros que se quieren , bool_(booleano)
# int8, int16, int32, int64 para der un rango de numeros a usar
# uint8, uint16, uint32, uint64 desde el 0 hasta el numero positivo que corresponda de cada byte
# float8, float16, float32, float64, por defecto python usa el 64, pero se se tiene un array muy grande
# donde no se necesita tanta precicion en los calculos y se quiere que corra mas rrapido, se cambia a 32 o
# incluso a 8 dependiendo de lo que se quiera.
#complex64, complex128 para numeros imaginarios.





