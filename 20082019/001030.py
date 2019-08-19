# En la nivelacion 2 se aprende como crear y usar funciones con el fin de simplificar y ordenar el programa.

name1 = "Yk"        # Se crean los datos los cuales la funcion utiliza.
height_m1 = 1.7
weight_kg1 = 55

name2 = "Sister"
height_m2 = 1.64
weight_kg2 = 49

name3 = "Brother"
height_m3 = 1.7
weight_kg3 = 70

def bmi_calculator(name, height_m, weight_kg):   # la funcion se llama bmi_calculator y necesita 3 variables
	bmi = weight_kg / (height_m)**2              # un nombre, la altura y el peso 
	print "bmi:", bmi               
	if bmi > 30:					             # obesidad con bmi sobre 30
		return name , "is obese"

	elif bmi > 25:					             # sobre peso con bmi entre 30 y 25
		return name ,"is overweight"

	elif bmi > 18.5:				             # normal con bmi entre 25 y 18.5
		return name ,"is normal weight"

	else:							             # bajo peso con bmi bajo los 18.5
		return name ,"is underweight"

resultado1 = bmi_calculator(name1, height_m1, weight_kg1)          # Con esta linea se crean 3 nuevas variables que son los 
resultado2 = bmi_calculator(name2, height_m2, weight_kg2)          # resultados de la funcion bmi_calculator (gracias al return) 
resultado3 = bmi_calculator(name3, height_m3, weight_kg3)          # con los datos creados de Yk, Sister y Brother, al hacer correr 
																   # este, solo se imprime el ibm de cada uno, ya que la funcion esta 
																   # hecha de ese modo.	
print resultado1												   # Luego en este print se imprimen los resultados definidos por 
print resultado2                                                   # la funcion.
print resultado3

