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
import os

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
divide = 20 #deymii



eliminate_Item = '22222'  # '-5'#22222
plt.close('all')

all_files = os.listdir("BigData/")
Len_all_files = len(all_files)
print ()

for numberCounter in range(Len_all_files):
    Read_selected_files = all_files[numberCounter]
    Read_selected_files = str(Read_selected_files)

    with open('BigData/' + Read_selected_files, "r") as f:
        variable = f.readlines()
    # --------------------

    

    for i in range(len(variable)):
        grades.append(variable[i].strip('\n'))
        
    rangeForrirate = len(grades)

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


    Xdim = list(map(int, Xdim))
    Ydim = list(map(int, Ydim))
    Zdim = list(map(int, Zdim))


    # Irdim=CreateDimen(IrVector,newgrades,steps2)
    # Tdim=CreateDimen(tVector,newgrades,steps)
    #ranges = len(Xdim)-10

    # ? CreateFile(Xdim,Ydim,Zdim,Tdim)


    Xdim = list(map(int, Xdim))
    Ydim = list(map(int, Ydim))
    Zdim = list(map(int, Zdim))


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

    #deraivate of real data
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
    

    #Integral of Diff
    IDXdim = Integ(XXdim)
    IDYdim = Integ(YYdim)
    IDZdim = Integ(ZZdim)



   
    ranges = min(len(IDXdim),len(IDYdim),len(IDZdim),rangeForrirate) # for ban out of index list





    # ? FilterIDXdim = filtering(4, 0.1, IDXdim).outy
    # ? FilterIDYdim = filtering(4, 0.1, IDYdim).outy
    # ? FilterIDZdim = filtering(4, 0.1, IDZdim).outy


    # print("b=",len(splitX))


    # print("Len=",len(medianDownsampleX),"medianDownsampleX=",medianDownsampleX,"medianDownsampleX[15]=",medianDownsampleX[5])



    # DXdim = np.diff(FilterIDXdim)
    # DYdim = np.diff(FilterIDYdim)
    # DZdim = np.diff(FilterIDZdim)

    # Integral of Diff
    # IDXdim = Integ(DXdim)
    # IDYdim = Integ(DYdim)
    # IDZdim = Integ(DZdim)


    p = Perceptron(3, np.array([0.2, 0.2, 0.2])) # [0.02, 0.02, 0.02]

    # for absolute
    # absIDXdim=np.abs(IDXdim)
    # absIDYdim=np.abs(IDYdim)
    # absIDZdim=np.abs(IDZdcim)

    # for filter absolut
    # ?absIDXdim = np.abs(FilterIDXdim)
    # ?absIDYdim = np.abs(FilterIDYdim)
    # ?absIDZdim = np.abs(FilterIDZdim)
    # for convert list to array
    ArrayabsIDXdim = np.abs(IDXdim)
    ArrayabsIDYdim = np.abs(IDYdim)
    ArrayabsIDZdim = np.abs(IDZdim)


    def Ann_Execute(r):
        p = r
        xxm = []
        OutY = []
        for x in range(ranges):
            xxm.append([ArrayabsIDXdim[x], ArrayabsIDYdim[x], ArrayabsIDZdim[x]])
            y = p(xxm[x])
            OutY.append(y)
        return OutY


    Ann_Execute(p)


    def ShowMyAlgortim():
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

        ax_name = str(all_files[numberCounter]) + 'X.png'
        plt.savefig('axs/' + ax_name)
        # plt.show()
        # plt.close()

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


        # plt.figure(4)
        # plt.subplot(111)
        # plt.plot(FilterIDXdim, 'g-', linewidth=2, label='filtered data')
        # plt.subplot(312)
        # plt.plot(Ann_Execute(p))
        # plt.title('ANN output')
        # plt.subplot(313)
        # plt.plot(np.abs(Xdim))
        # plt.title('Filtered signal')
        # plt.xlabel('X')
        # plt.plot(Ann_Execute(p))
        # plt.title('ANN output')

        plt.figure(4)
        plt.subplot(411)
        plt.plot(ArrayabsIDXdim, 'g-', linewidth=2, label='filtered data')
        plt.title('X filtered')
        plt.subplot(412)
        plt.plot(ArrayabsIDYdim, 'g-', linewidth=2, label='filtered data')
        plt.title('Y filtered')
        plt.subplot(413)
        plt.plot(ArrayabsIDZdim, 'g-', linewidth=2, label='filtered data')
        plt.title('Z filtered')
        plt.subplot(414)
        plt.plot(Ann_Execute(p), 'r-', linewidth=2, label='ANN output')
        plt.title('Ann Out')

        ax_name = str(all_files[numberCounter]) + 'out.png'
        plt.savefig('axs/' + ax_name)

        plt.show()
        plt.close('all')


    ShowMyAlgortim()

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
