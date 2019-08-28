#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 17:13:55 2019

@author: tony
"""


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
FESA_Bineado_2012=np.load('FESA_Bineado_2012.npy')[0,:,:]
t_2012=np.load(pathdatos+str('DATOS_2012_SIN_BINEAR/t_pegados_2012.npy'))
L_sin_binear_2012=np.load(pathdatos+str('DATOS_2012_SIN_BINEAR/L_pegados_2012.npy'))
Fesa_2012=np.load(pathdatos+str('DATOS_2012_SIN_BINEAR/FESA_pegados.npy'))
'''
FESA_Bineado_2013=np.load('FESA_Bineado_2013.npy')[0,:,:]
t_2013=np.load(pathdatos+str('DATOS_2013_SIN_BINEAR/t_pegados_2013.npy'))
L_sin_binear_2013=np.load(pathdatos+str('DATOS_2013_SIN_BINEAR/L_pegados_2013.npy'))
Fesa_2013=np.load(pathdatos+str('DATOS_2013_SIN_BINEAR/FESA_pegados.npy'))

FESA_Bineado_2014=np.load('FESA_Bineado_2014.npy')[0,:,:]
t_2014=np.load(pathdatos+str('DATOS_2014_SIN_BINEAR/t_pegados_2014.npy'))
L_sin_binear_2014=np.load(pathdatos+str('DATOS_2014_SIN_BINEAR/L_pegados_2014.npy'))
Fesa_2014=np.load(pathdatos+str('DATOS_2014_SIN_BINEAR/FESA_pegados.npy'))

FESA_Bineado_2015=np.load('FESA_Bineado_2015.npy')[0,:,:]
t_2015=np.load(pathdatos+str('DATOS_2015_SIN_BINEAR/t_pegados_2015.npy'))
L_sin_binear_2015=np.load(pathdatos+str('DATOS_2015_SIN_BINEAR/L_pegados_2015.npy'))
Fesa_2015=np.load(pathdatos+str('DATOS_2015_SIN_BINEAR/FESA_pegados.npy'))

FESA_Bineado_2016=np.load('FESA_Bineado_2016.npy')[0,:,:]
t_2016=np.load(pathdatos+str('DATOS_2016_SIN_BINEAR/t_pegados_2016.npy'))
L_sin_binear_2016=np.load(pathdatos+str('DATOS_2016_SIN_BINEAR/L_pegados_2016.npy'))
Fesa_2016=np.load(pathdatos+str('DATOS_2016_SIN_BINEAR/FESA_pegados.npy'))

FESA_Bineado_2017=np.load('FESA_Bineado_2017.npy')[0,:,:]
t_2017=np.load(pathdatos+str('DATOS_2017_SIN_BINEAR/t_pegados_2017.npy'))
L_sin_binear_2017=np.load(pathdatos+str('DATOS_2017_SIN_BINEAR/L_pegados_2017.npy'))
Fesa_2017=np.load(pathdatos+str('DATOS_2017_SIN_BINEAR/FESA_pegados.npy'))

FESA_Bineado_2018=np.load('FESA_Bineado_2018.npy')[0,:,:]
t_2018=np.load(pathdatos+str('DATOS_2018_SIN_BINEAR/t_pegados_2018.npy'))
L_sin_binear_2018=np.load(pathdatos+str('DATOS_2018_SIN_BINEAR/L_pegados_2018.npy'))
Fesa_2018=np.load(pathdatos+str('DATOS_2018_SIN_BINEAR/FESA_pegados.npy'))
'''

Hora_entera=datetime.timedelta(seconds=3600)
print(Hora_entera)
j=0
i=0
Memoria=[]
for i in range(len(t_2012)-1):
    if t_2012[i]-t_2012[j]>Hora_entera==True:
        print('Si')











