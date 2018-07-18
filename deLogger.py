import matplotlib.pyplot as plt
import numpy as np
from  dimes import *

grades = []
TokenDim=[]
Xdim=[]
Ydim=[]
Zdim=[]
Tdim=[]
results=[]
eliminate_Item='22222'
plt.close()
with open('ForwardStop.txt',"r") as f:
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
Tdim=CreateDimen(tVector,newgrades,steps)


CreateFile(Xdim,Ydim,Zdim,Tdim)


Xdim = list(map(int, Xdim))
Ydim = list(map(int, Ydim))
Zdim = list(map(int, Zdim))


Xdim = np.abs(Xdim)
Ydim = np.abs(Ydim)
Zdim = np.abs(Zdim)


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

plt.subplot(311)
plt.plot(Xdim)
plt.title('X Dimen')
plt.grid(True)

plt.subplot(312)
plt.plot(Ydim)
plt.ylabel('Amp')
plt.title('Y Dimen')
plt.grid(True)

plt.subplot(313)
plt.plot(Zdim)
plt.xlabel('Index')
plt.title('Z Dimen')
plt.grid(True)

plt.show()
plt.close()


    