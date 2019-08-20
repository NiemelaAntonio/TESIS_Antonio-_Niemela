#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 15:49:57 2019

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

Tiempo_Posta_E1E=np.empty_like(Datos_Goes_E2W[:,0],dtype=object)


for j in range(len(Datos_Goes_E2W[:,0])):
    Tiempo_Posta_E1E[j]=datetime.datetime.fromtimestamp(Datos_Goes_E2W[j,0]/1000)
    
    
    

Datos_Goes_E1E[Datos_Goes_E1E[:,1] == -99999]=np.nan
Datos_Goes_E1E[:,1]=np.log10(Datos_Goes_E1E[:,1])
Datos_Goes_E1W[Datos_Goes_E1W[:,1] == -99999]=np.nan
Datos_Goes_E1W[:,1]=np.log10(Datos_Goes_E1W[:,1])
Datos_Goes_E2E[Datos_Goes_E2E[:,1] == -99999]=np.nan
Datos_Goes_E2E[:,1]=np.log10(Datos_Goes_E2E[:,1])
Datos_Goes_E2W[Datos_Goes_E2W[:,1] == -99999]=np.nan
Datos_Goes_E2W[:,1]=np.log10(Datos_Goes_E2W[:,1])

######################################################
##Limites de los años
######################################################
Doce=219060
Trece=744660
Catorce=1270260
Quince=1795860
Dieciseis=2320020
Diecisiete=2845620
Dieciocho=len(Tiempo_Posta_E1E)-1

#####################################################
#Medias y Medianas
#####################################################
a=np.empty([8,2],dtype=float)
a[0,1]=np.nanmean(Datos_Goes_E1E[0:Doce,1])
a[1,1]=np.nanmean(Datos_Goes_E1E[Doce:Trece,1])
a[2,1]=np.nanmean(Datos_Goes_E1E[Trece:Catorce,1])
a[3,1]=np.nanmean(Datos_Goes_E1E[Catorce:Quince,1])
a[4,1]=np.nanmean(Datos_Goes_E1E[Quince:Dieciseis,1])
a[5,1]=np.nanmean(Datos_Goes_E1E[Dieciseis:Diecisiete,1])
a[6,1]=np.nanmean(Datos_Goes_E1E[Diecisiete:Dieciocho,1])
a[7,1]=np.nanmean(Datos_Goes_E1E[:,1])
a[0,0]=np.nanmedian(Datos_Goes_E1E[0:Doce,1])
a[1,0]=np.nanmedian(Datos_Goes_E1E[Doce:Trece,1])
a[2,0]=np.nanmedian(Datos_Goes_E1E[Trece:Catorce,1])
a[3,0]=np.nanmedian(Datos_Goes_E1E[Catorce:Quince,1])
a[4,0]=np.nanmedian(Datos_Goes_E1E[Quince:Dieciseis,1])
a[5,0]=np.nanmedian(Datos_Goes_E1E[Dieciseis:Diecisiete,1])
a[6,0]=np.nanmedian(Datos_Goes_E1E[Diecisiete:Dieciocho,1])
a[7,0]=np.nanmedian(Datos_Goes_E1E[:,1])


#####################################################
#Ploteo de Histogramas
#####################################################


fig, axs = plt.subplots(4, 2,sharey=False, sharex=True, constrained_layout=True)
fig.suptitle('Histogramas para GOES para E>0.8MeV Sensor Este',fontsize=24)
fig.set_size_inches(20.5, 28.5)

axs[0][0].hist(Datos_Goes_E1E[0:Doce,1], bins=10)
axs[0][0].set_title('2012')
axs[0][0].set_ylabel('Frecuencia')
axs[0][0].set_xlabel('log10(Flujo)')
axs[0][0].axvline(a[0][1], color='b', linestyle='dashed', linewidth=1)
axs[0][0].axvline(a[0][0], color='r', linestyle='-', linewidth=1)
axs[0][0].legend(['media:'+str(round(a[0][0],3)),'mediana:'+str(round(a[0][1],3))])


