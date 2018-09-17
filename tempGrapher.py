import matplotlib.pyplot as plt
import numpy as np
from numpy import *
from dimes import *
from scipy import integrate
from scipy import signal
from matplotlib import *


decrease = []
increase = []
TokenDim = []
Xdim = []
Ydim = []
Zdim = []
Tdim = []
Angpi = []
distance = []
results = []


temp_decrease = []
temp_increase = []
temp_decrease_elm = []
temp_increase_elm = []


plt.close('all')


with open('tempture/decrease_temp.txt', "r") as f:
    variable = f.readlines()


for i in range(len(variable)):
    decrease.append(variable[i].strip('\n'))

# Irdim=CreateDimen(IrVector,newgrades,steps2)
f.close()

stepz = 1

temp_decrease = CreateDimen1(0, decrease, stepz)
temp_decrease = list(map(float, temp_decrease))
temp_decrease_elm = [i for i in temp_decrease if i <= 50]
# for i in range(len(temp_decrease)):
# if (temp_decrease[i] < 15):
# temp_decrease_elm.append(temp_decrease[i])
#
# !temp_decrease_elm = filter(lambda x: x <= 150, temp_decrease)



with open('tempture/increase_temp.txt', "r") as f:
    variable = f.readlines()


for i in range(len(variable)):
    increase.append(variable[i].strip('\n'))
f.close()


stepz = 1

temp_increase = CreateDimen1(0, increase, stepz)
temp_increase = list(map(float, temp_increase))
temp_increase_elm = [i for i in temp_increase if i <= 15]


# temp_decreasez = list(map(int, temp_decrease))
# print(temp_decrease)


# Create real data
# Xdim = np.abs(temp_decrease)
# Ydim = np.abs(temp_increase)

Xdim = temp_decrease
Ydim = temp_increase


# Irdim= np.abs(Irdim)

# deraivate of real data
DXdim = np.diff(Xdim)
DYdim = np.diff(Ydim)

Ddecrease = FilterAmplitude(DXdim,7,20) # ! for negetive data what should I do
Dincrease = FilterAmplitude(DYdim,7,20)
# brono = []
# for i in range(len(DXdim)):
# 
    # if ((DXdim[i] < 20) and (DXdim[i] > 7) ):
        # brono.append(temp_decrease[i])
    # else:
        # brono.append(0)
# DYdim = np.diff(Ydim)

# ?LowLimit_DXDim = [i for i in DXdim if i >= 5]
# ?HighLimit_DXDim = [i for i in LowLimit_DXDim if i <= 20]





# ?LowLimit_DYDim = [i for i in DYdim if i >= 10]
# ?HighLimit_DYDim = [i for i in LowLimit_DYDim if i <= 30]
# for i in range(len(temp_decrease)):
    # if (temp_decrease[i] < 15):
        # temp_decrease_elm.append(temp_decrease[i])
# DYdim = np.diff(Ydim)
# matplotlib.image.imsave('name.png', Ddecrease)

# Integral of Diff
IDXdim = Integ(Ddecrease)
IDYdim = Integ(Dincrease)

plt.figure(1)

plt.subplot(211)
plt.plot(temp_decrease_elm)
plt.title('decrease')


plt.subplot(212)
plt.plot(temp_increase_elm)
plt.title('increase')

plt.xlabel('Almost pure data')

plt.figure(2)

plt.subplot(211)
plt.plot(Ddecrease)
plt.title('decrease')

plt.subplot(212)
plt.plot(Dincrease)
plt.title('increase')

plt.xlabel('Reform Difrenece')

plt.figure(3)

plt.subplot(211)
plt.plot(IDXdim)
plt.title('decrease')

plt.subplot(212)
plt.plot(IDYdim)
plt.title('increase')

plt.xlabel('Robust')
s = 4

d = str(s)+'al.png'

plt.savefig('axs/'+ d)


# plt.show()
plt.close('all')


print('end')
