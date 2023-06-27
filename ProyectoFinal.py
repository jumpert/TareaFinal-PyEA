# importar el archivo .csv que se encuentra en la misma carpeta, que contiene los datos

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#import prettytable as pt
import tkinter as tk
from tkinter import messagebox
from prettytable import PrettyTable
import os
from typing import Any

ventana = tk.Tk()
ventana.withdraw()
# IMPORTAR EL ARCHIVO .CSV QUE SE ENCUENTRA EN LA MISMA CARPETA, QUE CONTIENE LOS DATOS
names = ['ID', 'anio', 'mes', 'Sexo', 'Edad', 'region', 'PEA', 'Desempleo', 'Salario']
data = pd.read_csv('./ECH_2022-PyE2023.csv',sep=';', names=names, header=0)
data= data.dropna(subset=['Salario'])

# Convertir los valores en la columna "Salario" a tipo numérico
data['Salario'] = pd.to_numeric(data['Salario'], errors='coerce')

print("Proyecto Final - Probabilidad y Estadística Aplicada\n")
print("")
print("Parte A - DESEMPLEADOS")
"""
# a) Calcular la tasa de desempleo para la muestra
# contar la cantidad de desempleados si PEA = 1 y Desempleo = 0
desempleados = data[(data['PEA'] == 1) & (data['Desempleo'] == 0)]
#contar la cantidad de personas desempleados
print("La cantidad de desempleados presentados en la muestra son: {}".format(len(desempleados)))
tea = len(data['PEA'])
print("La cantidad de personas en la muestra son: {}".format(tea))
desempleo = len(desempleados) / tea
print("1- a- La taza de desempleo es: ", desempleo)

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
# b) Histograma de cada muestra
for tipo in desempleadosAr:
    sns.histplot(tipo, kde=True)
    plt.ylabel('Frecuencia')
    plt.title('Histograma de desempleados por edades')
    try:
        plt.savefig('./desempleados/histograma_desempleados_{}.png'.format(len(tipo)))
    except:
        os.mkdir('./desempleados')
        plt.savefig('./desempleados/histograma_desempleados_{}.png'.format(len(tipo)))
    plt.show()
"""
#Ejercicio parte 2 Salario
#calcular media, mediana y moda del salario
print("Parte 2 - SALARIO")
print("a. Elaborar un histograma de la variable salario")
salario = data['Salario']
sns.histplot(data['Salario'], kde=True)
plt.ylabel('Frecuencia')
plt.title('Histograma de salario')
plt.show()
plt.savefig('./salario/histograma_salario.png')

# Elaborar Boxplot para toda la muestra
print("2) b. Elaborar un Boxplot para toda la muestra")
sns.boxplot(data['Salario'])
plt.title('Boxplot de salario')
plt.show()
plt.savefig('./salario/boxplot_salario.png')

# Estudio de Boxplot
mediana = np.median(salario)
Q1 = np.quantile(salario, 0.25)
Q3 = np.quantile(salario, 0.75)
min_val = np.min(salario)
max_mal = np.max(salario)

# Rango intercuartilico
RI = Q3 - Q1
BII = Q1 - (1.5 * RI)
BSI = Q3 + (1.5 * RI)

print("i. Existen valores atípicos en la muestra. Si existen, ¿cuántos son?")
# Calcular la cantidad de valores atípicos
outliers = data[(data['Salario'] < BII) | (data['Salario'] > BSI)]
print("La cantidad de valores atípicos son: {}".format(len(outliers)))

print("ii. Corrección de valores atípicos")
# Corregir los valores atípicos
data['Salario'] = np.where(data['Salario'] < BII, BII, data['Salario'])
data['Salario'] = np.where(data['Salario'] > BSI, BSI, data['Salario'])
# Volver a graficar el Boxplot
sns.boxplot(data['Salario'])
plt.title('Boxplot de salario')
plt.show()
plt.savefig('./salario/boxplot_salario_corregido.png')

media = np.mean(salario)
moda = np.mode(salario)

print("2) c. Media: {}, Mediana: {}, Moda: {}".format(media, mediana, moda))

print("Valores de estudio del Boxplot de Salarios")
print("2) d. Q1: {}, Q3: {}, Mínimo: {}, Máximo: {}, RI: {}, BII: {}, BSI: {}".format(mediana, Q1, Q3, min_val, max_mal, RI, BII, BSI))

# Elaborar Boxplot por genero (masculino y femenino)
print("2) e. Elaborar un Boxplot por género (masculino y femenino)")
sns.boxplot(x=data['Sexo'], y=data['Salario'])
plt.title('Boxplot de salario por género')
plt.show()
plt.savefig('./salario/boxplot_salario_genero.png')
