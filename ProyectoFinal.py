# importar el archivo .csv que se encuentra en la misma carpeta, que contiene los datos

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
#import prettytable as pt
import tkinter as tk
from tkinter import messagebox
from prettytable import PrettyTable
import os
from typing import Any
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Image, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from datetime import date
import researchpy as rp


# Crear un nuevo documento PDF
#tomar el dato de la fecha actual
fecha = date.today()
doc = SimpleDocTemplate("Entregable_{}.pdf".format(fecha), pagesize=letter)

contenido = []

def guardarHeader(text, n):
    estilo = getSampleStyleSheet()
    estilo_parrafo = estilo['Heading{}'.format(n)]
    parrafo = Paragraph(text, estilo_parrafo)
    contenido.append(parrafo)

def guardarTxt(texto):
    estilo = getSampleStyleSheet()
    estilo_parrafo = estilo['Normal']
    parrafo = Paragraph(texto, estilo_parrafo)
    contenido.append(parrafo)

def guardarImg(imagen):
    imagen_Objeto = Image(imagen, 400, 400)
    contenido.append(imagen_Objeto)
    
def guardarDoc(imagen, alto, ancho):
    imagen_Objeto = Image(imagen, width=ancho, height=alto)
    contenido.append(imagen_Objeto)

text = "Proyecto Final - Probabilidad y Estadística Aplicada <br/><br/>"
guardarHeader(text,1)
text = "<br/><br/>"
guardarTxt(text*4)
text = "./documentos/logoUCU.png"
guardarDoc(text, 200, 200)
text = "<br/><br/>"
guardarTxt(text*4)
text = "Grupo: <br/> Estefany Clara, Gonzalo Paz, Juan Pérez y Lucas Cordero <br/><br/>"
guardarTxt(text)
text = "<br/><br/>"
guardarTxt(text*6)

text = "Introducción: <br/>"
guardarHeader(text, 1)
for i in range(1, 9):
    guardarDoc('./documentos/info{}.png'.format(i), 600,500)

text = "Anexo al informe: <br/>"
guardarHeader(text, 2)

ventana = tk.Tk()
ventana.withdraw()
# IMPORTAR EL ARCHIVO .CSV QUE SE ENCUENTRA EN LA MISMA CARPETA, QUE CONTIENE LOS DATOS
names = ['ID', 'anio', 'mes', 'Sexo', 'Edad', 'region', 'PEA', 'Desempleo', 'Salario']
data = pd.read_csv('./ECH_2022_PyE-2023.csv',sep=';', names=names, header=0)
# eliminar los datos cuando los salarios son mayores a 5.000.000 y los que sean igual a 0
data1 = data[data['Salario'] < 6000000]
data1 = data1[data1['Salario'] != 0]
# extraer los datos de la columna Salario en una variable de tipo Array siempre que sean distintos de 0
salarios = data1['Salario']
salarios = salarios.values

print("Proyecto Final - Probabilidad y Estadística Aplicada\n")
print("")
print("Parte A - DESEMPLEADOS")
text = "Parte A - DESEMPLEADOS"
guardarHeader(text, 2)

# a) Calcular la tasa de desempleo para la muestra
# contar la cantidad de desempleados si PEA = 1 y Desempleo = 1
desempleados = data[(data['PEA'] == 1) & (data['Desempleo'] == 1)]
#contar la cantidad de personas desempleados
print("La cantidad de desempleados presentados en la muestra son: {}".format(len(desempleados)))
text = "La cantidad de desempleados presentados en la muestra son: {}".format(len(desempleados))
guardarTxt(text)

tea = len(data['PEA'])
print("La cantidad de personas en la muestra son: {}".format(tea))
text = "La cantidad de personas en la muestra son: {}".format(tea)
guardarTxt(text)
desempleo = len(desempleados) / tea

print("1- a- La taza de desempleo es: ", desempleo)
text = "1- a- La taza de desempleo es: {}".format(desempleo)
guardarTxt(text)

