# esta programa utiliza algunos elementos basicos para al comprension de las listas
# entre algunas funciones que se podria utilizar esta el .append y el .pop que agrega y quita
# el ultimo elemento de la lista respectivamente.

b= ["banana", "apple", "kiwi"]                            # Se plantea una lista de frutas
print "b:", b                     						  # esta se imprime
#metodo 1:
temp = b[0]												  # se crea una variable temporal par apoder realizar el cambio				
b[0] = b[2]												  # se iguala el primer termino a l ultimo
b[2] = temp 										      # el ultimo se iguala a la variable temporal 
														  # con esto se invierte el orden de los elementos
print "Cambiamos el orden de b:" , b 					  
#metodo 2:

b[0],b[2]=b[2],b[0] 									  # este es el segundo metodo que iguala directamente ambas
print "Volvemos a cambiar el orden de b:" , b 			  # posiciones obteniendo mismo resultado.