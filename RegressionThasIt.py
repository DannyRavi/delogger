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
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import linear_model


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

# Tx = Fy * Ey
Ty = np.concatenate((Ey, Fy), axis=0)
# Ty = sort(Ty)
E_edge = len(Ey)
Tx = np.arange(0, len(Ty))
# Tx[:]=0
Tx[:E_edge]=0
Tx[E_edge:]=1
# Tx = Tx[0:len(Ty)]
# print(Fy)
# a = pd.DataFrame({ 'group' :"Full", 'value': Fx })
# b = pd.DataFrame({ 'group' :"Empty", 'value': Fy })
#! myData = { 'Empty': Ey, 'Full': Fy }
myData = { 'number': Tx  , 'alld': Ty  }
df = pd.DataFrame.from_dict(myData, orient='index')
df = df.transpose()
# df = df.fillna(0)

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
# Tx = Tx.reshape(-1,1)
# Ty = Ty.reshape(-1,1)


ys = df.number
xs = df.alld
xs= np.array(df.iloc[:, 1:2]) 	# end index is exclusive
ys= np.array(df.iloc[:, 0:1]) 

#todo from sklearn import svm
#todo clf = svm.SVC(kernel='linear', C = 1.0)
#todo clf.fit(xs,ys)
#todo test = np.array([0.58])
#todo test = test.reshape(1, -1)
# print(clf.predict(test)) 
# df = pd.DataFrame(list(df.all()))
# ys = df.iloc[-1:]     
# ys = ys.values.reshape(1,-1)  # sliced it here
# xs.array.reshape(1, -1)
# ys.array.reshape(1, -1)





dummy_data = (np.arange(60.0))
# start = 0
# stop  = 50
# incr = 0.5
# eps = 1e-3*(stop-start)
# num = int((stop-start)/(incr-eps)+1)
# dummy_data = np.linspace(start, stop,num)


print(dummy_data)
dummy_data = dummy_data.reshape(-1,1)
dummy_data = dummy_data

#! x_train, x_test ,y_train, y_test= train_test_split(xs, ys, test_size = 200, random_state=42)
#! # ─── SD ───────────
#! reg = LinearRegression()
#! reg.fit(x_train, y_train)
#! y_pred = reg.predict(x_test)
#! plt.scatter(x_test, y_pred)
#! plt.plot()
#! plt.show()
#! ─── SD ───────────


# ─── DD ──────────────────────────────────
# reg = LinearRegression()
# reg.fit(xs,ys)
# yhat = reg.predict(dummy_data)
# plt.scatter(xs,ys)
# plt.plot(dummy_data,yhat)
# plt.show()
# ─── DD ──────────────────────────────────
# ─── LOGSTIC ───────────────────────

# Fit the classifier
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
# X, y = load_iris(return_X_y=True)
clf = LogisticRegression(random_state=0, solver='lbfgs',multi_class='multinomial').fit(xs, ys)
yhat = clf.predict(dummy_data)
plt.scatter(xs,ys)
ess = clf.predict_proba(dummy_data) 
plt.plot(dummy_data,yhat)
plt.show()
lin = clf.score(xs, ys)
print("es",ess)
print("refLine",lin )
# plt.plot(xx,xs)
# plt.show()
# ─── LOGSTIC ────────────────────────────

# xs = df.Empy
# ys = df.Full
# xs = df.Full

# plt.scatter(xs, ys,  c=labels)
# plt.scatter(xs,ys,  cmap='rainbow')  
# plt.scatter(centroids[:,0],centroids[:,1],marker='x',s=150,alpha=0.5)
# plt.scatter(centroids[:,0],centroids[:,2],marker='x',s=150,alpha=0.5)
# plt.show()





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

# Plotting along with  Centroids
#!plt.scatter(f1, f2, c='#050505', s=7)
#!plt.scatter(C_x, C_y, marker='*', s=200, c='g')
#!
#!plt.show()
