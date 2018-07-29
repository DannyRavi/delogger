import matplotlib.pyplot as plt
import numpy as np
from  dimes import *
from numpy import *
from scipy import integrate
from scipy import signal
from scipy.signal import lfilter, lfilter_zi, filtfilt, butter

grades = []
TokenDim=[]
Xdim=[]
Ydim=[]
Zdim=[]
Tdim=[]
results=[]
eliminate_Item='22222'   #'-5'#22222
plt.close('all')

# def butter_lowpass(cutoff, fs, order=5):
#     nyq = 0.5 * fs
#     normal_cutoff = cutoff / nyq
#     b, a = butter(order, normal_cutoff, btype='low', analog=False)
#     return b, a

# def butter_lowpass_filter(data, cutoff, fs, order=5):
#     b, a = butter_lowpass(cutoff, fs, order=order)
#     y = lfilter(b, a, data)
#     return y

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






# # Filter requirements.
# order = 5
# fs = 50.0       # sample rate, Hz
# cutoff = 3.667  # desired cutoff frequency of the filter, Hz


# T = 5.0         # seconds
# n = int(T * fs) # total number of samples
# t = np.linspace(0, T, n, endpoint=False)
# # "Noisy" data.  We want to recover the 1.2 Hz signal from this.
# data = np.sin(1.2*2*np.pi*t) + 1.5*np.cos(9*2*np.pi*t) + 0.5*np.sin(12.0*2*np.pi*t)


# # Get the filter coefficients so we can check its frequency response.
# b, a = butter_lowpass(cutoff, fs, order)
# # Plot the frequency response.
# w, h = freqz(b, a, worN=8000)
# # y = butter_lowpass_filter(IDZdim, cutoff, fs, order)

# y = butter_lowpass_filter(data, cutoff, fs, order)

b, a = butter(4, 0.2,analog=False)

# Apply the filter to xn.  Use lfilter_zi to choose the initial condition
# of the filter.
zi = lfilter_zi(b, a)
z, _ = lfilter(b, a, Xdim, zi=zi*Xdim[0])

# Apply the filter again, to have a result filtered at an order
# the same as filtfilt.
z2, _ = lfilter(b, a, z, zi=zi*z[0])

# Use filtfilt to apply the filter.
y = filtfilt(b, a, Xdim)






