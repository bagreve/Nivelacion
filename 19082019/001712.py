# En la nivelacion 1 se aprende como utilizar de forma correcta if, elif y else.
# Estos sirven para poder diferenciar o discriminar el resultado o dato que se necesite

name = "YK"					# Estas 3 lineas de codigo son los datos o parametros que el programa necesita  
height_m = 1.7				# para ejecutarse y obtener el bmi: nombre, altura y peso
weight_kg = 55

bmi= weight_kg / (height_m)**2   # formula de bmi 
								 #	Existen 4 estados comunes de bmi:
print "bmi:", bmi               
if bmi > 30:					 # obesidad con bmi sobre 30
	print " YK is obese"

elif bmi > 25:					 # sobre peso con bmi entre 30 y 25
	print "YK is overweight"

elif bmi > 18.5:				 # normal con bmi entre 25 y 18.5
	print "YK is normal weight"

else:							 # bajo peso con bmi bajo los 18.5
	print " YK is underweight"

# Este codigo esta en este orden de mayor a menor bmi, debido a que de esa forma el programa entiende que si no entra a un estado
# entra al siguiente, pero si ya entra a uno no necesita entrar al siguiente elif o al ultimo else ya que ya entro a un estado
# anterior.