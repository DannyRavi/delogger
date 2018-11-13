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


Fx = np.arange(0, len(Fnumber))
Fy = np.array(Fnumber)

Ex = np.arange(0, len(Enumber))
Ey = np.array(Enumber)


Ty = np.concatenate((Ey, Fy), axis=0)
# Ty = sort(Ty)
E_edge = len(Ey)
Tx = np.arange(0, len(Ty))
# Tx[:]=0
Tx[:E_edge] = 1
Tx[E_edge:] = 0
# Tx = Tx[0:len(Ty)]
# print(Fy)
# a = pd.DataFrame({ 'group' :"Full", 'value': Fx })
# b = pd.DataFrame({ 'group' :"Empty", 'value': Fy })
#! myData = { 'Empty': Ey, 'Full': Fy }
myData = {'state': Tx, 'value': Ty}
df = pd.DataFrame.from_dict(myData, orient='index')
df = df.transpose()

# Usual boxplot
ax = sb.boxplot(x='state', y='value', data=df)


ax = sb.stripplot(x='state', y='value', data=df,
                  color="red", jitter=0.2, size=2.5)

plt.title("Boxplot with jitter", loc="left")

# sb.distplot(Fy)

# plt.show()
states = df.state
values = df.value


reng_of_train = 50


DefineNewState = []
stackPrecent = []
stackRefrence = []
Q3Empty = 0 # for lower case
Q1Full = 400 # for upper case


# [x * 0.1 for x in range(0, 10)]
for ref in range(Q3Empty,Q1Full):
  Nref = ref * 0.1
  for i in range(len(states)):
      if (values[i] >= Nref):
          DefineNewState.append(1)
      else:
          DefineNewState.append(0)
  stackPrecent.append(matchFunc(states, DefineNewState))
  stackRefrence.append(ref)
  DefineNewState = []


AllData = {'refrence': stackRefrence, 'precent': stackPrecent}
dfAllData = pd.DataFrame.from_dict(AllData, orient='index')
dfAllData = dfAllData.transpose()
dfAllData.to_csv('dfAllData.csv')

print(dfAllData)
maxAllData = max(stackPrecent)
indexOfAlldata = stackPrecent.index(maxAllData)
print(dfAllData.loc[indexOfAlldata] )