# Agrupar las edades en 4 grupos: 14-17, 18-25, 26-40, 41+
desempleados_14_17 = desempleados[(desempleados['Edad'] >= 14) & (desempleados['Edad'] <= 17)] 
desempleados_14_17 = desempleados_14_17['Edad']
desempleados_18_25 = desempleados[(desempleados['Edad'] >= 18) & (desempleados['Edad'] <= 25)]
desempleados_18_25 = desempleados_18_25['Edad']
desempleados_26_40 = desempleados[(desempleados['Edad'] >= 26) & (desempleados['Edad'] <= 40)]
desempleados_26_40 = desempleados_26_40['Edad']
desempleados_41 = desempleados[(desempleados['Edad'] >= 41)]
desempleados_41 = desempleados_41['Edad']
# Asignar los valores a un arreglo como  Any
desempleadosAr = [desempleados_14_17, desempleados_18_25, desempleados_26_40, desempleados_41]
#print(desempleadosAr)   #cantidad de desepleados por edades. 
print("Parte B - HISTOGRAMA DESEMPLEADOS")
text = "Parte B - HISTOGRAMA DESEMPLEADOS"
guardarHeader(text, 2)
edAr = ['14-17', '18-25', '26-40', '41+']
# b) Histograma de cada muestra
index = 0
for tipo in desempleadosAr:
    sns.histplot(tipo, kde=True)
    plt.ylabel('Frecuencia')
    plt.xlabel('Edades')
    
    plt.title('Histograma de desempleados por edades {}'.format(edAr[index]))
    index += 1
    try:
        plt.savefig('./desempleados/histograma_desempleados_{}.png'.format(len(tipo)))
        imagen = './desempleados/histograma_desempleados_{}.png'.format(len(tipo))
        guardarImg(imagen)
    except:
        os.mkdir('./desempleados')
        plt.savefig('./desempleados/histograma_desempleados_{}.png'.format(len(tipo)))
        imagen = './desempleados/histograma_desempleados_{}.png'.format(len(tipo))
        guardarImg(imagen)
    plt.show()

text = "<br/><br/>"
guardarTxt(text*9)
#Ejercicio parte 2 Salario
#calcular media, mediana y moda del salario
print("Parte 2 - SALARIO")
print("2) a. Elaborar un histograma de la variable salario")
text = "Parte 2 - SALARIO <br/>2) a. Elaborar un histograma de la variable salario"
guardarHeader(text, 2)

try: 
    sns.histplot(salarios, kde=True)
    plt.xlabel('Salario')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de salario')
    plt.savefig('./salario/histograma_salario.png')
    imagen = './salario/histograma_salario.png'
    guardarImg(imagen)
    plt.show()
    text = "<br/><br/>"
    guardarTxt(text*8)
except:
    print("No se pudo generar el histograma de salario")
    text = "No se pudo generar el histograma de salario"
    guardarTxt(text)


# Elaborar Boxplot para toda la muestra
print("2) b. Elaborar un Boxplot para toda la muestra")
text = "2) b. Elaborar un Boxplot para toda la muestra"
guardarTxt(text)
sns.boxplot(salarios)
plt.title('Boxplot de salario')
plt.savefig('./salario/boxplot_salario.png')
imagen = './salario/boxplot_salario.png'
guardarImg(imagen)
plt.show()
text = "<br/><br/>"
guardarTxt(text*8)

# Estudio de Boxplot  

mediana = np.median(salarios)
Q1 = np.quantile(salarios, 0.25)
Q3 = np.quantile(salarios, 0.75)
min_val = np.min(salarios)
max_mal = np.max(salarios)

# Rango intercuartilico
RI = Q3 - Q1
BII = Q1 - (1.5 * RI)
BSI = Q3 + (1.5 * RI)

print("i. Existen valores atípicos en la muestra. Si existen, ¿cuántos son?")
# Calcular la cantidad de valores atípicos
outliers = data[(data['Salario'] < BII) | (data['Salario'] > BSI)]
print("La cantidad de valores atípicos son: {}".format(len(outliers)))
text = "i. Existen valores atípicos en la muestra. Si existen, ¿cuántos son? <br/>La cantidad de valores atípicos son: {}".format(len(outliers))

