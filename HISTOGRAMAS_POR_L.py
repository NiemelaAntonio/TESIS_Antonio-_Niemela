#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 18:30:52 2019

@author: aniemela
"""



from scipy import stats
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
from datetime import datetime
from datetime import datetime, timedelta, date, time
import matplotlib.dates as mdates
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.colors as colors

pathdatos='/home/aniemela/Documentos/TESIS/DATOS_BINEADOS/FESA_BINARIO/'
Lista_Nombres=sorted(os.listdir(pathdatos))
bines=np.linspace(1,7,31)+0.1
DATOS_L_hola=[]
DATOS_L_primero=[]
for i in range(len(Lista_Nombres)):
    DATOS_L_hola=np.load(pathdatos+str(Lista_Nombres[i]))[:,28]
    DATOS_L_hola[DATOS_L_hola==0]=['nan']
    DATOS_L_hola=DATOS_L_hola[~np.isnan(DATOS_L_hola)]
    DATOS_L_primero.append(DATOS_L_hola)
LONGITUD_p=[]
#ACA agarro los datos de toda la mision para graficar despues
DATOS_Totales=(np.load(pathdatos+str(Lista_Nombres[len(Lista_Nombres)-1]))[:,28])
DATOS_Totales[DATOS_Totales==0]=['nan']
DATOS_Totales=DATOS_Totales[~np.isnan(DATOS_Totales)]
DATOS_Totales=np.log10(DATOS_Totales)
Media_Total=np.mean(DATOS_Totales)
Mediana_Total=np.median(DATOS_Totales)

for i in range(len(DATOS_L_primero)):
    LONGITUD_p.append(len(DATOS_L_primero[i]))
    
for i in range(len(DATOS_L_primero)-1):
    DATOS_L_primero[i+1][0:len(DATOS_L_primero[i])]=['nan']
DATOS_L_Posta=[]
for i in range(len(DATOS_L_primero)):
    DATOS_L_primero_aux=DATOS_L_primero[i]
    DATOS_L_primero_aux[DATOS_L_primero_aux==0]=['nan']
    DATOS_L_primero_aux=DATOS_L_primero_aux[~np.isnan(DATOS_L_primero_aux)]
    DATOS_L_Posta.append(DATOS_L_primero_aux)
    

a=np.empty([len(DATOS_L_Posta),2])
for i in range(len(DATOS_L_Posta)):
    DATOS_L_Posta[i]=np.log10(DATOS_L_Posta[i])
    a[i,0]=np.nanmean(DATOS_L_Posta[i])
    a[i,1]=np.nanmedian(DATOS_L_Posta[i])


fig, axs = plt.subplots(4, 2,sharey=False, sharex=True, constrained_layout=True)
fig.suptitle('Histogramas por L para L=6.7 para 1.8MeV',fontsize=24)
fig.set_size_inches(20.5, 28.5)

# We can set the number of bins with the `bins` kwarg
axs[0][0].hist(DATOS_L_Posta[0], bins=10)
axs[0][0].set_title('2012')
axs[0][0].set_ylabel('Frecuencia')
axs[0][0].set_xlabel('log10(Flujo)')
axs[0][0].axvline(a[0][0], color='b', linestyle='dashed', linewidth=1)
axs[0][0].axvline(a[0][1], color='r', linestyle='-', linewidth=1)
axs[0][0].legend(['media:'+str(round(a[0][0],3)),'mediana:'+str(round(a[0][1],3))])

#axs[0][0].set_xscale('symlog')
axs[0][1].hist(DATOS_L_Posta[1], bins=10)
axs[0][1].set_title('2013')
axs[0][1].set_ylabel('Frecuencia')
axs[0][1].set_xlabel('log10(Flujo)')
axs[0][1].axvline(a[1][0], color='b', linestyle='dashed', linewidth=1)
axs[0][1].axvline(a[1][1], color='r', linestyle='-', linewidth=1)
axs[0][1].legend(['media:'+str(round(a[1][0],3)),'mediana:'+str(round(a[1][1],3))])
#axs[0][1].set_xscale('symlog')
axs[1][0].hist(DATOS_L_Posta[2],bins=10)
axs[1][0].set_title('2014')
axs[1][0].set_ylabel('Frecuencia')
axs[1][0].set_xlabel('log10(Flujo)')
axs[1][0].axvline(a[2][0], color='b', linestyle='dashed', linewidth=1)
axs[1][0].axvline(a[2][1], color='r', linestyle='-', linewidth=1)
axs[1][0].legend(['media:'+str(round(a[2][0],3)),'mediana:'+str(round(a[2][1],3))])
#axs[0][2].set_xscale('symlog')

axs[1][1].hist(DATOS_L_Posta[3],bins=10)
axs[1][1].set_title('2015')
axs[1][1].set_ylabel('Frecuencia')
axs[1][1].set_xlabel('log10(Flujo)')
axs[1][1].axvline(a[3][0], color='b', linestyle='dashed', linewidth=1)
axs[1][1].axvline(a[3][1], color='r', linestyle='-', linewidth=1)
axs[1][1].legend(['media:'+str(round(a[3][0],3)),'mediana:'+str(round(a[3][1],3))])

axs[2][0].hist(DATOS_L_Posta[4],bins=10)
axs[2][0].set_title('2016')
axs[2][0].set_ylabel('Frecuencia')
axs[2][0].set_xlabel('log10(Flujo)')
axs[2][0].axvline(a[4][0], color='b', linestyle='dashed', linewidth=1)
axs[2][0].axvline(a[4][1], color='r', linestyle='-', linewidth=1)
axs[2][0].legend(['media:'+str(round(a[4][0],3)),'mediana:'+str(round(a[4][1],3))])

axs[2][1].hist(DATOS_L_Posta[5],bins=10)
axs[2][1].set_title('2017')
axs[2][1].set_ylabel('Frecuencia')
axs[2][1].set_xlabel('log10(Flujo)')
axs[2][1].axvline(a[5][0], color='b', linestyle='dashed', linewidth=1)
axs[2][1].axvline(a[5][1], color='r', linestyle='-', linewidth=1)
axs[2][1].legend(['media:'+str(round(a[5][0],3)),'mediana:'+str(round(a[5][1],3))])

axs[3][0].hist(DATOS_L_Posta[6],bins=10)
axs[3][0].set_title('2018')
axs[3][0].set_ylabel('Frecuencia')
axs[3][0].set_xlabel('log10(Flujo)')
axs[3][0].axvline(a[6][0], color='b', linestyle='dashed', linewidth=1)
axs[3][0].axvline(a[6][1], color='r', linestyle='-', linewidth=1)
axs[3][0].legend(['media:'+str(round(a[6][0],3)),'mediana:'+str(round(a[6][1],3))])

axs[3][1].hist(DATOS_Totales,bins=10)
axs[3][1].set_title('Toda la mision')
axs[3][1].set_ylabel('Frecuencia')
axs[3][1].set_xlabel('log10(Flujo)')
axs[3][1].axvline(Media_Total, color='b', linestyle='dashed', linewidth=1)
axs[3][1].axvline(Mediana_Total, color='r', linestyle='-', linewidth=1)
axs[3][1].legend(['media:'+str(round(Media_Total,3)),'mediana:'+str(round(Mediana_Total,3))])

plt.show()