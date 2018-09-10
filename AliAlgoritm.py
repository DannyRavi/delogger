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
treshold = 5
divide=5 #for window factor 
DataIn_Difference=5 # diference between Data 1 and data 2

eliminate_Item='22222'   #'-5'#22222
plt.close('all')



with open('970428/1250.txt',"r") as f:
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


splitX=list(split_by(Xdim,divide))
splitY=list(split_by(Ydim,divide))
splitZ=list(split_by(Zdim,divide))
# print("b=",len(splitX))

medianDownsampleX=normalize(splitX,divide)
medianDownsampleY=normalize(splitY,divide)
medianDownsampleZ=normalize(splitZ,divide)
# print("Len=",len(medianDownsampleX),"medianDownsampleX=",medianDownsampleX,"medianDownsampleX[15]=",medianDownsampleX[5])

ReSampleX=ReSample(medianDownsampleX,divide)
ReSampleY=ReSample(medianDownsampleY,divide)
ReSampleZ=ReSample(medianDownsampleZ,divide)

# print("Len=",len(ReSampleX),"ReSample=",ReSampleX,"ReSampleX[15]=",ReSampleX[15])

# print("LenXdim=",len(Xdim),"Xdim=",Xdim,"Xdim[15]=",Xdim[15])


BaseLIneX=ReSampleX[15]
BaseLIneY=ReSampleY[15]
BaseLIneZ=ReSampleZ[15]
# print("ReSampleX=",len(ReSampleX),"ReSampleX=",ReSampleX,"ReSampleX[15]=",ReSampleX[15])
# print(BaseLIneX)

OutX=AliAlgoritms(BaseLIneX,treshold,ReSampleX,DataIn_Difference)
OutY=AliAlgoritms(BaseLIneY,treshold,ReSampleY,DataIn_Difference)   
OutZ=AliAlgoritms(BaseLIneZ,treshold,ReSampleZ,DataIn_Difference)     

        
        
    #     for i in range(0,len(Xdim)-5):

    # Temp=(abs(Xdim[i]-Xdim[i+5]))
    # DisCh=abs(Temp-BaseLIneX)
    # if(DisCh<treshold):
    #     BaseLIneX=Temp
    #     xcc.append(0)
    # elif(DisCh>treshold):
    #     BaseLIneX=Temp
    #     state ^=1
    #     xcc.append(state)

plt.figure(1)
plt.subplot(311)
plt.plot(Xdim)
plt.title('input signal X')

plt.subplot(312)
plt.plot(Ydim)
plt.title('input signal Y')

plt.subplot(313)
plt.plot(Zdim)
plt.title('input signal Z')

plt.figure(2)
plt.subplot(311)
plt.plot(ReSampleX)
plt.title('Resample signal X')

plt.subplot(312)
plt.plot(ReSampleY)
plt.title('Resample signal Y')

plt.subplot(313)
plt.plot(ReSampleZ)
plt.title('Resample signal Z')

plt.figure(3)
plt.subplot(311)
plt.plot(OutX)
plt.title('outPut signal X')

plt.subplot(312)
plt.plot(OutY)
plt.title('outPut signal Y')



plt.subplot(313)
plt.plot(OutZ)
plt.title('outPut signal Z')

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