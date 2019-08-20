#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 11:44:18 2019

@author: aniemela
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

pathdatos='/media/tony/TOSHIBAEXT/TESIS/GOES/DATOS_CORTADOS/'
Datos_Goes_E1E=np.load(pathdatos+str('Datos_GOES_E1E.npy'))
Datos_Goes_E1W=np.load(pathdatos+str('Datos_GOES_E1W.npy'))
Datos_Goes_E2E=np.load(pathdatos+str('Datos_GOES_E2E.npy'))
Datos_Goes_E2W=np.load(pathdatos+str('Datos_GOES_E2W.npy'))

Tiempo_Posta_E1E=np.empty_like(Datos_Goes_E1E[:,0],dtype=object)


for j in range(len(Datos_Goes_E1E[:,0])):
    Tiempo_Posta_E1E[j]=datetime.datetime.fromtimestamp(Datos_Goes_E1E[j,0]/1000)
    

Threshold_Solarmonitor=np.empty_like(Tiempo_Posta_E1E)
Threshold_Solarmonitor[:]=10**2
Datos_Goes_E1E=ma.masked_where(Datos_Goes_E1E[:,1] == -99999, Datos_Goes_E1E[:,1])
Datos_Goes_E1E=ma.masked_where(Datos_Goes_E1E[:] == 0, Datos_Goes_E1E[:])
Datos_Goes_E1W=ma.masked_where(Datos_Goes_E1W[:,1] == -99999, Datos_Goes_E1W[:,1])
Datos_Goes_E1W=ma.masked_where(Datos_Goes_E1W[:] == 0, Datos_Goes_E1W[:])
Datos_Goes_E2E=ma.masked_where(Datos_Goes_E2E[:,1] == -99999, Datos_Goes_E2E[:,1])
Datos_Goes_E2E=ma.masked_where(Datos_Goes_E2E[:] == 0, Datos_Goes_E2E[:])
Datos_Goes_E2W=ma.masked_where(Datos_Goes_E2W[:,1] == -99999, Datos_Goes_E2W[:,1])
Datos_Goes_E2W=ma.masked_where(Datos_Goes_E2W[:] == 0, Datos_Goes_E2W[:])

Relacion_entre_energias_E=np.empty_like(Tiempo_Posta_E1E)
Relacion_entre_energias_W=np.empty_like(Tiempo_Posta_E1E)
for i in range(len(Datos_Goes_E1E)):
    Relacion_entre_energias_E[i]=Datos_Goes_E1E[i]/Datos_Goes_E2E[i]
    Relacion_entre_energias_W[i]=Datos_Goes_E1W[i]/Datos_Goes_E2W[i]
    
####################Separación de años##############
Doce=219060
Trece=744660
Catorce=1270260
Quince=1795860
Dieciseis=2320020
Diecisiete=2845620
Dieciocho=len(Tiempo_Posta_E1E)-1
Mayo=3021500
Junio=3100000
###########################################
#PLOTEO
###########################################


year = mdates.MonthLocator(interval=2)
months = mdates.MonthLocator(interval=1)
yearFmt = mdates.DateFormatter('%Y/%m/%d')
fig, ax = plt.subplots()
#ax.plot(Tiempo_Posta_E1E[Diecisiete:Dieciocho],Datos_Goes_E1E[Diecisiete:Dieciocho])
#ax.plot(Tiempo_Posta_E1E[Diecisiete:Dieciocho],Datos_Goes_E1W[Diecisiete:Dieciocho])
#ax.plot(Tiempo_Posta_E1E[Diecisiete:Dieciocho],Datos_Goes_E2E[Diecisiete:Dieciocho])
ax.plot(Tiempo_Posta_E1E[Mayo:Junio],Datos_Goes_E2W[Mayo:Junio])
ax.plot(Tiempo_Posta_E1E[Mayo:Junio],Threshold_Solarmonitor[Mayo:Junio],'--')
# format the ticks
ax.xaxis.set_major_locator(year)
ax.xaxis.set_major_formatter(yearFmt)
ax.xaxis.set_minor_locator(months)
ax.set_xlim(Tiempo_Posta_E1E[Mayo], Tiempo_Posta_E1E[Junio])
ax.set_yscale('log')
ax.set_ylim((10**-1),(10**7))
plt.legend(['E2W','Threshold'],loc='best')
fig.autofmt_xdate()
ax.set_xlabel('Tiempo(Año)')
ax.set_ylabel('Log10(flujo)')
plt.title('Flujo de electrones con E>0.8MeV para sensor Este de GOES 2018',loc='center')
plt.show()
###################################
#Plot de la relacion entre Flujos
###################################

year = mdates.MonthLocator(interval=2)
months = mdates.MonthLocator(interval=1)
yearFmt = mdates.DateFormatter('%Y/%m/%d')
fig, ax = plt.subplots()
ax.plot(Tiempo_Posta_E1E[Trece:Catorce],Relacion_entre_energias_E[Trece:Catorce])
ax.plot(Tiempo_Posta_E1E[Trece:Catorce],Threshold_Solarmonitor[Trece:Catorce],'--')
# format the ticks
ax.xaxis.set_major_locator(year)
ax.xaxis.set_major_formatter(yearFmt)
ax.xaxis.set_minor_locator(months)
ax.set_xlim(Tiempo_Posta_E1E[Trece], Tiempo_Posta_E1E[Catorce])
ax.set_yscale('log')
ax.set_ylim((10**-1),(10**7))
plt.legend(['Relacion entre Flujos','Threshold'],loc='best')
fig.autofmt_xdate()
ax.set_xlabel('Tiempo(Año)')
ax.set_ylabel('Log10(flujo)')
plt.title('Relacion entre Flujo de electrones con E>0.8MeV y E>2MeV para sensor Este de GOES 2018',loc='center')
plt.show()