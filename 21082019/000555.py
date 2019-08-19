b= ["banana", "apple", "kiwi"]                            # Se plantea una lista de frutas
print "b:", b                     						  # esta se imprime
#metodo 1:
temp = b[0]												  # se crea una variable temporal par apoder realizar el cambio				
b[0] = b[2]
b[2] = temp

print "Cambiamos el orden de b:" , b
#metodo 2:

b[0],b[2]=b[2],b[0]
print "Volvemos a cambiar el orden de b:" , b