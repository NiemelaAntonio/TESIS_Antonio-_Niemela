#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 19:46:21 2019

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
bines=np.linspace(1,7,31)+0.1
a=np.random.random_sample(100000)
b=np.random.random_sample(100000)
c=np.random.random_sample(100000)
d=np.random.random_sample(100000)
#bins=np.linspace(0,1,21)
histinfo_a,bines_a=np.histogram(a,bins='auto')
histinfo_b,bines_b=np.histogram(b,bins='auto')
histinfo_c,bines_c=np.histogram(c,bins='auto')
histinfo_d,bines_d=np.histogram(d,bins='auto')
#Armo la matriz grande
Matriz_Grande=np.empty([7,len(bines),len(bines_a),len(histinfo_a)])
Matriz_Grande[0,0,0,:]=histinfo_a
Matriz_Grande[0,0,:,0]=bines_a

