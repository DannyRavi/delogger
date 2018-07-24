import matplotlib.pyplot as plt
import numpy as np
from  dimes import *
from numpy import *

grades = []
TokenDim=[]
Xdim=[]
Ydim=[]
Zdim=[]
Tdim=[]
results=[]
eliminate_Item='22222'   #'-5'#22222
plt.close()



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


Xdim = np.abs(Xdim)
Ydim = np.abs(Ydim)
Zdim = np.abs(Zdim)
Irdim= np.abs(Irdim)

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



plt.figure(1)

# plt.subplot(411)
plt.plot(np.diff(Xdim))
# plt.title('X Dimen')
# plt.grid(True)

# plt.subplot(412)
# plt.plot(Ydim)
# plt.ylabel('Amp')
# plt.title('Y Dimen')
# plt.grid(True)

# plt.subplot(413)
# plt.plot(Zdim)
# plt.xlabel('Amp')
# plt.title('Z Dimen')
# plt.grid(True)

# plt.subplot(414)
# plt.plot(Irdim)
# plt.xlabel('Amp')
# plt.title('IR Dimen')
# plt.grid(True)

# plt.show()
# plt.close()


plt.ylabel('some numbers')
plt.show()