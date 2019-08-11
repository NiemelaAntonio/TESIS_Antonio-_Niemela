#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 13:56:57 2019

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

pathdatos='/media/tony/TOSHIBAEXT/TESIS/GOES/DATOS_CORTADOS/'
Datos_Goes_E1E=np.load(pathdatos+str('Datos_GOES_E1E.npy'))
Datos_Goes_E1W=np.load(pathdatos+str('Datos_GOES_E1W.npy'))
Datos_Goes_E2E=np.load(pathdatos+str('Datos_GOES_E2E.npy'))
Datos_Goes_E2W=np.load(pathdatos+str('Datos_GOES_E2W.npy'))

Tiempo_Posta_E1E=np.empty_like(Datos_Goes_E1E[:,0],dtype=object)



for j in range(len(Datos_Goes_E1E[:,0])):
    Tiempo_Posta_E1E[j]=datetime.datetime.fromtimestamp(Datos_Goes_E1E[j,0]/1000)
    

Threshold_Solarmonitor=np.empty_like(Tiempo_Posta_E1E)
Threshold_Solarmonitor[:]=10**3
Datos_Goes_E1E=ma.masked_where(Datos_Goes_E1E[:,1] == -99999, Datos_Goes_E1E[:,1])
Datos_Goes_E1W=ma.masked_where(Datos_Goes_E1W[:,1] == -99999, Datos_Goes_E1W[:,1])
Datos_Goes_E2E=ma.masked_where(Datos_Goes_E2E[:,1] == -99999, Datos_Goes_E2E[:,1])
Datos_Goes_E2W=ma.masked_where(Datos_Goes_E2W[:,1] == -99999, Datos_Goes_E2W[:,1])
####Separación de años
Doce=219060
Trece=744660
Catorce=1270260
Quince=1795860
Dieciseis=2320020
Diecisiete=2845620
Dieciocho=len(Tiempo_Posta_E1E)-1
InicioAgosto=3179700
FinSeptiembre=3224340

#########################
#DST
############################
#Cargo la tabla desde el txt, previamente separada con comas
############################
pathdatos='/media/tony/TOSHIBAEXT/TESIS/ManchasSolares_y_DST/'
data = pd.read_csv(pathdatos+str('DST_20120920_20181231.txt'), sep=",", header=None)
data.columns = ["Año", "Dia", "Hora", "DST (nT)"]
T_Inicial=datetime.datetime(data['Año'][0],9,21,0,0)
T_Final=datetime.datetime(data['Año'][len(data['Año'])-1],12,31,23,00)
T_Delta=datetime.timedelta(hours=1)
################
#Defino una funcion que hace el delta
################
def perdelta(start, end, delta):
    curr = start
    while curr < end:
        yield curr
        curr += delta
        
###########################
Tiempo=[]
for result in perdelta(T_Inicial, T_Final, timedelta(hours=1)):
    Tiempo.append(result)
#############################
#ploteo la variable
#############################
#plt.plot(Tiempo[51840:52103],data['DST (nT)'][51840:52103])


###########################################
#PLOTEO
###########################################


year = mdates.DayLocator(interval=2)
#months = mdates.Locator(interval=1)
yearFmt = mdates.DateFormatter('%d/%m')
fig, ax = plt.subplots()
fig.set_size_inches(20,10)
#eax.plot(Tiempo_Posta_E1E[Diecisiete:Dieciocho],Datos_Goes_E1E[Diecisiete:Dieciocho])
#ax.plot(Tiempo_Posta_E1E[Diecisiete:Dieciocho],Datos_Goes_E1W[Diecisiete:Dieciocho])
ax.plot(Tiempo_Posta_E1E[InicioAgosto:FinSeptiembre],Datos_Goes_E2W[InicioAgosto:FinSeptiembre],lw=3,color='red')
ax.plot(Tiempo_Posta_E1E[InicioAgosto:FinSeptiembre],Datos_Goes_E1W[InicioAgosto:FinSeptiembre],lw=3,color='orange')
ax.plot(Tiempo_Posta_E1E[InicioAgosto:FinSeptiembre],Threshold_Solarmonitor[InicioAgosto:FinSeptiembre],'--',color='red')
# format the ticks
ax.xaxis.set_major_locator(year)
ax.xaxis.set_major_formatter(yearFmt)
#ax.xaxis.set_minor_locator(months)
ax.set_xlim(Tiempo_Posta_E1E[InicioAgosto], Tiempo_Posta_E1E[FinSeptiembre])
ax.set_yscale('log')
ax.set_ylim((10**-1),(10**7))
#plt.legend(['E2W','Threshold'],loc='best')
fig.autofmt_xdate()
ax.set_xlabel('Time (Day/Month)',fontsize=24)
ax.set_ylabel('Electron Flux ($cm^{-2}s^{-1}sr^{-1}$)',color='red',fontsize=24)
ax.tick_params(axis='y',labelsize=18,labelcolor='red')
ax.tick_params(axis='x',labelsize=18,rotation=0)
ax.legend(['E<2MeV','E<0.8MeV'],fontsize=18)

ax2 = ax.twinx()
color = 'tab:blue'
ax2.set_ylabel('DST index (nT)', color=color,fontsize=24)  # we already handled the x-label with ax1
ax2.plot(Tiempo[51840:53304],data['DST (nT)'][51840:53304], color=color,lw=1)
ax2.tick_params(axis='y', labelcolor=color, labelsize=18)
ax2.tick_params(axis='x', labelsize=18,rotation=0)
ax2.xaxis.set_major_formatter(yearFmt)
ax2.xaxis.set_major_locator(year)
fig.tight_layout()  # otherwise the right y-label is slightly clipped
#plt.title('Flujo de electrones con E>0.8MeV para sensor Este de GOES 2018',loc='center')
plt.savefig('GOES_Flujo_Ago_21_8_a_21_9.pdf',format='pdf')
plt.show()