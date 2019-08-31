
from matplotlib import pyplot as plt 

#print (plt.style.available)										# esta linea ayuda a saber los estilos disponibles
#plt.style.use('fivethirtyeight')
plt.xkcd()															# imprime con forma de comic

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35] 

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
plt.plot(ages_x, py_dev_y, label = 'Python')

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(ages_x, js_dev_y, label = 'javaScript')

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
plt.plot(ages_x, dev_y, color = '#444444', linestyle = '--', label = 'All Devs')

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('midian Salary (USD) by Age')

plt.legend()

plt.tight_layout()

#plt.savefig('plot.png')											# este codigo facilita el guardado de fotos

plt.show()

