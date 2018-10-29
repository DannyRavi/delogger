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
divide = 20  # deymii


eliminate_Item = '22222'  # '-5'#22222
plt.close('all')

all_files = os.listdir("BigData/")
Len_all_files = len(all_files)
print()

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

    # deraivate of real data
    DXdim = np.diff(Xdim)
    DYdim = np.diff(Ydim)
    DZdim = np.diff(Zdim)

    # ? XXdim = FilterAmplitude (DXdim,-2000,2000) #[i for i in DXdim if i <= 1000]
    # ? YYdim = FilterAmplitude (DYdim,-2000,2000) #[i for i in DYdim if i <= 1000] # limit ovf
    # ? ZZdim = FilterAmplitude (DZdim,-2000,2000) #[i for i in DZdim if i <= 1000]

    XXdim1 = [i for i in DXdim if i <= 5000]
    YYdim1 = [i for i in DYdim if i <= 5000]
    ZZdim1 = [i for i in DZdim if i <= 5000]

    XXdim = [i for i in XXdim1 if i >= -5000]
    YYdim = [i for i in YYdim1 if i >= -5000]
    ZZdim = [i for i in ZZdim1 if i >= -5000]

    # Integral of Diff
    IDXdim = Integ(XXdim)
    IDYdim = Integ(YYdim)
    IDZdim = Integ(ZZdim)

    ranges = min(len(IDXdim), len(IDYdim), len(IDZdim),
                 rangeForrirate)  # for ban out of index list

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

    p = Perceptron(3, np.array([0.2, 0.2, 0.2]))  # [0.02, 0.02, 0.02]

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
            xxm.append(
                [ArrayabsIDXdim[x], ArrayabsIDYdim[x], ArrayabsIDZdim[x]])
            y = p(xxm[x])
            OutY.append(y)
        return OutY

    Ann_Execute(p)

    def ShowMyAlgortim():
        plt.figure(1)

        plt.subplot(331)
        plt.plot(Xdim)
        plt.title('Real signals')
        plt.ylabel('X')

        # plt.show()
        # plt.close()

        plt.subplot(332)
        plt.plot(Ydim)
        plt.ylabel('Y')

        plt.subplot(333)
        plt.plot(Zdim)
        plt.ylabel('Z')



        plt.subplot(334)
        plt.title('integral signals')
        plt.plot(IDXdim, 'y-')
        plt.ylabel('X')


        plt.subplot(335)
        plt.plot(IDYdim, 'y-')
        plt.ylabel('Y')

        plt.subplot(336)
        plt.plot(IDZdim, 'y-')
        plt.ylabel('Z')


        plt.subplot(337)
        plt.title('abs integral signals')
        plt.plot(ArrayabsIDXdim, 'r-')
        plt.ylabel('X')


        plt.subplot(338)
        plt.plot(ArrayabsIDYdim, 'r-')
        plt.ylabel('Y')

        plt.subplot(339)
        plt.plot(ArrayabsIDZdim, 'r-')
        plt.ylabel('Z')


        mng = plt.get_current_fig_manager()
        mng.resize(*mng.window.maxsize())
        ax_name = str(all_files[numberCounter]) + '.png'
        plt.savefig('axs/' + ax_name)
        #!plt.show()
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
    togg = False
    final_human_output = []
    numberCounter = 0
    Real_human_detect = []
    Real_human_detect_int = []
    length_of_computer_export = 0
    algoritm_detect = []
    midNumber = []
