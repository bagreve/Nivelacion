
# este ultimo video de la nivelacion consiste en una breve introduccion sobre matplotlib y sus usos
from matplotlib import pyplot as plt 								# de la libreria se importa a pyplot

#print (plt.style.available)										# esta linea ayuda a saber los estilos disponibles
plt.style.use('fivethirtyeight')									# existen distintos estilos de grafico, este es uno de los
																	# disponibles
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35] 				# del Github del profesor del video se obtienen datos como edad

py_dev_y = [45372, 48876, 53850, 57287, 63016,						# por cada edad tienen un promedio de pago
            65998, 70003, 70000, 71496, 75370, 83640]
plt.plot(ages_x, py_dev_y, color = '#5a7d9a', linewidth = 3, label = 'Python')		# este codigo dice que va a graficar y con que
																					# caracteristicas, como color, ancho de linea y etiqueta
js_dev_y = [37810, 43515, 46823, 49293, 53437,									
            56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(ages_x, js_dev_y, color = '#adad3b', linewidth = 3, label = 'javaScript')

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
plt.plot(ages_x, dev_y, color = '#444444', linestyle = '--', label = 'All Devs')

plt.xlabel('Ages')													# esta es la etiqueta de los ejes, en este caso el eje x
plt.ylabel('Median Salary (USD)')									# etiqueta del eje y
plt.title('midian Salary (USD) by Age')								# y el titulo del grafico a mostrar

plt.legend()														# se necesita este codigo para que plotee de form corecta

plt.grid(True)														# se le pide que imprima cuadriculado

plt.tight_layout()													# hace el orden de las etiquetas y que calcen bien

plt.show()															# imprime