print("ii. Corrección de valores atípicos")
text = "ii. Corrección de valores atípicos"
guardarTxt(text)

# Corregir los valores atípicos
#data['Salario'] = np.where(data['Salario'] < BII, BII, data['Salario'])
#data['Salario'] = np.where(data['Salario'] > BSI, BSI, data['Salario'])

# Volver a graficar el Boxplot
sns.boxplot(salarios)
plt.title('Boxplot de salario')
plt.savefig('./salario/boxplot_salario_corregido.png')
plt.show()
imagen = './salario/boxplot_salario_corregido.png'
guardarImg(imagen)
text = "<br/><br/>"
guardarTxt(text*8)

# calcular la media y moda de la muestra
media = np.mean(salarios)
moda = stats.mode(salarios)

print("2) c. Media: {}, Mediana: {}, Moda: {}".format(media, mediana, moda))
text = "2) c. Media: {}, Mediana: {}, Moda: {}".format(media, mediana, moda)
guardarTxt(text)

print("Valores de estudio del Boxplot de Salarios")
print("2) d. Q1: {}, Q3: {}, Mínimo: {}, Máximo: {}, RI: {}, BII: {}, BSI: {}".format(mediana, Q1, Q3, min_val, max_mal, RI, BII, BSI))
text = "Valores de estudio del Boxplot de Salarios <br/> 2) d. Q1: {}, Q3: {}, Mínimo: {}, Máximo: {}, RI: {}, BII: {}, BSI: {}".format(mediana, Q1, Q3, min_val, max_mal, RI, BII, BSI)
guardarTxt(text)
text = "<br/><br/>"
guardarTxt(text*6)
# Elaborar Boxplot por genero (masculino y femenino) identificando en el plt el color por genero
print("2) e. i. Elaborar un Boxplot por género (masculino y femenino)")
text = "2) e. i. Elaborar un Boxplot por género (masculino y femenino)"
guardarTxt(text)

sns.boxplot(x=data1['Sexo'], y=data1['Salario'], palette=['blue', 'pink'])
plt.title('Boxplot de salario por género')
plt.xticks(
    ticks=[0, 1],
    labels=['Hombre', 'Mujer']
)
plt.savefig('./salario/boxplot_salario_genero.png')
plt.show()
imagen = './salario/boxplot_salario_genero.png'
guardarImg(imagen)

print("2) e. ii. Elaborar un Boxplot por región")
text = "2) e. ii. Elaborar un Boxplot por región"
guardarTxt(text)

sns.set_palette(['red', 'green', 'blue'])
# Elaborar Boxplot por region
sns.boxplot(x=data1['region'], y=data1['Salario'] , palette=['red', 'green', 'yellow'])
plt.title('Boxplot de salario por región')
plt.xlabel('Región')

plt.xticks(
    ticks=[0, 1, 2],
    labels=['Montevideo', 'Interior < 5k hab', 'Interior > 5k hab']
)
plt.savefig('./salario/boxplot_salario_region.png')
plt.show()
imagen = './salario/boxplot_salario_region.png'
guardarImg(imagen)


# PARTE B)- ESTIMACIÓN 
"""
Se asume que la muestra es representativa del total de la población.
Dado que la población activa de Uruguay es de 1.757.161. (2).
Suponer que el desempleo se distribuye de forma normal.
1) Estimar el desempleo del total de la población
2) Elabora intervalo de confianza con 95% de certeza para la variable desempleo.
"""
text = "<br/><br/>"
guardarTxt(text*9)
text = "PARTE B)- ESTIMACIÓN"
guardarHeader(text,2)
# 1) Estimar el desempleo del total de la población
print("1) Estimar el desempleo del total de la población")
text = "1) Estimar el desempleo del total de la población"
guardarHeader(text,3)


