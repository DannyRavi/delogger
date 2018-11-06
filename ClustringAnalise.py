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
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn import datasets
import pandas as pd
import seaborn as sb
from sklearn.cluster import DBSCAN
from sklearn.cluster import KMeans

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


Ex = np.arange(1, len(Fnumber)+1)
Ey = np.array(Fnumber)

Fx = np.arange(1, len(Enumber)+1)
Fy = np.array(Enumber)
Fy = Fy[0:len(Ey)]
print(Fy)
# a = pd.DataFrame({ 'group' :"Full", 'value': Fx })
# b = pd.DataFrame({ 'group' :"Empty", 'value': Fy })
myData = { 'Empty': Ey, 'Full': Fy }
df = pd.DataFrame.from_dict(myData, orient='index')
df = df.transpose()
# a = {'Links' : lines ,'Titles' : titles , 'Singers': finalsingers , 'Albums':finalalbums , 'Years' : years}
# df = pd.DataFrame.from_dict(a, orient='index')
# df.transpose()




 
# Usual boxplot
# ax = sb.boxplot(x='group', y='value', data=df)


# ax = sb.stripplot(x='group', y='value', data=df, color="red", jitter=0.2, size=2.5)

# plt.title("Boxplot with jitter", loc="left")
print(df)
# sb.distplot(Fy)
# dbscan = DBSCAN()
# dbscan.fit(df)
# labels = dbscan.labels_
# xx = 'group'
# yy = 'value'
# plt.scatter(xx,yy, c=labels)
# plt.show()
# print(df.group)
# print(df.group)
# Fx = Fx.reshape(-1,1)
# Fy = Fy.reshape(-1,1)
kmn = KMeans(n_clusters=3)
kmn.fit(df)
labels = kmn.predict(df)
xs = df.Empty
ys = df.Full

centroids = kmn.cluster_centers_
plt.scatter( xs, ys, c=labels)
# plt.scatter(centroids[:,0],centroids[:,2],marker='x',s=150,alpha=0.5)
plt.show()

#! f2 = df['Empty'].values
#! f1 = df['Full'].values
#! X = np.array(list(zip(f1, f2)))
#! plt.scatter(f1, f2, c='black', s=7)
#! plt.show()
#! plt.close()

# Euclidean Distance Caculator
#! def dist(a, b, ax=1):
#!     return np.linalg.norm(a - b, axis=ax)
# Number of clusters
#! k = 3
# X coordinates of random centroids
#! C_x = np.random.randint(0, np.max(X)-20, size=k)
#! # Y coordinates of random centroids
#! C_y = np.random.randint(0, np.max(X)-20, size=k)
#! C = np.array(list(zip(C_x, C_y)), dtype=np.float32)

# Plotting along with the Centroids
#!plt.scatter(f1, f2, c='#050505', s=7)
#!plt.scatter(C_x, C_y, marker='*', s=200, c='g')
#!
#!plt.show()
