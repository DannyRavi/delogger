import matplotlib.pyplot as plt
import numpy as np
from dimes import *
from numpy import *
from scipy import integrate
from numpy import linalg as LA
import os
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
ReConstruct = []
counter = 0
divide = 25

eliminate_Item = '22222'  # '-5'#22222
plt.close('all')

all_files = os.listdir("BigData/")
Len_all_files = len(all_files)
for numberCounter in range(Len_all_files):
    Read_selected_files = all_files[numberCounter]
    Read_selected_files = str(Read_selected_files)

    with open('BigData/' + Read_selected_files, "r") as f:
        variable = f.readlines()
    # --------------------

    for i in range(len(variable)):
        grades.append(variable[i].strip('\n'))

    # print(grades)

        # for example 5
    # print(mini_size)
    for i in range(len(grades)):
        mini_size = len(grades[i].split(','))
        for ii in range(mini_size):
            sd = grades[i].split(',')
            ReConstruct.append(sd[ii])

    newgrades = list(filter(lambda x: x != eliminate_Item, grades))
    stepz = 5
    Xdim = CreateDimen1(0, ReConstruct, stepz)
    Ydim = CreateDimen(1, ReConstruct, stepz)
    Zdim = CreateDimen(2, ReConstruct, stepz)
    Irdim = CreateDimen(3, ReConstruct, stepz)
    Tdim = CreateDimen(4, ReConstruct, stepz)
    # Irdim=CreateDimen(IrVector,newReConstruct,steps2)
    # Tdim=CreateDimen(tVector,newgrades,steps)
    ranges = len(Xdim)-50

    # ? CreateFile(Xdim, Ydim, Zdim, Tdim)

    Xdim = list(map(int, Xdim))
    Ydim = list(map(int, Ydim))
    Zdim = list(map(int, Zdim))
    # Irdim= list(map(int, Irdim))

    # Create real data
    Xdim = np.abs(Xdim)
    Ydim = np.abs(Ydim)
    Zdim = np.abs(Zdim)
    # Irdim= np.abs(Irdim)

    # Irdim= list(map(int, Irdim))
    splitX = list(split_by(Xdim, divide))
    splitY = list(split_by(Ydim, divide))
    splitZ = list(split_by(Zdim, divide))

    medianDownsampleX = normalize(splitX, divide)
    medianDownsampleY = normalize(splitY, divide)
    medianDownsampleZ = normalize(splitZ, divide)
    # Create real data

    FilterIDXdim = ReSample(medianDownsampleX, divide)
    FilterIDYdim = ReSample(medianDownsampleY, divide)
    FilterIDZdim = ReSample(medianDownsampleZ, divide)

    Xdim = np.abs(FilterIDXdim)
    Ydim = np.abs(FilterIDYdim)
    Zdim = np.abs(FilterIDZdim)

    # Irdim= np.abs(Irdim)

    # deraivate of real data
    DXdim = np.diff(Xdim)
    DYdim = np.diff(Ydim)
    DZdim = np.diff(Zdim)

    # ? XXdim = FilterAmplitude (DXdim,-2000,2000) #[i for i in DXdim if i <= 1000]
    # ? YYdim = FilterAmplitude (DYdim,-2000,2000) #[i for i in DYdim if i <= 1000] # limit ovf
    # ? ZZdim = FilterAmplitude (DZdim,-2000,2000) #[i for i in DZdim if i <= 1000]

    XXdim1 = [i for i in DXdim if i <= 3000]
    YYdim1 = [i for i in DYdim if i <= 3000]
    ZZdim1 = [i for i in DZdim if i <= 3000]

    XXdim = [i for i in XXdim1 if i >= -3000]
    YYdim = [i for i in YYdim1 if i >= -3000]
    ZZdim = [i for i in ZZdim1 if i >= -3000]

    # Integral of Diff
    IDXdim = Integ(XXdim)
    IDYdim = Integ(YYdim)
    IDZdim = Integ(ZZdim)

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

# ?
    Angpi = AngpiCa()
    distance = Distance()
  
# ?
    # ? b, a = butter(4, 0.1, analog=False)
# ?
    # ? # Apply the filter to xn.  Use lfilter_zi to choose the initial condition
    # ? # of the filter.
    # ? zi = lfilter_zi(b, a)
    # ? z, _ = lfilter(b, a, distance, zi=zi*distance[0])
# ?
    # ? # Apply the filter again, to have a result filtered at an order
    # ? # the same as filtfilt.
    # ? z2, _ = lfilter(b, a, z, zi=zi*z[0])
# ?
    # ? # Use filtfilt to apply the filter.
    # ? y = filtfilt(b, a, distance)

    # print("Angpi=")
    # print(Angpi)
    # print("Angpi23=")
    # print(Angpi[24])
    # print(IDXdim[24])
    # print(IDYdim[24])
    # print(IDZdim[24])
    # vr = y.__gt__(12);
    # print(vr)

    plt.figure(1)

    plt.subplot(411)
    plt.plot(Xdim)
    plt.title('Real signal')

    plt.subplot(412)
    plt.plot(XXdim)
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
    ax_name = str(all_files[numberCounter]) + 'X.png'
    plt.savefig('axs/' + ax_name)

    plt.figure(2)

    plt.subplot(411)
    plt.plot(Ydim)
    plt.title('Real signal')

    plt.subplot(412)
    plt.plot(YYdim)
    plt.title('diff signal')

    plt.subplot(413)
    plt.plot((IDYdim))
    plt.title('integral signal')

    plt.subplot(414)
    plt.plot(np.abs(IDYdim))
    plt.title('abs signal')
    plt.xlabel('Y')

    ax_name = str(all_files[numberCounter]) + 'Y.png'
    plt.savefig('axs/' + ax_name)

    plt.figure(3)

    plt.subplot(411)
    plt.plot(Zdim)
    plt.title('Real signal')

    plt.subplot(412)
    plt.plot(ZZdim)
    plt.title('diff signal')

    plt.subplot(413)
    plt.plot((IDZdim))
    plt.title('integral signal')

    plt.subplot(414)
    plt.plot(np.abs(IDZdim))
    plt.title('abs signal')
    plt.xlabel('Z')

    ax_name = str(all_files[numberCounter]) + 'Z.png'
    plt.savefig('axs/' + ax_name)

    plt.figure(4)

    plt.subplot(311)
    plt.plot(Angpi)
    plt.title('Angle')

    plt.subplot(312)
    plt.plot(distance)
    plt.title('distance')

    plt.subplot(313)
    dist = np.array(distance)
    y = dist.__gt__(7)
    plt.plot(y, 'y-', linewidth=2, label='filtered data')
    plt.title('output norm abs')

    # plt.subplot(413)
    # y = abs(y)
    # y = y.__gt__(10)
    # plt.plot(y, 'g-', linewidth=2, label='filtered data')
    # plt.title('filtered norm abs')
#
    # plt.subplot(413)
    # y = distance.__gt__(12)
    # plt.plot(y, 'y-', linewidth=2, label='filtered data')
    # plt.title('output norm abs')

    ax_name = str(all_files[numberCounter]) + 'out.png'
    plt.savefig('axs/' + ax_name)
    # plt.show()  #! ################### for show graph ###########################
    plt.close('all')

    name_file_execute = str(all_files[numberCounter])
    print(name_file_execute)
    counter += 1
    print(counter)

    grades = []
    TokenDim = []
    Xdim = []
    Ydim = []
    Zdim = []
    Tdim = []
    Angpi = []
    distance = []
    results = []
    ReConstruct = []
