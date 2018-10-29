import matplotlib.pyplot as plt
import numpy as np
from numpy import *
from numpy import linalg as LA
from ForDebudLibrary import *
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
divide = 1  # deymii

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

    stepz = 5
    Xdim = CreateDimen1(0, ReConstruct, stepz)
    Ydim = CreateDimen(1, ReConstruct, stepz)
    Zdim = CreateDimen(2, ReConstruct, stepz)
    Irdim = CreateDimen(3, ReConstruct, stepz)
    Tdim = CreateDimen(4, ReConstruct, stepz)

    Xdim = list(map(int, Xdim))
    Ydim = list(map(int, Ydim))
    Zdim = list(map(int, Zdim))
    Irdim = list(map(int, Irdim))
    

    t = 0
    for i in range(len(Irdim)):
      if(Irdim[i]  > 2 ):
        t += 1
    if (t >= 1):
      lineError = len(Irdim) - t
      print("***********************error**************************",lineError )

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


    name_file_execute = str(all_files[numberCounter])
    print(name_file_execute)
    counter += 1
    print(counter)
    if (t >= 1):
        print("***********************----*****************************" )
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
