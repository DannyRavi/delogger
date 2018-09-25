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

   ##todo  plt.figure(1)

   ##todo  plt.subplot(411)
   ##todo  plt.plot(Xdim)
   ##todo  plt.title('Real signal')

   ##todo  plt.subplot(412)
   ##todo  plt.plot(XXdim)
   ##todo  plt.title('diff signal')

   ##todo  plt.subplot(413)
   ##todo  plt.plot((IDXdim))
   ##todo  plt.title('integral signal')

   ##todo  plt.subplot(414)
   ##todo  plt.plot(np.abs(IDXdim))
   ##todo  plt.title('abs signal')
   ##todo  plt.xlabel('X')
   ##todo  # plt.show()
   ##todo  # plt.close()
   ##todo  ax_name = str(all_files[numberCounter]) + 'X.png'
   ##todo  #! plt.savefig('axs/' + ax_name)

   ##todo  plt.figure(2)

   ##todo  plt.subplot(411)
   ##todo  plt.plot(Ydim)
   ##todo  plt.title('Real signal')

   ##todo  plt.subplot(412)
   ##todo  plt.plot(YYdim)
   ##todo  plt.title('diff signal')

   ##todo  plt.subplot(413)
   ##todo  plt.plot((IDYdim))
   ##todo  plt.title('integral signal')

   ##todo  plt.subplot(414)
   ##todo  plt.plot(np.abs(IDYdim))
   ##todo  plt.title('abs signal')
   ##todo  plt.xlabel('Y')

   ##todo  ax_name = str(all_files[numberCounter]) + 'Y.png'
   ##todo  #! plt.savefig('axs/' + ax_name)

   ##todo  plt.figure(3)

   ##todo  plt.subplot(411)
   ##todo  plt.plot(Zdim)
   ##todo  plt.title('Real signal')

   ##todo  plt.subplot(412)
   ##todo  plt.plot(ZZdim)
   ##todo  plt.title('diff signal')

   ##todo  plt.subplot(413)
   ##todo  plt.plot((IDZdim))
   ##todo  plt.title('integral signal')

   ##todo  plt.subplot(414)
   ##todo  plt.plot(np.abs(IDZdim))
   ##todo  plt.title('abs signal')
   ##todo  plt.xlabel('Z')

   ##todo  ax_name = str(all_files[numberCounter]) + 'Z.png'
    # !plt.savefig('axs/' + ax_name)
    
    fig = plt.figure(1)

    plt.subplot(311)
    plt.plot(Angpi)
    plt.title('Angle')

    plt.subplot(312)
    plt.plot(distance)
    plt.title('distance')

    line, = plt.plot(distance, 'r-', linewidth=2, label='select target', picker=5)

    plt.title('output norm abs')
    
    fig.canvas.callbacks.connect('pick_event', on_pick)


    plt.subplot(313)
    dist = np.array(distance)
    y = dist.__gt__(5)
    # plt.plot(y, 'y-', linewidth=2, label='filtered data')
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
    #!plt.savefig('axs/' + ax_name)
    plt.show()  # ! ################### for show graph ###########################
    plt.close('all')
    print("==>{0}",Real_human_detect)
    name_file_execute = str(all_files[numberCounter])
    print(name_file_execute)
    counter += 1 # number of code execute
    print(counter)

    print("Real_human_detect")
    Real_human_detect_int = [int(iii) for iii in Real_human_detect]
    final_human_output = []
    togg = False
    length_of_computer_export = len(Real_human_detect_int)
    numberCounter = 0
    print(Real_human_detect_int)

    for i in range(len(y)):
        # RR = Real_human_detect_int[numberCounter]
        try:
           RR = Real_human_detect_int[numberCounter]
        except IndexError:
           RR = 0
        #    print ("Error")
        
        if i == RR:
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
    #Real_human_detect = []
    togg = False
    final_human_output = []
    
    numberCounter = 0
    Real_human_detect = []
    Real_human_detect_int = []
    length_of_computer_export = 0