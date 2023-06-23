# Grupo: Estefany Clara, Gonzalo Paz, Juan Pérez y Lucas Cordero

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import binom
from scipy.stats import geom
from scipy.stats import poisson
from prettytable import PrettyTable
import tkinter as tk
from tkinter import messagebox
import os
ventana = tk.Tk()
ventana.withdraw()

print("Tarea 3 - Probabilidad y Estadística Aplicada\n")
mensaje = "DISTRIBUCIÓN 1: \n\nbinomial de parámetros n = 100 y p = 0,35."
messagebox.showinfo("Mensaje", mensaje)
ventana.destroy()

print(mensaje +"\n")
n, p = 100, 0.35

## Parte 1
# a) Generar 4 muestras de tamaño 100, 1000, 10000 y 100000
r2 = binom.rvs(n, p, size=100)
r3 = binom.rvs(n, p, size=1000)
r4 = binom.rvs(n, p, size=10000)
r5 = binom.rvs(n, p, size=100000)
tipos = [r2, r3, r4, r5]

# b) Boxplot de cada muestra
for tipo in tipos:
    median = np.median(tipo)
    Q1 = np.quantile(tipo, 0.25)
    Q3 = np.quantile(tipo, 0.75)
    min_val = np.min(tipo)
    max_val = np.max(tipo)

    # Rango intercuartílico
    RI = Q3 - Q1
    BII = Q1 - 1.5*RI
    BIS = Q3 + 1.5*RI
    # print('rango para detección de datos atípicos: {}, {}'.format(BII, BIS))

    sns.boxplot(tipo)
    plt.ylabel('Valores')
    plt.title('Boxplot de {} muestras'.format(len(tipo)))
    try:
        plt.savefig('./binomial/boxplot_binomial_{}.png'.format(len(tipo)))
    except:
        os.mkdir('./binomial')
        plt.savefig('./binomial/boxplot_binomial_{}.png'.format(len(tipo)))
    plt.show()
    

# c) Histograma de cada muestra
for tipo in tipos:
    sns.histplot(tipo, kde=True)
    plt.ylabel('Frecuencia')
    plt.title('Histograma de {} muestras'.format(len(tipo)))
    plt.savefig('./binomial/hist_binomial_{}.png'.format(len(tipo)))
    plt.show()
    
# d) Calcular mediana y moda de cada muestra
tabla = PrettyTable()
tabla.field_names = ['Tamaño de muestra', 'Mediana', 'Moda']
for tipo in tipos:
    muestra = len(tipo)    
    median = np.median(tipo)
    mode = np.argmax(np.bincount(tipo))
    tabla.add_row([muestra, round(median,2), round(mode, 2)])
print(tabla)
tabla.clear_rows()

# e) Hallar la media empírica de cada muestra y compararla con la esperanza teórica de la distribución 1. ¿Qué se puede observar en las muestras más grandes?
tabla.field_names = ['Tamaño de muestra', 'Media empírica', 'Media teórica']
for tipo in tipos:
    muestra = len(tipo)
    media_empirica = np.mean(tipo)
    media_teorica = n*p
    tabla.add_row([muestra, round(media_empirica,2), round(media_teorica, 2)])
print(tabla)
tabla.clear_rows()

# f) Calcular la varianza empírica de cada muestra y compararla con la varianza teórica de la distribución 1. ¿Qué se puede observar en las muestras más grandes?
tabla.field_names = ['Tamaño de muestra', 'Varianza empírica', 'Varianza teórica']
for tipo in tipos:
    muestra = len(tipo)
    varianza_empirica = np.var(tipo)
    varianza_teorica = n*p*(1-p)
    tabla.add_row([muestra, round(varianza_empirica,2), round(varianza_teorica, 2)])
print(tabla)
tabla.clear_rows()

print("\n=====================================================================================================\n")

## Parte 2
mensaje = "DISTRIBUCIÓN 2: \n\ngeométrica de parámetro p = 0,08."
print(mensaje)
messagebox.showinfo("Mensaje", mensaje)
p = 0.08

# a) Generar 4 muestras de tamaño 100, 1000, 10000 y 100000
r2 = geom.rvs(p, size=100)
r3 = geom.rvs(p, size=1000)
r4 = geom.rvs(p, size=10000)
r5 = geom.rvs(p, size=100000)
tipos = [r2, r3, r4, r5]

# b) Boxplot de cada muestra
for tipo in tipos:
    median = np.median(tipo)
    Q1 = np.quantile(tipo, 0.25)
    Q3 = np.quantile(tipo, 0.75)
    min_val = np.min(tipo)
    max_val = np.max(tipo)

    # Rango intercuartílico
    RI = Q3 - Q1
    BII = Q1 - 1.5*RI
    BIS = Q3 + 1.5*RI
    # print('rango para detección de datos atípicos: {}, {}'.format(BII, BIS))

    sns.boxplot(tipo)
    plt.ylabel('Valores')
    plt.title('Boxplot de {} muestras'.format(len(tipo)))
    try: 
        plt.savefig('./geom/boxplot_geom_{}.png'.format(len(tipo)))
    except:
        os.mkdir('./geom')
        plt.savefig('./geom/boxplot_geom_{}.png'.format(len(tipo)))
    plt.show()

