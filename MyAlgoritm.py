import matplotlib.pyplot as plt
import numpy as np
from  dimes import *
from numpy import *
from scipy import integrate
from scipy import signal
from scipy.signal import butter, lfilter, freqz

grades = []
TokenDim=[]
Xdim=[]
Ydim=[]
Zdim=[]
Tdim=[]
results=[]
eliminate_Item='22222'   #'-5'#22222
plt.close('all')



with open('970431/703.txt',"r") as f:
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
print("token=>\n")
print(CreateDimen(Tokens,newgrades,steps))
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
print("t=>\n")
print(CreateDimen(tVector,newgrades,steps))






# Filter requirements.
order = 6
fs = 1.0       # sample rate, Hz
cutoff = 3.667  # desired cutoff frequency of the filter, Hz

# Get the filter coefficients so we can check its frequency response.
b, a = butter_lowpass(cutoff, fs, order)
# Plot the frequency response.
w, h = freqz(b, a, worN=8000)
y = butter_lowpass_filter(IDZdim, cutoff, fs, order)









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

plt.plot( y, 'g-', linewidth=2, label='filtered data')


plt.show()
plt.close('all')