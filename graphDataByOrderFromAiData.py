import matplotlib.pyplot as plt
import numpy as np
from ForDebudLibrary import *
from cursor import *
from numpy import *
from scipy import integrate
from numpy import linalg as LA
import os
from scipy.signal import lfilter, lfilter_zi, filtfilt, butter
from matplotlib.widgets import Cursor
# from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn import datasets
import pandas as pd
import seaborn as sb
import csv
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

grades = []
grades2 = []
TokenDim = []
Xdim = []
Ydim = []
Zdim = []
Tdim = []
Angpi = []
distance = []
results = []
ReConstruct = []
ReConstruct2 = []
counter = 0
divide = 25
final = []
minArrayd = 0.0
StChange = 0
StChange2 = 0
ArStateChange = []
ArStateChange2 = []
NumberFualt = 0.0
numberExe = 0


plt.close('all')

all_files = os.listdir("BigData")

Len_all_files = len(all_files)


for numberCounter in range(Len_all_files):
    Read_selected_files = all_files[numberCounter]

    Read_selected_files = str(Read_selected_files)

    with open('BigData/' + Read_selected_files, "r") as f:
        variable = f.readlines()
    # --------------------

    for i in range(len(variable)):
        grades.append(variable[i].strip('\n'))

    for i in range(len(grades)):
        mini_size = len(grades[i].split(','))
        for ii in range(mini_size):
            sd = grades[i].split(',')
            ReConstruct.append(sd[ii])

    if(numberExe == 0):
        Fnumber = list(map(float, ReConstruct))
        numberExe = 1
    else:
        Enumber = list(map(float, ReConstruct))

    grades = []
    TokenDim = []
    Angpi = []
    distance = []
    results = []
    ReConstruct = []
    algoritm_detect = []


Fx = np.arange(1, len(Fnumber)+1)
Fy = np.array(Fnumber)

Ex = np.arange(1, len(Enumber)+1)
Ey = np.array(Enumber)


a = pd.DataFrame({ 'group' :"Full", 'value': Fx })
b = pd.DataFrame({ 'group' :"Empty", 'value': Fy })

df=a.append(b)
 
# Usual boxplot
ax = sb.boxplot(x='group', y='value', data=df)


ax = sb.stripplot(x='group', y='value', data=df, color="red", jitter=0.2, size=2.5)

plt.title("Boxplot with jitter", loc="left")

# sb.distplot(Fy)

plt.show()
