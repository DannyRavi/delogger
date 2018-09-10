import matplotlib.pyplot as plt
import numpy as np
from dimes import *
from numpy import *
from scipy import integrate
from numpy import linalg as LA
from scipy.signal import lfilter, lfilter_zi, filtfilt, butter

grades = []
TokenDim = []
Xdim = []
Ydim = []
Zdim = []
Tdim = []
Angpi = []
distance = []
results = []

eliminate_Item = '22222'  # '-5'#22222
plt.close('all')


with open('9706A2/C1_3.txt', "r") as f:
    variable = f.readlines()
# --------------------

for i in range(len(variable)):
    grades.append(variable[i].strip('\n'))
# print(grades)


newgrades = list(filter(lambda x: x != eliminate_Item, grades))
stepz = 5
Xdim = CreateDimen1(0, grades, stepz)
Ydim = CreateDimen(1, grades, stepz)
Zdim = CreateDimen(2, grades, stepz)
Irdim = CreateDimen(3, grades, stepz)
Tdim = CreateDimen(4, grades, stepz)
# Irdim=CreateDimen(IrVector,newgrades,steps2)
# Tdim=CreateDimen(tVector,newgrades,steps)
ranges = len(Xdim)-10

CreateFile(Xdim, Ydim, Zdim, Tdim)


Xdim = list(map(int, Xdim))
Ydim = list(map(int, Ydim))
Zdim = list(map(int, Zdim))
# Irdim= list(map(int, Irdim))

# Create real data
Xdim = np.abs(Xdim)
Ydim = np.abs(Ydim)
Zdim = np.abs(Zdim)
# Irdim= np.abs(Irdim)

# deraivate of real data
DXdim = np.diff(Xdim)
DYdim = np.diff(Ydim)
DZdim = np.diff(Zdim)

# Integral of Diff
IDXdim = Integ(DXdim)
IDYdim = Integ(DYdim)
IDZdim = Integ(DZdim)

# print("allItem=>\n")
# print(newgrades)
# print("\n \n")
# print("token=>\n")
# print(CreateDimen1(Tokens,newgrades,steps2))
# print("\n \n")
# print("X=>\n")
# print(CreateDimen1(xVector,newgrades,steps2))
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
    dem = []
    for i in range(ranges):
        Angpi = LA.norm([Xdim[i], Ydim[i], Zdim[i]])
        acos = np.arccos(Zdim[i]/Angpi)
        dem.append(acos)

    return dem


def Distance():
    dem = []
    for i in range(ranges):
        # Angpi=IDXdim[i]**2
        # Angpi=LA.norm(IDXdim[i])
        Angpi = LA.norm([IDXdim[i], IDYdim[i], IDZdim[i]])

        # Angpi=LA.norm([IDXdim[i],IDZdim[i]])
        dem.append(Angpi)

    return dem


Angpi = AngpiCa()
distance = Distance()
# Angpi=LA.norm([3,4])

b, a = butter(4, 0.1, analog=False)

# Apply the filter to xn.  Use lfilter_zi to choose the initial condition
# of the filter.
zi = lfilter_zi(b, a)
z, _ = lfilter(b, a, distance, zi=zi*distance[0])

# Apply the filter again, to have a result filtered at an order
# the same as filtfilt.
z2, _ = lfilter(b, a, z, zi=zi*z[0])

# Use filtfilt to apply the filter.
y = filtfilt(b, a, distance)


# print("Angpi=")
# print(Angpi)
# print("Angpi23=")
# print(Angpi[24])
# print(IDXdim[24])
# print(IDYdim[24])
# print(IDZdim[24])
vr = y.__gt__(12);
print(vr)


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
plt.plot(Angpi)
plt.title('Angle')

plt.subplot(312)
plt.plot(distance)
plt.title('distance')

plt.subplot(313)
y = abs(y)
# y = y.__gt__(10)
plt.plot(y, 'g-', linewidth=2, label='filtered data')
plt.title('filtered norm abs')


plt.show()
plt.close('all')