# c) Histograma de cada muestra
for tipo in tipos:
    sns.histplot(tipo, kde=True)
    plt.ylabel('Frecuencia')
    plt.title('Histograma de {} muestras'.format(len(tipo)))
    plt.savefig('./geom/hist_geom_{}.png'.format(len(tipo)))
    plt.show()
    
# d) Calcular mediana y moda de cada muestra    
tabla.field_names = ['Tamaño de muestra', 'Mediana', 'Moda']
for tipo in tipos:
    muestra = len(tipo)    
    median = np.median(tipo)
    mode = np.argmax(np.bincount(tipo))
    tabla.add_row([muestra, round(median,2), round(mode, 2)])
print(tabla)
tabla.clear_rows()

# e) Hallar la media empírica de cada muestra y compararla con la esperanza teórica de la distribución 2. ¿Qué se puede observar en las muestras más grandes?
tabla.field_names = ['Tamaño de muestra', 'Media empírica', 'Media teórica']
for tipo in tipos:
    muestra = len(tipo)
    media_empirica = np.mean(tipo)
    media_teorica = (1-p)/p
    tabla.add_row([muestra, round(media_empirica,2), round(media_teorica, 2)])
print(tabla)
tabla.clear_rows()

# f) Calcular la varianza empírica de cada muestra y compararla con la varianza teórica de la distribución 2. ¿Qué se puede observar en las muestras más grandes?
tabla.field_names = ['Tamaño de muestra', 'Varianza empírica', 'Varianza teórica']
for tipo in tipos:
    muestra = len(tipo)
    varianza_empirica = np.var(tipo)
    varianza_teorica = (1-p)/(p**2)
    tabla.add_row([muestra, round(varianza_empirica,2), round(varianza_teorica,2)])
print(tabla)
tabla.clear_rows()

print("\n=====================================================================================================\n")

## Parte 3
mensaje = "DISTRIBUCIÓN 3: \n\npoisson de parámetro λ = 30."
messagebox.showinfo("Mensaje", mensaje)
print(mensaje)
L = 30

# a) Generar 4 muestras de tamaño 100, 1000, 10000 y 100000
r2 = poisson.rvs(L, size=100)
r3 = poisson.rvs(L, size=1000)
r4 = poisson.rvs(L, size=10000)
r5 = poisson.rvs(L, size=100000)
tipos = [r2, r3, r4, r5]

# b) Boxplot de cada muestra
for tipo in tipos:
    median = np.median(tipo)
    Q1 = np.quantile(tipo, 0.25)
    Q3 = np.quantile(tipo, 0.75)
    min_val = np.min(tipo)
    max_val = np.max(tipo)

    # Rango intercuartílico
    RI = Q3 - Q1
    BII = Q1 - 1.5*RI
    BIS = Q3 + 1.5*RI
    # print('rango para detección de datos atípicos: {}, {}'.format(BII, BIS))

    sns.boxplot(tipo)
    plt.ylabel('Valores')
    plt.title('Boxplot de {} muestras'.format(len(tipo)))
    try:
        plt.savefig('./poisson/boxplot_pois_{}.png'.format(len(tipo)))
    except:
        os.mkdir('./poisson')
        plt.savefig('./poisson/boxplot_pois_{}.png'.format(len(tipo)))
    plt.show()
    
# c) Histograma de cada muestra
for tipo in tipos:
    sns.histplot(tipo, kde=True)
    plt.ylabel('Frecuencia')
    plt.title('Histograma de {} muestras'.format(len(tipo)))
    plt.savefig('./poisson/hist_pois_{}.png'.format(len(tipo)))
    plt.show()
    
# d) Calcular mediana y moda de cada muestra
tabla.field_names = ['Tamaño de muestra', 'Mediana', 'Moda']
for tipo in tipos:
    muestra = len(tipo)    
    median = np.median(tipo)
    mode = np.argmax(np.bincount(tipo))
    tabla.add_row([muestra, round(median,2), round(mode, 2)])
print(tabla)
tabla.clear_rows()

# e) Hallar la media empírica de cada muestra y compararla con la esperanza teórica de la distribución 3. ¿Qué se puede observar en las muestras más grandes?
tabla.field_names = ['Tamaño de muestra', 'Media empírica', 'Media teórica']
for tipo in tipos:
    muestra = len(tipo)
    media_empirica = np.mean(tipo)
    media_teorica = L
    tabla.add_row([muestra, round(media_empirica,2), round(media_teorica, 2)])
print(tabla)
tabla.clear_rows()

# f) Calcular la varianza empírica de cada muestra y compararla con la varianza teórica de la distribución 3. ¿Qué se puede observar en las muestras más grandes?
tabla.field_names = ['Tamaño de muestra', 'Varianza empírica', 'Varianza teórica']
for tipo in tipos:
    muestra = len(tipo)
    varianza_empirica = np.var(tipo)
    varianza_teorica = L
    tabla.add_row([muestra, round(varianza_empirica,2), round(varianza_teorica, 2)])
print(tabla)
tabla.clear_rows()

mensaje = "FIN DEL PROGRAMA.\n\nPodrá encontrar los gráficos en la carpeta del programa. \nY los resultados en la consola."
messagebox.showinfo("Mensaje", mensaje)

## Solicitar al usuario que ingrese FIN para finalizar el programa, sino seguirá ejecutándose
while True:
    fin = input("Ingrese SALIR para finalizar el programa: ").upper()
    if fin == "SALIR":
        break
    else:
        print("Ingrese FIN para finalizar el programa.")
        continue