PAUruguay = 1757161
desempleados = data[(data['PEA'] == 1) & (data['Desempleo'] == 1)]
desempleo = len(desempleados)
# contar la cantidad de filas de data en PEA
PAmuestra = len(data[data['PEA'] == 1])
print("La cantidad de desempleados es: {} de un Total muestral de {} personas activas\nEl total de la Población Activa es: {}\nPor lo cual la proporción es del {}%".format(desempleo, PAmuestra, PAUruguay, round((PAmuestra/PAUruguay)*100, 2)))
text = "La cantidad de desempleados es: {} de un Total muestral de {} personas activas<br/>El total de la Población Activa es: {}<br/>Por lo cual la proporción es del {}%".format(desempleo,PAmuestra, PAUruguay, round((PAmuestra/PAUruguay)*100, 2))
desempleadosTotales = int((desempleo/PAmuestra)*PAUruguay)
print("El total estimado de desempleados es: {}".format(desempleadosTotales))
text = "<br/>El total estimado de desempleados es: {}".format(desempleadosTotales)
guardarTxt(text)

# 2) Elabora intervalo de confianza con 95% de certeza para la variable desempleo.
print("2) Elabora intervalo de confianza con 95% de certeza para la variable desempleo.")
text = "2) Elabora intervalo de confianza con 95% de certeza para la variable desempleo."
guardarHeader(text,3)

# guardar una tabla con los datos de la muestra PAmuestra y desempleo
df = pd.DataFrame(data)
PEAColumn = df['PEA']
DesempleoColumn = df['Desempleo']
tuple = list(zip(PEAColumn, DesempleoColumn))
tuple
tabla = pd.DataFrame(tuple, columns=['PEA', 'Desempleo'])
EdadesColumn = df['Edad']
EdadesDesempleo = list(zip(PEAColumn, EdadesColumn))

confianzaDesempleo = stats.t.interval(confidence=0.95, df=len(DesempleoColumn)-1, loc=np.mean(DesempleoColumn), scale=stats.sem(DesempleoColumn))
sns.regplot(x=EdadesColumn.iloc[20:80], y=DesempleoColumn.iloc[20:80], data=tabla, ci=95, color='blue')
plt.title('Intervalo de confianza de 60 muestras de desempleo')
plt.xlabel('Edades')
plt.ylabel('Desempleo')
plt.savefig('./salario/intervalo_confianza_desempleo.png')
plt.show()
imagen = './salario/intervalo_confianza_desempleo.png'
guardarImg(imagen)

print("El intervalo de confianza para la variable Desempleo es: {}".format(confianzaDesempleo))
text = "El intervalo de confianza para la variable Desempleo es: {}".format(confianzaDesempleo)
print("La muestra arroja que existe un intervalo de certeza del 95% que el desempleo es correcto según la muestra.")
text += "<br/>La muestra arroja que existe un intervalo de certeza del 95% que el desempleo es correcto según la muestra."
guardarTxt(text)
text = "<br/><br/>"
guardarTxt(text*2)

print("C) PRUEBA DE HIÓTESIS \n1) DESEMPLEO:")
text = "C) PRUEBA DE HIÓTESIS <br/>1) DESEMPLEO:"
guardarHeader(text,2)

print("Se pide verificar si es correcto decir que la tasa de desempleo aumento desde 2021.")
text = "Se pide verificar si es correcto decir que la tasa de desempleo aumento desde 2021."
guardarTxt(text)

# Calculo de hipotesis de una cola.
t_static, p_value = stats.ttest_1samp(DesempleoColumn, popmean=0.05)
print("t_static: ",t_static)
print("p_value: " ,p_value)
text = "t_static: {}<br/>p_value: {}".format(t_static, p_value)

nivel_significancia = 0.05
margen_error = 0.0001 * nivel_significancia
#se añade un margen de error al p value para saver si es considerable o no, ya que evidentemente nunca  va a dar exactamente igual al nivel de significancia
# notese que el margen de error es del 0.01% del nivel de significancia (0.05) osea 0.0005 que equivale en porcentaje a 0.05%
if (abs(p_value - nivel_significancia) < margen_error):
    print ("Se rechaza la hipótesis nula." )
    text += "<br/>Se rechaza la hipótesis nula."
