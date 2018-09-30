import matplotlib.pyplot as plt
import numpy as np
from dimes import *
from cursor import *
from numpy import *
from scipy import integrate
from numpy import linalg as LA
import os
from scipy.signal import lfilter, lfilter_zi, filtfilt, butter
from matplotlib.widgets import Cursor

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
Refrence_for_detect = 6
midNumber = []
CreateZeroIndex = 170
midNumber = [0] * CreateZeroIndex
divide = 2


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

    rangeForrirate = len(grades)

    # print(grades)

    # for example 5
    # print(mini_size)
    for i in range(len(grades)):
        mini_size = len(grades[i].split(','))
        for ii in range(mini_size):
            sd = grades[i].split(',')
            ReConstruct.append(sd[ii])

    Real_human_detect = []

    def on_pick(event):
        # Real_human_detect = []
        # global Real_human_detect
        # Real_human_detect = []
        artist = event.artist
        xmouse, ymouse = event.mouseevent.xdata, event.mouseevent.ydata
        x, y = artist.get_xdata(), artist.get_ydata()
        ind = event.ind
        # print 'Artist picked:', event.artist
        # print '{} vertices picked'.format(len(ind))
        # print 'Pick between vertices {} and {}'.format(min(ind), max(ind)+1)
        print 'x, y of mouse: {:.2f},{:.2f}'.format(xmouse, ymouse)
        # print 'Data point:', x[ind[0]], y[ind[0]]
        Real_human_detect.append(x[ind[0]])
        # return Real_human_detect

    stepz = 5
    Xdim = CreateDimen(0, ReConstruct, stepz)
    Ydim = CreateDimen(1, ReConstruct, stepz)
    Zdim = CreateDimen(2, ReConstruct, stepz)
    Irdim = CreateDimen(3, ReConstruct, stepz)
    Tdim = CreateDimen(4, ReConstruct, stepz)

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

    ranges = min(len(IDXdim), len(IDYdim), len(IDZdim),rangeForrirate)  # for ban out of index list

    #
    ##############################
    #

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

    # Angpi = AngpiCa()
    
    distance = Distance()


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

    fig = plt.figure(1)

    plt.subplot(321)
    sumFormatMath = np.array(SummidNumber)
    plt.plot(sumFormatMath)
    plt.title('distance')
    line, = plt.plot(sumFormatMath, 'r-', linewidth=2,
                     label='select target', picker=10)
    plt.title('output norm abs')
    fig.canvas.callbacks.connect('pick_event', on_pick)

    plt.subplot(322)
    sumFormatMath = np.array(SummidNumber)
    RefrenceCut = sumFormatMath.__gt__(Refrence_for_detect)
    plt.plot(RefrenceCut, 'b-', linewidth=2, label='filtered data')
    plt.title('output sum4norm aRefrenceCut')

    plt.subplot(323)
    plt.plot(np.abs(IDXdim))
    plt.title('integral signal x')
    plt.xlabel('X')

    plt.subplot(324)
    plt.plot(np.abs(IDYdim))
    plt.title('integral signal y')
    plt.xlabel('Y')

    plt.subplot(325)
    plt.plot(np.abs(IDZdim))
    plt.title('integral signal z')
    plt.xlabel('Z')

    plt.subplot(326)
    plt.plot(dist, 'y-', linewidth=2, label='filtered data')
    plt.title('Real output')
    

    mng = plt.get_current_fig_manager()
    mng.resize(*mng.window.maxsize())
    plt.show()
    plt.close('all')

    #
    ###############################
    #

    name_file_execute = str(all_files[numberCounter])
    print(name_file_execute)
    counter += 1  # number of code execute
    print(counter)

    Real_human_detect_int = [int(iii) for iii in Real_human_detect]
    final_human_output = []
    togg = False
    length_of_computer_export = len(Real_human_detect_int)
    numberCounter = 0

    '''this segment for export of logical human data '''
    for i in range(len(RefrenceCut)):
        # RR = Real_human_detect_int[numberCounter]
        try:
            RR = Real_human_detect_int[numberCounter]
        except IndexError:
            RR = 0.0001
        #    print ("Error")

        if (i == RR):
            togg ^= True
            if numberCounter < (length_of_computer_export-1):
                numberCounter += 1
        if togg == True:
            final_human_output.append(1)
        else:
            final_human_output.append(0)

    print(Real_human_detect)
    Real_human_detect = []
    Real_human_detect_int = []

    plt.figure(1)
    plt.subplot(111)
    plt.plot(final_human_output)
    plt.title('final_human_output')
    plt.show()
    plt.close('all')

    CreateFileForHumandetector(final_human_output, Read_selected_files)

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
    midNumber = [0] * CreateZeroIndex
