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
divide = 2
Refrence_for_detect = 6
midNumber = []
CreateZeroIndex = 170
midNumber = [0] * CreateZeroIndex
EndDataEliminate = 35


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
    '''data goto the computer underStand'''
    for i in range(len(grades)):
        mini_size = len(grades[i].split(','))
        for ii in range(mini_size):
            sd = grades[i].split(',')
            ReConstruct.append(sd[ii])

    stepz = 5
    Xdim = CreateDimen(0, ReConstruct, stepz)
    Ydim = CreateDimen(1, ReConstruct, stepz)
    Zdim = CreateDimen(2, ReConstruct, stepz)
    Irdim = CreateDimen(3, ReConstruct, stepz)
    Tdim = CreateDimen(4, ReConstruct, stepz)
    # Irdim=CreateDimen(IrVector,newReConstruct,steps2)
    # Tdim=CreateDimen(tVector,newgrades,steps)

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

    XXdim1 = [i for i in DXdim if i <= 500]
    YYdim1 = [i for i in DYdim if i <= 500]
    ZZdim1 = [i for i in DZdim if i <= 500]

    XXdim = [i for i in XXdim1 if i >= -500]
    YYdim = [i for i in YYdim1 if i >= -500]
    ZZdim = [i for i in ZZdim1 if i >= -500]

    # Integral of Diff
    IDXdim = Integ(XXdim)
    IDYdim = Integ(YYdim)
    IDZdim = Integ(ZZdim)

    ranges = min(len(IDXdim), len(IDYdim), len(
        IDZdim))  # for ban out of index list
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
            Angpi = LA.norm([IDXdim[i], IDYdim[i], IDZdim[i]])
            dem.append(Angpi)
        return dem    



    Angpi = AngpiCa()
    distance = Distance()

    distance = Distance()
    for i in range(EndDataEliminate):
        distance.pop()


    
    for i in range(len(distance)//3):
        sequence = distance[-5:-1]
        MidSequence = (sum(sequence))/(len(sequence))
        distance.append(MidSequence)

    SummidNumber = []
    dist = np.array(distance)
    stackCount = 0
    for i in range(len(dist)):
        midNumber[stackCount] = dist[i]
        stackCount += 1
        sumdiv = sum(midNumber)/len(midNumber)
        SummidNumber.append(sumdiv)
        if stackCount == len(midNumber):
            stackCount = 0



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
    # ! ax_name = str(all_files[numberCounter]) + 'X.png'
    # ! plt.savefig('axs/' + ax_name)

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

    # ! ax_name = str(all_files[numberCounter]) + 'Y.png'
    # ! plt.savefig('axs/' + ax_name)

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

    # ! ax_name = str(all_files[numberCounter]) + 'Z.png'
    # ! plt.savefig('axs/' + ax_name)

    plt.figure(4)

    plt.subplot(511)
    plt.plot(Angpi)
    plt.title('Angle')

    plt.subplot(512)
    dist = np.array(distance)
    plt.plot(dist)
    plt.title('distance')

    plt.subplot(513)
    y = dist.__gt__(Refrence_for_detect)
    plt.plot(y, 'y-', linewidth=2, label='filtered data')
    plt.title('output norm abs')


    plt.subplot(514)
    sumFormatMath = np.array(SummidNumber)
    RefrenceCut = sumFormatMath.__gt__(Refrence_for_detect)
    plt.plot(RefrenceCut, 'b-', linewidth=2, label='filtered data')
    plt.title('output sum4norm aRefrenceCut')
    
    plt.subplot(515)
    sumFormatMath = np.array(SummidNumber)
    plt.plot(sumFormatMath, 'b-', linewidth=2, label='filtered data')
    plt.title('sumFormatMath')

    # ! ax_name = str(all_files[numberCounter]) + 'out.png'
    # ! plt.savefig('axs/' + ax_name)
    #! plt.show()       #! ################### for show graph ############################
    #! plt.close('all') #! ################### for close graph ###########################

    algoritm_detect = []
    for i in range(len(sumFormatMath)):
        if(sumFormatMath[i] > Refrence_for_detect):
            algoritm_detect.append(1)
        else:
            algoritm_detect.append(0)

    name_file_execute = str(all_files[numberCounter])

    CreateFile_outputAloritm(algoritm_detect, name_file_execute)

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
    algoritm_detect = []
    midNumber = []
    midNumber = [0] * CreateZeroIndex