else:
    print ("No se rechaza la hipótesis nula." )
    text += "<br/>No se rechaza la hipótesis nula."
guardarTxt(text)

# como preguntar si un valor es igual al otro pero con margen de error de 5%


print("2) SALARIO:")
text = "2) SALARIO:"
guardarHeader(text,2)

print("Se pide examinar la muestra con certeza de 99%, para verificar si el salario promedio entre los hombres y las mujeres es el mismo.")
text = "Se pide examinar la muestra con certeza de 99%, para verificar si el salario promedio entre los hombres y las mujeres es el mismo."
guardarTxt(text)

# Calculo de hipotesis de dos colas.
SalarioHombres = data[data['Sexo'] == 1]
print("la cantidad de salarios hombres es: ",len(SalarioHombres))
SalarioMujeres = data[data['Sexo'] == 2]
print("la cantidad de salarios mujeres es: ",len(SalarioHombres))

t_static, p_value = stats.ttest_ind(SalarioHombres['Salario'], SalarioMujeres['Salario'])
print("t_static: ",t_static)
print("p_value: " ,p_value)
SalarioHombres = SalarioHombres[SalarioHombres['Salario'] < 6000000]
SalarioMujeres = SalarioMujeres[SalarioMujeres['Salario'] < 6000000]

# boxplot de salario por sexo y por rangos de edad en 4 grupos: 14-17, 18-25, 26-40, 41+
SalarioHombres14_17 = SalarioHombres[SalarioHombres['Edad'] <= 17]
SalarioHombres18_25 = SalarioHombres[(SalarioHombres['Edad'] >= 18) & (SalarioHombres['Edad'] <= 25)]
SalarioHombres26_40 = SalarioHombres[(SalarioHombres['Edad'] >= 26) & (SalarioHombres['Edad'] <= 40)]
SalarioHombres41 = SalarioHombres[(SalarioHombres['Edad'] >= 41)]

SalarioMujeres14_17 = SalarioMujeres[SalarioMujeres['Edad'] <= 17]
SalarioMujeres18_25 = SalarioMujeres[(SalarioMujeres['Edad'] >= 18) & (SalarioMujeres['Edad'] <= 25)]
SalarioMujeres26_40 = SalarioMujeres[(SalarioMujeres['Edad'] >= 26) & (SalarioMujeres['Edad'] <= 40)]
SalarioMujeres41 = SalarioMujeres[SalarioMujeres['Edad'] >= 41]

arSaHo = [SalarioHombres14_17['Salario'], SalarioHombres18_25['Salario'], SalarioHombres26_40['Salario'], SalarioHombres41['Salario']]
arSaMu = [SalarioMujeres14_17['Salario'], SalarioMujeres18_25['Salario'], SalarioMujeres26_40['Salario'], SalarioMujeres41['Salario']] 
rangos_edad = ['14-17', '18-25', '26-40', '41+']
plt.boxplot(arSaHo)
plt.title('Boxplot de Salario Hombres')
plt.xlabel('Edades')
plt.ylabel('Salario')
plt.xticks([1, 2, 3, 4], ['14-17', '18-25', '26-40', '41+'])
plt.savefig('./salario/boxplot_salario_hombres.png')
plt.show()
imagen = './salario/boxplot_salario_hombres.png'
guardarImg(imagen)

plt.boxplot(arSaMu)
plt.title('Boxplot de Salario Mujeres')
plt.xlabel('Edades')
plt.ylabel('Salario')
plt.xticks([1, 2, 3, 4], ['14-17', '18-25', '26-40', '41+'])

plt.savefig('./salario/boxplot_salario_mujeres.png')
plt.show()
imagen = './salario/boxplot_salario_mujeres.png'
guardarImg(imagen)

arSaHoMean = [SalarioHombres14_17['Salario'].mean(), SalarioHombres18_25['Salario'].mean(), SalarioHombres26_40['Salario'].mean(), SalarioHombres41['Salario'].mean()]
arSaMuMean = [SalarioMujeres14_17['Salario'].mean(), SalarioMujeres18_25['Salario'].mean(), SalarioMujeres26_40['Salario'].mean(), SalarioMujeres41['Salario'].mean()]

