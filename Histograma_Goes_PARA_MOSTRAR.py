#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 15:49:54 2019

@author: tony
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
from scipy.stats import norm

pathdatos='/media/tony/TOSHIBAEXT/TESIS/GOES/DATOS_CORTADOS/'
Datos_Goes_E2E=np.load(pathdatos+str('Datos_GOES_E2E.npy'))
Datos_Goes_E2W=np.load(pathdatos+str('Datos_GOES_E2W.npy'))

    
Datos_Goes_E2E[Datos_Goes_E2E[:,1] == -99999]=np.nan
Datos_E2E=Datos_Goes_E2E[:,1]
mu1, std1 = norm.fit(np.log10(Datos_E2E[~np.isnan(Datos_E2E)]))
Datos_E2E=np.ma.masked_invalid(Datos_E2E)
Datos_Goes_E2E[:,1]=np.log10(Datos_Goes_E2E[:,1])
Datos_Goes_E2E=np.ma.masked_invalid(Datos_Goes_E2E)
'''
fig, axs = plt.subplots(constrained_layout=True)
fig.suptitle('PARA E2E sin log10',fontsize=18)
#fig.set_size_inches(10.5, 18.5)
axs.hist(Datos_E2E)
axs.set_ylabel('Frecuency')
axs.set_xlabel('Flux')
plt.show()

fig, axs = plt.subplots(constrained_layout=True)
fig.suptitle('PARA E2E',fontsize=18)
#fig.set_size_inches(10.5, 18.5)
axs.hist(Datos_Goes_E2E[:,1])
axs.set_ylabel('Frecuency')
axs.set_xlabel('log10(Flux)')
ax2 = axs.twinx()
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu1, std1)
plt.plot(x, p, 'k', linewidth=2)
ax2.axes.get_yaxis().set_visible(False)
title = "Fit results: mu = %.2f,  std = %.2f" % (mu1, std1)
plt.title(title)
plt.show()
'''


Datos_Goes_E2W[Datos_Goes_E2W[:,1] == -99999]=np.nan
Datos_E2W=Datos_Goes_E2W[:,1]
mu2, std2 = norm.fit(np.log10(Datos_E2W[~np.isnan(Datos_E2W)]))
Datos_E2W=np.ma.masked_invalid(Datos_E2W)
Datos_Goes_E2W[:,1]=np.log10(Datos_Goes_E2W[:,1])
Datos_Goes_E2W=np.ma.masked_invalid(Datos_Goes_E2W)
x_0_media=np.nanmean(np.log10(Datos_E2W))
'''
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
'''

fig, axs = plt.subplots(constrained_layout=True)
fig.set_size_inches(12, 10)
axs.hist(Datos_Goes_E2W[:,1])
axs.set_ylabel('Frecuency',fontsize=24)
axs.set_xlabel(r'log$_{10}$(Monthly Mean Flux)',fontsize=24)
plt.tick_params(axis='x',labelsize=20)
plt.tick_params(axis='y',labelsize=20)
axs.text(3.65, 400000, r'$\mathcal{N}(\mu = 2.94 , \sigma =0.84)$', fontsize=30)
axs.axvline(x_0_media, color='r', linestyle='-', linewidth=1)
ax2 = axs.twinx()
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu2, std2)
plt.plot(x, p, 'k', linewidth=2)
ax2.axes.get_yaxis().set_visible(False)
plt.savefig('histograma_GOES.pdf', format='pdf')
plt.show()



