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

# contar la cantidad de desempleados si PEA = 1 y Desempleo = 0
desempleados = data[(data['PEA'] == 1) & (data['Desempleo'] == 0)]
#contar la cantidad de personas desempleados
print(len(desempleados))
tea = len(data['PEA'])
print(tea)
desempleo = len(desempleados) / tea
print("1- a- La taza de desempleo es: ", desempleo)

# utilizando desempleo agruparlos por rango de edad de 14 a 17, 18 a 25, 26 a 40 y más de 40
desempleados_14_17 = desempleados[(desempleados['Edad'] >= 14) & (desempleados['Edad'] <= 17)]
desempleados_18_25 = desempleados[(desempleados['Edad'] >= 18) & (desempleados['Edad'] <= 25)]
desempleados_26_40 = desempleados[(desempleados['Edad'] >= 26) & (desempleados['Edad'] <= 40)]
desempleados_41 = desempleados[(desempleados['Edad'] >= 41)]
desempleadosAr = [len(desempleados_14_17), len(desempleados_18_25), len(desempleados_26_40),  len(desempleados_41)]
print(desempleadosAr)   #cantidad de desepleados por edades. 

#Ejercicio parte 2 Salario
#calcular media, mediana y moda del salario
columna = data['Salario']
media = columna.mean()
mediana = columna.median()
moda = columna.mode()

print("2- a- La media del salario es: ", media)
print("2- b- La mediana del salario es: ", mediana)
print("2- c- La moda del salario es: ", moda) #esto da cero pero no sé si está bien