axs[0][1].hist(Datos_Goes_E1E[Doce:Trece,1], bins=10)
axs[0][1].set_title('2013')
axs[0][1].set_ylabel('Frecuencia')
axs[0][1].set_xlabel('log10(Flujo)')
axs[0][1].axvline(a[1][1], color='b', linestyle='dashed', linewidth=1)
axs[0][1].axvline(a[1][0], color='r', linestyle='-', linewidth=1)
axs[0][1].legend(['media:'+str(round(a[1][0],3)),'mediana:'+str(round(a[1][1],3))])


axs[1][0].hist(Datos_Goes_E1E[Trece:Catorce,1], bins=10)
axs[1][0].set_title('2014')
axs[1][0].set_ylabel('Frecuencia')
axs[1][0].set_xlabel('log10(Flujo)')
axs[1][0].axvline(a[2][1], color='b', linestyle='dashed', linewidth=1)
axs[1][0].axvline(a[2][0], color='r', linestyle='-', linewidth=1)
axs[1][0].legend(['media:'+str(round(a[2][0],3)),'mediana:'+str(round(a[2][1],3))])

axs[1][1].hist(Datos_Goes_E1E[Catorce:Quince,1], bins=10)
axs[1][1].set_title('2015')
axs[1][1].set_ylabel('Frecuencia')
axs[1][1].set_xlabel('log10(Flujo)')
axs[1][1].axvline(a[3][1], color='b', linestyle='dashed', linewidth=1)
axs[1][1].axvline(a[3][0], color='r', linestyle='-', linewidth=1)
axs[1][1].legend(['media:'+str(round(a[3][0],3)),'mediana:'+str(round(a[3][1],3))])


axs[2][0].hist(Datos_Goes_E1E[Quince:Dieciseis,1], bins=10)
axs[2][0].set_title('2016')
axs[2][0].set_ylabel('Frecuencia')
axs[2][0].set_xlabel('log10(Flujo)')
axs[2][0].axvline(a[4][1], color='b', linestyle='dashed', linewidth=1)
axs[2][0].axvline(a[4][0], color='r', linestyle='-', linewidth=1)
axs[2][0].legend(['media:'+str(round(a[4][0],3)),'mediana:'+str(round(a[4][1],3))])

axs[2][1].hist(Datos_Goes_E1E[Dieciseis:Diecisiete,1], bins=10)
axs[2][1].set_title('2017')
axs[2][1].set_ylabel('Frecuencia')
axs[2][1].set_xlabel('log10(Flujo)')
axs[2][1].axvline(a[5][1], color='b', linestyle='dashed', linewidth=1)
axs[2][1].axvline(a[5][0], color='r', linestyle='-', linewidth=1)
axs[2][1].legend(['media:'+str(round(a[5][0],3)),'mediana:'+str(round(a[5][1],3))])

axs[3][0].hist(Datos_Goes_E1E[Diecisiete:Dieciocho,1], bins=10)
axs[3][0].set_title('2018')
axs[3][0].set_ylabel('Frecuencia')
axs[3][0].set_xlabel('log10(Flujo)')
axs[3][0].axvline(a[6][1], color='b', linestyle='dashed', linewidth=1)
axs[3][0].axvline(a[6][0], color='r', linestyle='-', linewidth=1)
axs[3][0].legend(['media:'+str(round(a[6][0],3)),'mediana:'+str(round(a[6][1],3))])

axs[3][1].hist(Datos_Goes_E1E[:,1], bins=10)
axs[3][1].set_title('Período 2012-2018')
axs[3][1].set_ylabel('Frecuencia')
axs[3][1].set_xlabel('log10(Flujo)')
axs[3][1].axvline(a[7][1], color='b', linestyle='dashed', linewidth=1)
axs[3][1].axvline(a[7][0], color='r', linestyle='-', linewidth=1)
axs[3][1].legend(['media:'+str(round(a[7][0],3)),'mediana:'+str(round(a[7][1],3))])
