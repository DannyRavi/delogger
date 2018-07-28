import matplotlib.pyplot as plt
import numpy as np
from  dimes import *
from numpy import *
from scipy import integrate
from numpy import linalg as LA

grades = []
TokenDim=[]
Xdim=[]
Ydim=[]
Zdim=[]
Tdim=[]
Angpi=[]
distance=[]
results=[]
eliminate_Item='22222'   #'-5'#22222
plt.close('all')



with open('970431/658.txt',"r") as f:
    variable=f.readlines()
#--------------------

for i in range(len(variable)):
    grades.append(variable[i].strip('\n'))
# print(grades)


newgrades = list(filter(lambda x : x != eliminate_Item, grades))
TokenDim=CreateDimen(Tokens,newgrades,steps)
Xdim=CreateDimen(xVector,newgrades,steps)
Ydim=CreateDimen(yVector,newgrades,steps)
Zdim=CreateDimen(zVector,newgrades,steps)
Irdim=CreateDimen(IrVector,newgrades,steps)
Tdim=CreateDimen(tVector,newgrades,steps)


CreateFile(Xdim,Ydim,Zdim,Tdim)


Xdim = list(map(int, Xdim))
Ydim = list(map(int, Ydim))
Zdim = list(map(int, Zdim))
Irdim= list(map(int, Irdim))

#Create real data
Xdim = np.abs(Xdim)
Ydim = np.abs(Ydim)
Zdim = np.abs(Zdim)
Irdim= np.abs(Irdim)

#deraivate of real data
DXdim = np.diff(Xdim)
DYdim = np.diff(Ydim)
DZdim = np.diff(Zdim)

#Integral of Diff
IDXdim = Integ(DXdim)
IDYdim = Integ(DYdim)
IDZdim = Integ(DZdim)

# print("allItem=>\n")
# print(newgrades)
# print("\n \n")
# print("token=>\n")
# print(CreateDimen(Tokens,newgrades,steps))
# print("\n \n")
# print("X=>\n")
# print(CreateDimen(xVector,newgrades,steps))
# print("\n \n")
# print("Y=>\n")
# print(CreateDimen(yVector,newgrades,steps))
# print("\n \n")
# print("Z=>\n")
# print(CreateDimen(zVector,newgrades,steps))
# print("\n \n")
# print("t=>\n")
# print(CreateDimen(tVector,newgrades,steps))


# Angpi=np.arccos((float(Xdim[50]/(LA.norm([Xdim[50],Ydim[50],Zdim[50]])))))
# Angpi=np.arccos((float(Xdim/(LA.norm([Xdim,Ydim,Zdim])))))


def AngpiCa():
    dem=[]
    for i in range(90):
        Angpi=LA.norm([Xdim[i],Ydim[i],Zdim[i]])
        acos=np.arccos(Zdim[i]/Angpi)
        dem.append(acos)

    return dem 


def Distance():
    dem=[]
    for i in range(90):
        Angpi=LA.norm([IDXdim[i],IDYdim[i],IDZdim[i]])
        dem.append(Angpi)

    return dem 


Angpi=AngpiCa()
distance=Distance()
# Angpi=LA.norm([3,4])






print("Angpi=")
print(Angpi)
print("Angpi23=")
print(Angpi[24])
print(IDXdim[24])
print(IDYdim[24])
print(IDZdim[24])











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

plt.subplot(411)
plt.plot(Angpi)
plt.title('AAngle')

plt.subplot(412)
plt.plot(distance)
plt.title('distance')




plt.show()
plt.close('all')