# grafica de comparación de los primerios de salarios de hombres y mujeres por rango etario.
ancho_barras = 0.35
posiciones_hombres = np.arange(len(rangos_edad))
plt.bar(posiciones_hombres, arSaHoMean, ancho_barras, label = "Hombres", color = 'blue')
plt.bar(posiciones_hombres + ancho_barras, arSaMuMean, ancho_barras, label = "Mujeres", color = 'pink')
plt.xlabel('Rango de Edad')
plt.ylabel('Salario Promedio')
plt.title('Comparación de Salarios Promedio por Rango de Edad')
plt.legend()
plt.xticks(posiciones_hombres + ancho_barras/2, rangos_edad)
plt.savefig('./salario/comparacion_salarios_promedio.png')
plt.show()
imagen = './salario/comparacion_salarios_promedio.png'
guardarImg(imagen)
text = "<br/><br/>"
guardarTxt(text*10)
# Comentarios finales
print("Conclusiones:\nComo grupo creemos que a este trabajo por ser el de final de Unidad, nos llevo más tiempo poder realizarlo. Debido a varios factores, como la complejidad del mismo, así como también que en algunas partes de la letra nos hubiera gustado tener más ideas de lo que se nos estaba pidiendo, ya que no quedaba muy claro.\nPor suerte para nosotros los apuntes tomados en clase, las respuestas de los profes a dudas de los compañeros y algunas propias, nos ayudaron a entender un poco mejor que es lo que se quería conseguir con este trabajo.")
text = "Conclusiones:<br/>"
guardarHeader(text,1)
text = "Como grupo creemos que a este trabajo por ser el de final de Unidad, nos llevo más tiempo poder realizarlo. Debido a varios factores, como la complejidad del mismo, así como también que en algunas partes de la letra nos hubiera gustado tener más ideas de lo que se nos estaba pidiendo, ya que no quedaba muy claro.<br/>Por suerte para nosotros los apuntes tomados en clase, las respuestas de los profes a dudas de los compañeros y algunas propias, nos ayudaron a entender un poco mejor que es lo que se quería conseguir con este trabajo."
print("También queremos destacar que poder ver los resultados de los conceptos aprendidos en clase, en un trabajo final, nos ayuda a entender mejor el funcionamiento de los mismos, y nos da una idea de como se aplican en la vida real.")
text += "<br/>También queremos destacar que poder ver los resultados de los conceptos aprendidos en clase, en un trabajo final, nos ayuda a entender mejor el funcionamiento de los mismos, y nos da una idea de como se aplican en la vida real."
print("Para finalizar. Agradecemos a los profesores por la paciencia y la dedicación que nos brindaron en este curso, y esperamos que este trabajo sea de su agrado.\n\n")
text += "<br/>Para finalizar. Agradecemos a los profesores por la paciencia y la dedicación que nos brindaron en este curso, y esperamos que este trabajo sea de su agrado.<br/><br/>"
guardarTxt(text)

# Información sobre el Proyecto
text = "<br/>Enlace al repositorio de GitHub: <br/>"
guardarHeader(text,2)
text = "https://github.com/jumpert/TareaFinal-PyEA.git  <br/><br/>*Nota: Se recomienda clonar el repositorio para poder visualizar el proyecto completo. Para ello utiliza el comando:  'git clone https://github.com/jumpert/TareaFinal-PyEA.git'"
guardarTxt(text)

print("Se esta formalizando el documento, este proceso puede tardar unos segundos...\nPor favor espere...")
# chequear si el documento ya existe
if os.path.exists("Entregable_{}.pdf".format(fecha)):
    #auto incrementar el numero de documento
    counter = 1
    while os.path.exists("Entregable_{}({}).pdf".format(fecha, counter)):
        counter += 1

    # si existe, se crea un nuevo documento
    doc = SimpleDocTemplate("Entregable_{}({}).pdf".format(fecha, counter), pagesize=letter)
    doc.build(contenido)
else:
    doc.build(contenido)