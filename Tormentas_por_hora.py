#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:10:38 2019

@author: tony
"""

from spacepy import pycdf
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
import spacepy.toolbox as tb
import spacepy.time as spt
import spacepy.radbelt as sprb
from spacepy import radbelt
import spacepy.pycdf as cdf
import os
from os import listdir
from datetime import datetime
from datetime import datetime, timedelta, date, time
import matplotlib.dates as mdates
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.colors as colors

pathdatos='/media/tony/TOSHIBAEXT/TESIS/Figuras_tormentas/'
pathdatos1='/media/tony/TOSHIBAEXT/TESIS/DATOS_BINEADOS/Fraccionado_por_anio/DATOS_2018_SIN_BINEAR/'
t_Pegados=np.load(pathdatos1+str('t_pegados_2018.npy'))
t_min=t_Pegados[0]
t_max=t_Pegados[len(t_Pegados)-1]
del(t_Pegados)
x=np.load('T_tormenta_2018.npy')
y=np.load('L_tormenta_2018.npy')
y= ma.masked_where(y==min(y), y)
z=np.load('Fesa_tormenta_2018.npy')

fig,ax=plt.subplots(figsize=(40,10))
marker_size=15
plt.scatter(x, y, marker_size, c=np.log10(z),cmap='nipy_spectral')
plt.title('FESA (spin averaged electron flux) vs. L para E=')
fig.autofmt_xdate()
ax.set_xlim([t_min, t_max])
plt.xlabel("Tiempo (yyyy-mm-dd)")
plt.ylabel("L-Shell")

cbar= plt.colorbar(cmap='gist_rainbow')
cbar.set_label("Flujo log10(FESA)", labelpad=+1)
plt.show()