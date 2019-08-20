#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 16:42:46 2019

@author: tony
"""

import numpy as np
import matplotlib.pyplot as plt

L=[1,1.2,1.4,1.6,1.8,2,2.2,2.4,2.6,2.8,3,3.2,3.4,3.6,3.8,4,4.2,4.4,4.6,4.8,5,5.2,5.4,5.6,5.8,6,6.2,6.4,6.6,6.8,7]
##############################################

DATOS_Totales=np.empty([75,31])
DATOS_Totales[0:3,:]=np.load('/media/tony/TOSHIBAEXT/TESIS/DATOS_BINEADOS/Fraccionado_por_anio/x_2012.npy')
DATOS_Totales[3:15,:]=np.load('/media/tony/TOSHIBAEXT/TESIS/DATOS_BINEADOS/Fraccionado_por_anio/x_2013.npy')
DATOS_Totales[15:27,:]=np.load('/media/tony/TOSHIBAEXT/TESIS/DATOS_BINEADOS/Fraccionado_por_anio/x_2014.npy')
DATOS_Totales[27:39,:]=np.load('/media/tony/TOSHIBAEXT/TESIS/DATOS_BINEADOS/Fraccionado_por_anio/x_2015.npy')
DATOS_Totales[39:51,:]=np.load('/media/tony/TOSHIBAEXT/TESIS/DATOS_BINEADOS/Fraccionado_por_anio/x_2016.npy')
DATOS_Totales[51:63,:]=np.load('/media/tony/TOSHIBAEXT/TESIS/DATOS_BINEADOS/Fraccionado_por_anio/x_2017.npy')
DATOS_Totales[63:75,:]=np.load('/media/tony/TOSHIBAEXT/TESIS/DATOS_BINEADOS/Fraccionado_por_anio/x_2018.npy')

Medias=(np.nanmean(DATOS_Totales,axis=0))
Desvio=(np.nanstd(DATOS_Totales,axis=0))

Log10Medias=np.nanmean(np.log10(DATOS_Totales),axis=0)
Log10std=np.nanstd(np.log10(DATOS_Totales),axis=0)

bines=np.linspace(1,7,31)+0.1
#################################
#maximo solar

#B/B0=1
#Arriba=2.0MeV
#Abajo=1.6MeV
#Centro=1.8MeV
Arriba=[0.00E+00,1.50E+02,9.50E+04,1.12E+05,2.10E+04,3.20E+03,1.25E+03,1.26E+03,3.46E+04,1.00E+05,2.20E+05,3.50E+05,4.60E+05,5.90E+05,6.50E+05,6.89E+05,6.19E+05,5.70E+05,4.79E+05,3.99E+05,3.29E+05,2.61E+05,2.07E+05,1.63E+05,1.27E+05,9.89E+04,7.31E+04,5.40E+04,3.99E+04,2.60E+04,1.70E+04]
Centro=[0.00E+00,2.04E+02,1.33E+05,1.57E+05,3.66E+04,5.69E+03,2.29E+03,2.90E+03,5.07E+04,1.41E+05,3.05E+05,4.72E+05,6.15E+05,8.09E+05,8.70E+05,9.65E+05,9.05E+05,8.34E+05,7.18E+05,5.99E+05,4.92E+05,3.95E+05,3.17E+05,2.50E+05,1.94E+05,1.51E+05,1.12E+05,8.34E+04,6.20E+04,4.16E+04,2.79E+04]
Log10_centro=np.log10(Centro)
Abajo=[0.00E+00,2.78E+02,1.86E+05,2.20E+05,6.36E+04,1.01E+04,4.21E+03,6.65E+03,7.44E+04,1.98E+05,4.24E+05,6.37E+05,8.22E+05,1.11E+06,1.17E+06,1.35E+06,1.32E+06,1.22E+06,1.08E+06,8.97E+05,7.36E+05,5.96E+05,4.83E+05,3.83E+05,2.97E+05,2.30E+05,1.72E+05,1.29E+05,9.62E+04,6.65E+04,4.60E+04]
#B/B0=2
Arriba1=[0.00E+00,0.00E+00,1.98E+02,1.28E+04,3.86E+03,7.02E+02,2.96E+02,8.11E+02,2.22E+04,6.82E+04,1.53E+05,2.70E+05,3.58E+05,4.64E+05,5.16E+05,5.47E+05,4.92E+05,4.57E+05,3.84E+05,3.20E+05,2.64E+05,2.09E+05,1.66E+05,1.31E+05,1.02E+05,7.92E+04,5.86E+04,4.33E+04,3.20E+04,2.09E+04,1.36E+04]
Centro1=[0.00E+00,0.00E+00,2.78E+02,1.72E+04,6.72E+03,1.25E+03,5.43E+02,1.86E+03,3.26E+04,9.59E+04,2.13E+05,3.64E+05,4.79E+05,6.36E+05,6.91E+05,7.66E+05,7.19E+05,6.69E+05,5.76E+05,4.80E+05,3.95E+05,3.16E+05,2.54E+05,2.00E+05,1.56E+05,1.21E+05,8.99E+04,6.68E+04,4.97E+04,3.33E+04,2.24E+04]
Log10_centro_1=np.log10(Centro1)
Abajo1=[0.00E+00,0.00E+00,3.88E+02,2.33E+04,1.17E+04,2.22E+03,9.96E+02,4.27E+03,4.78E+04,1.35E+05,2.96E+05,4.91E+05,6.40E+05,8.72E+05,9.26E+05,1.07E+06,1.05E+06,9.79E+05,8.63E+05,7.19E+05,5.90E+05,4.78E+05,3.87E+05,3.07E+05,2.38E+05,1.85E+05,1.38E+05,1.03E+05,7.71E+04,5.33E+04,3.68E+04]

###################
#En el minimo
#B/B0=1
Abajo2=[0.00E+00,2.78E+02,1.86E+05,3.10E+05,6.36E+04,1.01E+04,4.21E+03,4.59E+03,2.23E+04,6.34E+04,1.00E+05,1.66E+05,2.37E+05,3.28E+05,4.51E+05,5.65E+05,6.99E+05,8.56E+05,9.20E+05,8.43E+05,7.36E+05,6.00E+05,4.90E+05,3.88E+05,2.99E+05,2.30E+05,1.72E+05,1.29E+05,9.62E+04,6.65E+04,4.60E+04]
Centro2=[0.00E+00,2.04E+02,1.33E+05,2.30E+05,3.66E+04,5.69E+03,2.29E+03,2.14E+03,1.23E+04,3.98E+04,7.56E+04,1.23E+05,1.82E+05,2.57E+05,3.39E+05,4.27E+05,5.10E+05,6.05E+05,6.21E+05,5.66E+05,4.92E+05,4.03E+05,3.30E+05,2.60E+05,1.98E+05,1.51E+05,1.12E+05,8.34E+04,6.20E+04,4.16E+04,2.79E+04]
Log10_centro_2=np.log10(Centro2)
Arriba2=[0.00E+00,1.50E+02,9.50E+04,1.70E+05,2.10E+04,3.20E+03,1.25E+03,1.00E+03,6.81E+03,2.50E+04,5.71E+04,9.11E+04,1.40E+05,2.02E+05,2.55E+05,3.23E+05,3.72E+05,4.27E+05,4.20E+05,3.79E+05,3.29E+05,2.70E+05,2.22E+05,1.74E+05,1.31E+05,9.89E+04,7.31E+04,5.40E+04,3.99E+04,2.60E+04,1.70E+04]

#B/B0=2
Abajo3=[0.00E+00,0.00E+00,3.88E+02,2.33E+04,1.17E+04,2.22E+03,9.96E+02,2.95E+03,1.43E+04,4.32E+04,6.98E+04,1.27E+05,1.84E+05,2.58E+05,3.58E+05,4.49E+05,5.56E+05,6.86E+05,7.37E+05,6.76E+05,5.90E+05,4.81E+05,3.92E+05,3.11E+05,2.40E+05,1.85E+05,1.38E+05,1.03E+05,7.71E+04,5.33E+04,3.68E+04]
Centro3=[0.00E+00,0.00E+00,2.78E+02,1.72E+04,6.72E+03,1.25E+03,5.43E+02,1.38E+03,7.92E+03,2.71E+04,5.27E+04,9.45E+04,1.42E+05,2.02E+05,2.69E+05,3.40E+05,4.05E+05,4.85E+05,4.98E+05,4.53E+05,3.95E+05,3.23E+05,2.64E+05,2.08E+05,1.59E+05,1.21E+05,8.99E+04,6.68E+04,4.97E+04,3.33E+04,2.24E+04]
Log10_centro_3=np.log10(Centro3)
Arriba3=[0.00E+00,0.00E+00,1.98E+02,1.28E+04,3.86E+03,7.02E+02,2.96E+02,6.44E+02,4.38E+03,1.71E+04,3.99E+04,7.01E+04,1.09E+05,1.59E+05,2.03E+05,2.57E+05,2.95E+05,3.43E+05,3.36E+05,3.04E+05,2.64E+05,2.17E+05,1.78E+05,1.40E+05,1.05E+05,7.92E+04,5.86E+04,4.33E+04,3.20E+04,2.09E+04,1.36E+04]

###############################################
#Ploteo B/B0=1 maximo
fig, ax = plt.subplots()
ax.plot(L,Arriba)
ax.plot(L,Centro)
ax.plot(L,Abajo)
ax.plot(bines,Medias)
ax.set_yscale('log')
ax.set_xlabel('Tiempo(Año)')
ax.set_ylabel('Log10(flujo)')
plt.legend(['2.0 MeV','1.8 MeV','1.6 MeV','DATOS'],loc='best')
plt.show()

#Ploteo B/B0=1 minimo
fig, ax = plt.subplots()
ax.plot(L,Arriba2)
ax.plot(L,Centro2)
ax.plot(L,Abajo2)
ax.plot(bines,Medias)
ax.set_yscale('log')
ax.set_xlabel('Tiempo(Año)')
ax.set_ylabel('Log10(flujo)')
plt.legend(['2.0 MeV','1.8 MeV','1.6 MeV','DATOS'],loc='best')
plt.show()

#Ploteo datos vs minimo y maximo
fig, ax = plt.subplots()
ax.plot(L,Centro)
ax.plot(L,Centro2)
ax.plot(bines,Medias)
ax.set_yscale('log')
ax.set_xlabel('L-shell')
ax.set_ylabel('Log10(flujo)')
plt.legend(['1,8MeV en maximo','1,8MeV en minimo','1,8MeV Datos'],loc='best')
plt.show()

#Ploteo datos vs minimo y maximo
fig, ax = plt.subplots()
ax.plot(L,Log10_centro,linewidth=2)
ax.plot(L,Log10_centro_2,linewidth=2)
ax.plot(bines,Log10Medias,linewidth=2,color='green')
ax.plot(bines,Log10Medias+Log10std,'--',linewidth=1,color='green')
ax.plot(bines,Log10Medias-Log10std,'--',linewidth=1,color='green')
#ax.set_yscale('log')
ax.set_xlabel('L-shell')
ax.set_ylabel('Log10(flujo)')
plt.legend(['1,8MeV en maximo','1,8MeV en minimo','1,8MeV Datos'],loc='best')
plt.show()