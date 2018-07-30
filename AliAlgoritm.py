import matplotlib.pyplot as plt
import numpy as np
from numpy import *
from scipy import integrate
from scipy import signal
from scipy.signal import lfilter, lfilter_zi, filtfilt, butter
from numpy import linalg as LA
from  dimes import *
from  Filtering import *
from  ANNC import *


medianDownsampleX=[]
medianDownsampleY=[]
medianDownsampleZ=[]

ReSampleX=[]
ReSampleY=[]
ReSampleZ=[]
treshold=5
state=1

eliminate_Item='22222'   #'-5'#22222
plt.close('all')



with open('970427/forwardStop.txt',"r") as f:
    variable=f.readlines()
#--------------------

for i in range(len(variable)):
    grades.append(variable[i].strip('\n'))
# print(grades)


newgrades = list(filter(lambda x : x != eliminate_Item, grades))
TokenDim=CreateDimen(Tokens,newgrades,steps2)
Xdim=CreateDimen1(xVector,newgrades,steps2)
Ydim=CreateDimen1(yVector,newgrades,steps2)
Zdim=CreateDimen1(zVector,newgrades,steps2)
# Irdim=CreateDimen(IrVector,newgrades,steps2)
# Tdim=CreateDimen(tVector,newgrades,steps)
ranges=len(Xdim)-10

CreateFile(Xdim,Ydim,Zdim,Tdim)


Xdim = list(map(int, Xdim))
Ydim = list(map(int, Ydim))
Zdim = list(map(int, Zdim))

Xdim = np.abs(Xdim)
Ydim = np.abs(Ydim)
Zdim = np.abs(Zdim)


ranges=len(Xdim)-10





    

# seg_length = 3
# a = range(10)
# b=[a[x:x+seg_length] for x in range(0,len(a),seg_length)]

divide=5 #for window factor 
b=list(split_by(Xdim,divide))

medianDownsampleX=normalize(Xdim,divide)
medianDownsampleX=normalize(Ydim,divide)
medianDownsampleX=normalize(Zdim,divide)


ReSampleX=ReSample(medianDownsampleX,divide)
ReSampleY=ReSample(medianDownsampleY,divide)
ReSampleY=ReSample(medianDownsampleZ,divide)

print(len(ReSampleX))
print(ReSampleX)
print("ReSampleX")
print(ReSampleX[15])

BaseLIneX=Xdim[15]
# BaseLIneX=ReSampleX[15]
# BaseLIneY=ReSampleY[15]
# BaseLIneZ=ReSampleZ[15]

print(BaseLIneX)
# xcc=[]
# for i in range(len(ReSampleX)):
#     Temp=(abs(BaseLIneX-ReSampleX[i]))
#     if((Temp-BaseLIneX)<treshold):
#         BaseLIneX=Temp
#     elif((Temp-BaseLIneX)>treshold):
#         # BaseLIneX=Temp
#         state ^=1
#         xcc.append(state)

xcc=[]

for i in range(0,len(Xdim)-5):

    Temp=(abs(Xdim[i]-Xdim[i+5]))
    DisCh=abs(Temp-BaseLIneX)
    if(DisCh<treshold):
        BaseLIneX=Temp
        xcc.append(0)
    elif(DisCh>treshold):
        BaseLIneX=Temp
        state ^=1
        xcc.append(state)

plt.figure(1)
plt.subplot(311)
plt.plot(ReSampleX)


plt.subplot(312)
plt.plot(Xdim)
plt.title('Real signal')

plt.subplot(313)
plt.plot(xcc)
plt.title('sig')


plt.show()
plt.close('all')


def PrintDataDiscreate():
    # print("allItem=>\n")
    # print(newgrades)
    # print("\n \n")
    print("token=>\n")
    print(CreateDimen1(Tokens,newgrades,steps2))
    print("\n \n")
    print("X=>\n")
    print(CreateDimen1(xVector,newgrades,steps2))
    print("\n \n")
    # print("Y=>\n")
    # print(CreateDimen(yVector,newgrades,steps))
    # print("\n \n")
    # print("Z=>\n")
    # print(CreateDimen(zVector,newgrades,steps))
    # print("\n \n")
    # print("t=>\n")
    # print(CreateDimen(tVector,newgrades,steps))

# PrintDataDiscreate()