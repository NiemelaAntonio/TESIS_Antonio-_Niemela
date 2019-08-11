#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 14:45:55 2019

@author: tony
"""

from scipy import stats
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

N_points = 100000
n_bins = 20
bines=np.linspace(1,7,31)+0.1
DATOS_Completos=np.load('/media/tony/TOSHIBAEXT/TESIS/DATOS_BINEADOS/DATOS/FESA_BINARIO/FESA_Bineado_2012.npy')
DATOS_Completos[DATOS_Completos==0]=['nan']
# Cosas para hacer el histograma
x_0 = np.log10(DATOS_Completos[:,0])
x_0_mean=np.nanmean(np.log10(DATOS_Completos[:,0]))
x_0_median=np.nanmedian(np.log10(DATOS_Completos[:,0]))
x_1 = np.log10(DATOS_Completos[:,1])
x_1_mean=np.nanmean(np.log10(DATOS_Completos[:,1]))
x_1_median=np.nanmedian(np.log10(DATOS_Completos[:,1]))
x_2 = np.log10(DATOS_Completos[:,2])
x_2_mean=np.nanmean(np.log10(DATOS_Completos[:,2]))
x_2_median=np.nanmedian(np.log10(DATOS_Completos[:,2]))
x_3 = np.log10(DATOS_Completos[:,3])
x_3_mean=np.nanmean(np.log10(DATOS_Completos[:,3]))
x_3_median=np.nanmedian(np.log10(DATOS_Completos[:,3]))
x_4 = np.log10(DATOS_Completos[:,4])
x_4_mean=np.nanmean(np.log10(DATOS_Completos[:,4]))
x_4_median=np.nanmedian(np.log10(DATOS_Completos[:,4]))
x_5 = np.log10(DATOS_Completos[:,5])
x_5_mean=np.nanmean(np.log10(DATOS_Completos[:,5]))
x_5_median=np.nanmedian(np.log10(DATOS_Completos[:,5]))
x_6 = np.log10(DATOS_Completos[:,6])
x_6_mean=np.nanmean(np.log10(DATOS_Completos[:,6]))
x_6_median=np.nanmedian(np.log10(DATOS_Completos[:,6]))
x_7 = np.log10(DATOS_Completos[:,7])
x_7_mean=np.nanmean(np.log10(DATOS_Completos[:,7]))
x_7_median=np.nanmedian(np.log10(DATOS_Completos[:,7]))
x_8 = np.log10(DATOS_Completos[:,8])
x_8_mean=np.nanmean(np.log10(DATOS_Completos[:,8]))
x_8_median=np.nanmedian(np.log10(DATOS_Completos[:,8]))
x_9 = np.log10(DATOS_Completos[:,9])
x_9_mean=np.nanmean(np.log10(DATOS_Completos[:,9]))
x_9_median=np.nanmedian(np.log10(DATOS_Completos[:,9]))
x_10 = np.log10(DATOS_Completos[:,10])
x_10_mean=np.nanmean(np.log10(DATOS_Completos[:,10]))
x_10_median=np.nanmedian(np.log10(DATOS_Completos[:,10]))
x_11 = np.log10(DATOS_Completos[:,11])
x_11_mean=np.nanmean(np.log10(DATOS_Completos[:,11]))
x_11_median=np.nanmedian(np.log10(DATOS_Completos[:,11]))
x_12 = np.log10(DATOS_Completos[:,12])
x_12_mean=np.nanmean(np.log10(DATOS_Completos[:,12]))
x_12_median=np.nanmedian(np.log10(DATOS_Completos[:,12]))
x_13 = np.log10(DATOS_Completos[:,13])
x_13_mean=np.nanmean(np.log10(DATOS_Completos[:,13]))
x_13_median=np.nanmedian(np.log10(DATOS_Completos[:,13]))
x_14 = np.log10(DATOS_Completos[:,14])
x_14_mean=np.nanmean(np.log10(DATOS_Completos[:,14]))
x_14_median=np.nanmedian(np.log10(DATOS_Completos[:,14]))
x_15 = np.log10(DATOS_Completos[:,15])
x_15_mean=np.nanmean(np.log10(DATOS_Completos[:,15]))
x_15_median=np.nanmedian(np.log10(DATOS_Completos[:,15]))
x_16 = np.log10(DATOS_Completos[:,16])
x_16_mean=np.nanmean(np.log10(DATOS_Completos[:,16]))
x_16_median=np.nanmedian(np.log10(DATOS_Completos[:,16]))
x_17 = np.log10(DATOS_Completos[:,17])
x_17_mean=np.nanmean(np.log10(DATOS_Completos[:,17]))
x_17_median=np.nanmedian(np.log10(DATOS_Completos[:,17]))
x_18 = np.log10(DATOS_Completos[:,18])
x_18_mean=np.nanmean(np.log10(DATOS_Completos[:,18]))
x_18_median=np.nanmedian(np.log10(DATOS_Completos[:,18]))
x_19 = np.log10(DATOS_Completos[:,19])
x_19_mean=np.nanmean(np.log10(DATOS_Completos[:,19]))
x_19_median=np.nanmedian(np.log10(DATOS_Completos[:,19]))
x_20 = np.log10(DATOS_Completos[:,20])
x_20_mean=np.nanmean(np.log10(DATOS_Completos[:,20]))
x_20_median=np.nanmedian(np.log10(DATOS_Completos[:,20]))
x_21 = np.log10(DATOS_Completos[:,21])
x_21_mean=np.nanmean(np.log10(DATOS_Completos[:,21]))
x_21_median=np.nanmedian(np.log10(DATOS_Completos[:,21]))
x_22 = np.log10(DATOS_Completos[:,22])
x_22_mean=np.nanmean(np.log10(DATOS_Completos[:,22]))
x_22_median=np.nanmedian(np.log10(DATOS_Completos[:,22]))
x_23 = np.log10(DATOS_Completos[:,23])
x_23_mean=np.nanmean(np.log10(DATOS_Completos[:,23]))
x_23_median=np.nanmedian(np.log10(DATOS_Completos[:,23]))
x_24 = np.log10(DATOS_Completos[:,24])
x_24_mean=np.nanmean(np.log10(DATOS_Completos[:,24]))
x_24_median=np.nanmedian(np.log10(DATOS_Completos[:,24]))
x_25 = np.log10(DATOS_Completos[:,25])
x_25_mean=np.nanmean(np.log10(DATOS_Completos[:,25]))
x_25_median=np.nanmedian(np.log10(DATOS_Completos[:,25]))
x_26 = np.log10(DATOS_Completos[:,26])
x_26_mean=np.nanmean(np.log10(DATOS_Completos[:,26]))
x_26_median=np.nanmedian(np.log10(DATOS_Completos[:,26]))
x_27 = np.log10(DATOS_Completos[:,27])
x_27_mean=np.nanmean(np.log10(DATOS_Completos[:,27]))
x_27_median=np.nanmedian(np.log10(DATOS_Completos[:,27]))
x_28 = np.log10(DATOS_Completos[:,28])
x_28_mean=np.nanmean(np.log10(DATOS_Completos[:,28]))
x_28_median=np.nanmedian(np.log10(DATOS_Completos[:,28]))
x_29 = np.log10(DATOS_Completos[:,29])
x_29_mean=np.nanmean(np.log10(DATOS_Completos[:,29]))
x_29_median=np.nanmedian(np.log10(DATOS_Completos[:,29]))
x_30 = np.log10(DATOS_Completos[:,30])
x_30_mean=np.nanmean(np.log10(DATOS_Completos[:,30]))
x_30_median=np.nanmedian(np.log10(DATOS_Completos[:,30]))

fig, axs = plt.subplots(5, 6,sharey=False, sharex=True, constrained_layout=True)
fig.suptitle('Histogramas por Bines para el año 2012',fontsize=24)
fig.set_size_inches(28.5, 20.5)

# We can set the number of bins with the `bins` kwarg
axs[0][0].hist(x_0[~np.isnan(x_0)], bins=10)
axs[0][0].axvline(x_0_mean, color='b', linestyle='dashed', linewidth=1)
axs[0][0].axvline(x_0_median, color='r', linestyle='-', linewidth=1)
#axs[0][0].legend(['media:'+str(round(a[0][0],3)),'mediana:'+str(round(a[0][1],3))])
axs[0][0].set_title(str(np.round(bines[0],2)))
axs[0][0].set_ylabel('Frecuencia')
axs[0][0].set_xlabel('Flujo()')
#axs[0][0].set_xscale('symlog')
axs[0][1].hist(x_1[~np.isnan(x_1)], bins=10)
axs[0][1].set_title(str(np.round(bines[1],2)))
axs[0][1].set_ylabel('Frecuencia')
axs[0][1].set_xlabel('Flujo()')
#axs[0][1].set_xscale('symlog')
axs[0][2].hist(x_2[~np.isnan(x_2)],bins=10)
axs[0][2].set_title(str(np.round(bines[2],2)))
axs[0][2].set_ylabel('Frecuencia')
axs[0][2].set_xlabel('Flujo()')
#axs[0][2].set_xscale('symlog')
axs[0][3].hist(x_3[~np.isnan(x_3)],bins=10)
axs[0][3].set_title(str(np.round(bines[3],2)))
axs[0][3].set_ylabel('Frecuencia')
axs[0][3].set_xlabel('Flujo()')
#axs[0][3].set_xscale('symlog')
axs[0][4].hist(x_4[~np.isnan(x_4)],bins=10)
axs[0][4].set_title(str(np.round(bines[4],2)))
axs[0][4].set_ylabel('Frecuencia')
axs[0][4].set_xlabel('Flujo()')
#axs[0][4].set_xscale('symlog')
axs[0][5].hist(x_5[~np.isnan(x_5)],bins=10)
axs[0][5].set_title(str(np.round(bines[5],2)))
axs[0][5].set_ylabel('Frecuencia')
axs[0][5].set_xlabel('Flujo()')
#axs[0][5].set_xscale('symlog')

axs[1][0].hist(x_6[~np.isnan(x_6)], bins=10)
axs[1][0].set_title(str(np.round(bines[6],2)))
axs[1][0].set_ylabel('Frecuencia')
axs[1][0].set_xlabel('Flujo()')
#axs[1][0].set_xscale('symlog')
axs[1][1].hist(x_7[~np.isnan(x_7)], bins=10)
axs[1][1].set_title(str(np.round(bines[7],2)))
axs[1][1].set_ylabel('Frecuencia')
axs[1][1].set_xlabel('Flujo()')
#axs[1][1].set_xscale('symlog')
axs[1][2].hist(x_8[~np.isnan(x_8)],bins=10)
axs[1][2].set_title(str(np.round(bines[8],2)))
axs[1][2].set_ylabel('Frecuencia')
axs[1][2].set_xlabel('Flujo()')
#axs[1][2].set_xscale('symlog')
axs[1][3].hist(x_9[~np.isnan(x_9)],bins=10)
axs[1][3].set_title(str(np.round(bines[9],2)))
axs[1][3].set_ylabel('Frecuencia')
axs[1][3].set_xlabel('Flujo()')
#axs[1][3].set_xscale('symlog')
axs[1][4].hist(x_10[~np.isnan(x_10)],bins=10)
axs[1][4].set_title(str(np.round(bines[10],2)))
axs[1][4].set_ylabel('Frecuencia')
axs[1][4].set_xlabel('Flujo()')
#axs[1][4].set_xscale('symlog')
axs[1][5].hist(x_11[~np.isnan(x_11)],bins=10)
axs[1][5].set_title(str(np.round(bines[11],2)))
axs[1][5].set_ylabel('Frecuencia')
axs[1][5].set_xlabel('Flujo()')
#axs[1][5].set_xscale('symlog')

axs[2][0].hist(x_12[~np.isnan(x_12)], bins=10)
axs[2][0].set_title(str(np.round(bines[12],2)))
axs[2][0].set_ylabel('Frecuencia')
axs[2][0].set_xlabel('Flujo()')
#axs[2][0].set_xscale('symlog')
axs[2][1].hist(x_13[~np.isnan(x_13)], bins=10)
axs[2][1].set_title(str(np.round(bines[13],2)))
axs[2][1].set_ylabel('Frecuencia')
axs[2][1].set_xlabel('Flujo()')
#axs[2][1].set_xscale('symlog')
axs[2][2].hist(x_14[~np.isnan(x_14)],bins=10)
axs[2][2].set_title(str(np.round(bines[14],2)))
axs[2][2].set_ylabel('Frecuencia')
axs[2][2].set_xlabel('Flujo()')
#axs[2][2].set_xscale('symlog')
axs[2][3].hist(x_15[~np.isnan(x_15)],bins=10)
axs[2][3].set_title(str(np.round(bines[15],2)))
axs[2][3].set_ylabel('Frecuencia')
axs[2][3].set_xlabel('Flujo()')
#axs[2][3].set_xscale('symlog')
axs[2][4].hist(x_16[~np.isnan(x_16)],bins=10)
axs[2][4].set_title(str(np.round(bines[16],2)))
axs[2][4].set_ylabel('Frecuencia')
axs[2][4].set_xlabel('Flujo()')
#axs[2][4].set_xscale('symlog')
axs[2][5].hist(x_17[~np.isnan(x_17)],bins=10)
axs[2][5].set_title(str(np.round(bines[17],2)))
axs[2][5].set_ylabel('Frecuencia')
axs[2][5].set_xlabel('Flujo()')
#axs[2][5].set_xscale('symlog')

axs[3][0].hist(x_18[~np.isnan(x_18)], bins=10)
axs[3][0].set_title(str(np.round(bines[18],2)))
axs[3][0].set_ylabel('Frecuencia')
axs[3][0].set_xlabel('Flujo()')
#axs[3][0].set_xscale('symlog')
axs[3][1].hist(x_19[~np.isnan(x_19)], bins=10)
axs[3][1].set_title(str(np.round(bines[19],2)))
axs[3][1].set_ylabel('Frecuencia')
axs[3][1].set_xlabel('Flujo()')
#axs[3][1].set_xscale('symlog')
axs[3][2].hist(x_20[~np.isnan(x_20)],bins=10)
axs[3][2].set_title(str(np.round(bines[20],2)))
axs[3][2].set_ylabel('Frecuencia')
axs[3][2].set_xlabel('Flujo()')
#axs[3][2].set_xscale('symlog')
axs[3][3].hist(x_21[~np.isnan(x_21)],bins=10)
axs[3][3].set_title(str(np.round(bines[21],2)))
axs[3][3].set_ylabel('Frecuencia')
axs[3][3].set_xlabel('Flujo()')
#axs[3][3].set_xscale('symlog')
axs[3][4].hist(x_22[~np.isnan(x_22)],bins=10)
axs[3][4].set_title(str(np.round(bines[22],2)))
axs[3][4].set_ylabel('Frecuencia')
axs[3][4].set_xlabel('Flujo()')
#axs[3][4].set_xscale('symlog')
axs[3][5].hist(x_23[~np.isnan(x_23)],bins=10)
axs[3][5].set_title(str(np.round(bines[23],2)))
axs[3][5].set_ylabel('Frecuencia')
axs[3][5].set_xlabel('Flujo()')
#axs[3][5].set_xscale('symlog')

axs[4][0].hist(x_24[~np.isnan(x_24)], bins=10)
axs[4][0].set_title(str(np.round(bines[24],2)))
axs[4][0].set_ylabel('Frecuencia')
axs[4][0].set_xlabel('Flujo()')
#axs[4][0].set_xscale('symlog')
axs[4][1].hist(x_25[~np.isnan(x_25)], bins=10)
axs[4][1].set_title(str(np.round(bines[25],2)))
axs[4][1].set_ylabel('Frecuencia')
axs[4][1].set_xlabel('Flujo()')
#axs[4][1].set_xscale('symlog')
axs[4][2].hist(x_26[~np.isnan(x_26)],bins=10)
axs[4][2].set_title(str(np.round(bines[26],2)))
axs[4][2].set_ylabel('Frecuencia')
axs[4][2].set_xlabel('Flujo()')
#axs[4][2].set_xscale('symlog')
axs[4][3].hist(x_27[~np.isnan(x_27)],bins=10)
axs[4][3].set_title(str(np.round(bines[27],2)))
axs[4][3].set_ylabel('Frecuencia')
axs[4][3].set_xlabel('Flujo()')
#axs[4][3].set_xscale('symlog')
axs[4][4].hist(x_28[~np.isnan(x_28)],bins=10)
axs[4][4].set_title(str(np.round(bines[28],2)))
axs[4][4].set_ylabel('Frecuencia')
axs[4][4].set_xlabel('Flujo()')
#axs[4][4].set_xscale('symlog')
axs[4][5].hist(x_29[~np.isnan(x_29)],bins=10)
axs[4][5].set_title(str(np.round(bines[29],2)))
axs[4][5].set_ylabel('Frecuencia')
axs[4][5].set_xlabel('Flujo()')
#axs[4][5].set_xscale('symlog')
plt.show()















































































