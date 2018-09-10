import matplotlib.pyplot as plt
import numpy as np
from numpy import *
from scipy import integrate
from scipy import signal
from scipy.signal import lfilter, lfilter_zi, filtfilt, butter
from numpy import linalg as LA
from dimes import *
from Filtering import *
from ANNC import *


plt.close('all')

eliminate_Item = ''

with open('9706A2/A2_2.txt', "r") as f:
    variable = f.readlines()
# --------------------

for i in range(len(variable)):
    grades.append(variable[i].strip('\n'))
grades = list(filter(lambda x: x != eliminate_Item, grades))

# dem.append(grades[5].split(','))

# ddd = r2d2.remove (',')
stepz = 5
Xdim = CreateDimen1(0, grades, stepz)
Ydim = CreateDimen(1, grades, stepz)
Zdim = CreateDimen(2, grades, stepz)
Irdim = CreateDimen(3, grades, stepz)
Tdim = CreateDimen(4, grades, stepz)
print(Irdim[3])
Xdim = list(map(int, Xdim))
Ydim = list(map(int, Ydim))
Zdim = list(map(int, Zdim))


plt.figure(1)

plt.subplot(311)
plt.plot(Xdim)
plt.title('X')

plt.subplot(312)
plt.plot(Ydim)
plt.title('Y')

plt.subplot(313)
plt.plot((Zdim))
plt.title('Z')

plt.show()
plt.close('all')
# for x in range(0,len(newgrades)):
#         # for i in range(0,len(newgrades[x],)
#     dem.append(newgrades[x])
# r2d2=dem[x]
# Xdim = list(map(int, dem))
# dem.split(',')
# r2d2=dem[2]
# print(newgrades[2])
# def CreateDimen1(Vector,dataInput,Steps2):
#     dem=[]
#     for x in range(Vector,len(dataInput),Steps2):
#         dem.append(dataInput[x])
#     return dem
