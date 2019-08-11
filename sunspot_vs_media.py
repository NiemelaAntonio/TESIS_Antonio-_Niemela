#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 17:14:02 2019

@author: tony
"""
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator
from datetime import datetime, timedelta, date, time
import numpy as np
import numpy.ma as ma
from collections import defaultdict
import os
from os import listdir
import datetime
from datetime import timedelta, date, time
import matplotlib.dates as mdates
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.colors as colors
import time
from matplotlib.ticker import MaxNLocator
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
import pandas as pd
import csv


pathdatos='/media/tony/TOSHIBAEXT/TESIS/ManchasSolares_y_DST/'
data = pd.read_csv(pathdatos+str('SN_d_tot_V2.0.csv'), sep=";", header=None)
Anio_d=[]
Mes_d=[]
Dia_d=[]
Dato_d=[]
Desviacion_d=[]
Fraccion_d=[]
###############################
# Que representa cada columna?
# ["Anio", "Mes", "Dia", "Dia como fraccion del anio","Daily_Value","Daily_sd","Cantidad de observaciones","definitivo o provisional?"]
#####################################3
for i in range(len(data)):
    if 2011<data[0][i]<2019:
        Dato_d.append(data[4][i])
        Desviacion_d.append(data[5][i])
        Anio_d.append(data[0][i])
        Mes_d.append(data[1][i])
        Dia_d.append(data[2][i])
        Fraccion_d.append(data[3][i])
        
################################################################3
#MENSUAL
data = pd.read_csv(pathdatos+str('SN_m_tot_V2.0.csv'), sep=";", header=None)
Anio_m=[]
Mes_m=[]
Fraccion_m=[]
Dato_m=[]
Desviacion_m=[]

for i in range(len(data)):
    if 2011<data[0][i]<2019:
        Dato_m.append(data[3][i])
        Desviacion_m.append(data[4][i])
        Anio_m.append(data[0][i])
        Mes_m.append(data[1][i])
        Fraccion_m.append(data[2][i])

#########################################3
#Mensual suavizado
data = pd.read_csv(pathdatos+str('SN_ms_tot_V2.0.csv'), sep=";", header=None)
Anio_ms=[]
Mes_ms=[]
Fraccion_ms=[]
Dato_ms=[]
Desviacion_ms=[]

for i in range(len(data)):
    if 2011<data[0][i]<2019:
        Dato_ms.append(data[3][i])
        Desviacion_ms.append(data[4][i])
        Anio_ms.append(data[0][i])
        Mes_ms.append(data[1][i])
        Fraccion_ms.append(data[2][i])
        
T_Inicial=datetime.datetime(Anio_d[0],Mes_d[0],Dia_d[0])
T_Final=datetime.datetime(Anio_d[len(Anio_d)-1],Mes_d[len(Anio_d)-1],Dia_d[len(Anio_d)-1])
T_Delta=datetime.timedelta(days=1)

################
#Defino una funcion que hace el delta
################
def perdelta(start, end, delta):
    curr = start
    while curr < end:
        yield curr
        curr += delta
        
###########################

DATOS_Totales=np.empty([75,31])
DATOS_Totales[0:3,:]=np.load('/media/tony/TOSHIBAEXT/TESIS/DATOS_BINEADOS/Fraccionado_por_anio/x_2012.npy')
DATOS_Totales[3:15,:]=np.load('/media/tony/TOSHIBAEXT/TESIS/DATOS_BINEADOS/Fraccionado_por_anio/x_2013.npy')
DATOS_Totales[15:27,:]=np.load('/media/tony/TOSHIBAEXT/TESIS/DATOS_BINEADOS/Fraccionado_por_anio/x_2014.npy')
DATOS_Totales[27:39,:]=np.load('/media/tony/TOSHIBAEXT/TESIS/DATOS_BINEADOS/Fraccionado_por_anio/x_2015.npy')
DATOS_Totales[39:51,:]=np.load('/media/tony/TOSHIBAEXT/TESIS/DATOS_BINEADOS/Fraccionado_por_anio/x_2016.npy')
DATOS_Totales[51:63,:]=np.load('/media/tony/TOSHIBAEXT/TESIS/DATOS_BINEADOS/Fraccionado_por_anio/x_2017.npy')
DATOS_Totales[63:75,:]=np.load('/media/tony/TOSHIBAEXT/TESIS/DATOS_BINEADOS/Fraccionado_por_anio/x_2018.npy')
Datos_4_3=DATOS_Totales[:,16]
Medias=(np.nanmean(DATOS_Totales,axis=0))
Medianas=np.nanmedian(DATOS_Totales,axis=0)
Log10Medias=np.log10(np.nanmean(DATOS_Totales,axis=0))
Log10Medianas=np.log10(np.nanmedian(DATOS_Totales,axis=0))
bines=np.linspace(1,7,31)+0.1

def moving_average(a, n=5) :
    ret = np.nancumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

Sunspot_moving_avg=moving_average(Dato_m[9:84])
Flux_4_3_moving_avg=moving_average(np.log10(Datos_4_3))

Tiempo=[]
for result in perdelta(T_Inicial, T_Final, timedelta(days=1)):
    Tiempo.append(result)
    

fig, ax1 = plt.subplots()

fig.set_size_inches(11,8)
color = 'tab:red'
ax1.set_xlabel('Time (Years)',fontsize=24)
ax1.set_ylabel('Mean Flux at L=4.3 ($cm^{-2}sr^{-1}s^{-1}MeV^{-1}$) ', color=color,fontsize=24)
ax1.plot(Fraccion_m[9:84],np.log10(Datos_4_3), color=color,lw=1)
ax1.plot(Fraccion_m[11:82],Flux_4_3_moving_avg,linestyle='--', color=color,lw=3)
ax1.tick_params(axis='y', labelcolor=color,labelsize=18)
ax1.tick_params(axis='x',labelsize=18)
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('Sunspot number', color=color,fontsize=24)  # we already handled the x-label with ax1
ax2.plot(Fraccion_m[9:84],Dato_m[9:84], color=color,lw=1)
ax2.plot(Fraccion_m[11:82],Sunspot_moving_avg, linestyle='--',color=color,lw=3)
ax2.tick_params(axis='y', labelcolor=color, labelsize=18)
ax2.tick_params(axis='x', labelsize=18)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.savefig('Ciclo_Solar_vs_media.pdf',format='pdf')
plt.show()  
