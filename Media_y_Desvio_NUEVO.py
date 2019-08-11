#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 13:51:17 2019

@author: tony
"""
'''
ESTE LO CORRI EN LA DE SERGIO PORQUE QUEMA TODA LA MEMORIA
'''

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
import csv
import pylab

pathdatos='/home/tonyto94/Desktop/FESA_BINEADOS_DISCO_EXTERNO/Fraccionado_por_anio/'
Lista_Nombres=os.listdir(pathdatos)
list.sort(Lista_Nombres)
Lista_Nombres_1=Lista_Nombres[7:14]

'''
Medias_1=[]
Desvios_1=[]
for i in range(len(Lista_Nombres_1)):
    filename=pathdatos+str(Lista_Nombres_1[i])
    Fesa_1=np.load(filename)[0,:,:]
    Media=np.nanmean(Fesa_1,axis=0)
    Medias_1.append(Media)
    Desvio=np.nanstd(Fesa_1,axis=0)
    Desvios_1.append(Desvio)
'''
'''
np.save('Desvios_por_bines',Desvios_1)
np.save('Medias_por_bines',Medias_1)
'''
Medias_1=np.load('Medias_por_bines.npy')
Desvios_1=np.load('Desvios_por_bines.npy')

Desvios_por_bin=np.mean(Desvios_1,axis=0)
Medias_por_bin=np.mean(Medias_1,axis=0)
    
#################################
#Ploteo
#################################
bines=np.linspace(1,7,31)+0.1

Arriba=Medias_por_bin+Desvios_por_bin
Abajo=Medias_por_bin-Desvios_por_bin

fig = plt.figure()
fig.set_size_inches(18,10)
ax = fig.add_subplot(2, 1, 1)
line, = ax.plot(bines,Medias_por_bin, color='red', lw=3)
line, =ax.plot(bines,Arriba,color='blue',lw=1)
line, =ax.plot(bines,Abajo,color='blue',lw=1)
ax.set_yscale('log')
ax.set_ylabel('Mean Electron Flux \n ($cm^{-2}sr^{-1}s^{-1}MeV^{-1}$)',fontsize=20)
ax.tick_params(axis='y',labelsize=18)
ax.set_xlabel('L-shell',fontsize=20)
ax.tick_params(axis='x',labelsize=18)
ax.text(0.63, 10000, 'Inner Radiation Belt', style='italic',size=14,
        bbox={'facecolor': 'green', 'alpha': 0.8, 'pad': 10})
ax.text(3.65, 100000, 'Region of Maximum Flux', style='italic',size=14,
        bbox={'facecolor': 'gray', 'alpha': 1, 'pad': 10})
ax.text(3.75, 10000, 'Outer Radiation Belt', style='italic',size=14,
        bbox={'facecolor': 'orange', 'alpha': 1, 'pad': 10})

ax.axvspan(0.2, 2, alpha=0.5, color='green')
ax.axvspan(3, 6, alpha=0.5, color='orange')
ax.axvspan(3.9, 4.7, alpha=1, color='gray')
#plt.savefig('Media_por_bines.pdf', format='pdf')
pylab.show()




