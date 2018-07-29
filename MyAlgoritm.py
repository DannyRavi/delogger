import matplotlib.pyplot as plt
import numpy as np
from numpy import *
from scipy import integrate
from scipy import signal
from scipy.signal import lfilter, lfilter_zi, filtfilt, butter
from numpy import linalg as LA
from  dimes import *
from  ANNC import *



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
# Irdim= list(map(int, Irdim))

#Create real data
Xdim = np.abs(Xdim)
Ydim = np.abs(Ydim)
Zdim = np.abs(Zdim)
# Irdim= np.abs(Irdim)

#deraivate of real data
DXdim = np.diff(Xdim)
DYdim = np.diff(Ydim)
DZdim = np.diff(Zdim)

#Integral of Diff
IDXdim = Integ(DXdim)
IDYdim = Integ(DYdim)
IDZdim = Integ(DZdim)


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



def filters():
    b, a = butter(4, 0.1,analog=False)

    # Apply the filter to xn.  Use lfilter_zi to choose the initial condition
    # of the filter.
    zi = lfilter_zi(b, a)
    z, _ = lfilter(b, a, IDXdim, zi=zi*IDXdim[0])

    # Apply the filter again, to have a result filtered at an order
    # the same as filtfilt.
    z2, _ = lfilter(b, a, z, zi=zi*z[0])

    # Use filtfilt to apply the filter.
    yy = filtfilt(b, a, IDXdim)

    yy=abs(yy)
    return yy

p = Perceptron(3, np.array([0.02, 0.02,0.02]))
# for absolute
absIDXdim=np.abs(IDXdim)
absIDYdim=np.abs(IDYdim)
absIDZdim=np.abs(IDZdim)
# for convert list to array
ArrayabsIDXdim=np.vstack(absIDXdim)
ArrayabsIDYdim=np.vstack(absIDYdim)
ArrayabsIDZdim=np.vstack(absIDZdim)




def AnnExecute(r):
    p=r
    xxm=[]
    OutY=[]
    for x in range(ranges):
        xxm.append([ArrayabsIDXdim[x],ArrayabsIDYdim[x],ArrayabsIDZdim[x]])
        y = p(xxm[x])
        OutY.append(y)
    return OutY
   



AnnExecute(p)


def ShowMyAlgortim():
    plt.figure(1)

    plt.subplot(411)
    plt.plot(Xdim)
    plt.title('Real signal')

    plt.subplot(412)
    plt.plot(DXdim)
    plt.title('diff signal')

    plt.subplot(413)
    plt.plot((IDXdim))
    plt.title('integral signal')

    plt.subplot(414)
    plt.plot(np.abs(IDXdim))
    plt.title('abs signal')
    plt.xlabel('X')
    # plt.show()
    # plt.close()

    plt.figure(2)

    plt.subplot(411)
    plt.plot(Ydim)
    plt.title('Real signal')

    plt.subplot(412)
    plt.plot(DYdim)
    plt.title('diff signal')

    plt.subplot(413)
    plt.plot((IDYdim))
    plt.title('integral signal')

    plt.subplot(414)
    plt.plot(np.abs(IDYdim))
    plt.title('abs signal')
    plt.xlabel('Y')

    plt.figure(3)

    plt.subplot(411)
    plt.plot(Zdim)
    plt.title('Real signal')

    plt.subplot(412)
    plt.plot(DZdim)
    plt.title('diff signal')

    plt.subplot(413)
    plt.plot((IDZdim))
    plt.title('integral signal')

    plt.subplot(414)
    plt.plot(np.abs(IDZdim))
    plt.title('abs signal')
    plt.xlabel('Z')

    plt.figure(4)
    plt.subplot(311)
    plt.plot(filters(), 'g-', linewidth=2, label='filtered data')
    plt.subplot(312)
    plt.plot(AnnExecute(p))
    plt.title('ANN output')
    plt.subplot(313)
    plt.plot(np.abs(Xdim))
    plt.title('Filtered signal')
    plt.xlabel('X')



    plt.show()
    plt.close('all')


ShowMyAlgortim()