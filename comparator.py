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
grades2 = []
TokenDim = []
Xdim = []
Ydim = []
Zdim = []
Tdim = []
Angpi = []
distance = []
results = []
ReConstruct = []
ReConstruct2 = []
counter = 0
divide = 25
final = []
minArrayd = 0.0
StChange = 0
StChange2 = 0

plt.close('all')

all_files = os.listdir("outHumanAlgoritm")
all_files2 = os.listdir("OutputAlgoritm")
Len_all_files = len(all_files)
Len_all_files2 = len(all_files2)
for numberCounter in range(Len_all_files):
    Read_selected_files = all_files[numberCounter]
    Read_selected_files2 = all_files2[numberCounter]

    Read_selected_files = str(Read_selected_files)
    Read_selected_files2 = str(Read_selected_files2)

    with open('outHumanAlgoritm/' + Read_selected_files, "r") as f:
        variable = f.readlines()
    # --------------------

    with open('OutputAlgoritm/' + Read_selected_files, "r") as f:
        variable2 = f.readlines()

    for i in range(len(variable)):
        grades.append(variable[i].strip('\n'))

    for i in range(len(variable2)):
        grades2.append(variable2[i].strip('\n'))

    if Read_selected_files in Read_selected_files2:
        print(Read_selected_files , 'ok')
    else:
        print("error")   

    for i in range(len(grades)):
        mini_size = len(grades[i].split(','))
        for ii in range(mini_size):
            sd = grades[i].split(',')
            ReConstruct.append(sd[ii])


    for i in range(len(grades2)):
        mini_size2 = len(grades2[i].split(','))
        for ii in range(mini_size2):
            sd = grades2[i].split(',')
            ReConstruct2.append(sd[ii])        

    #equal = ReConstruct - ReConstruct2
    # Xdim = CreateDimen(1, grades2, 2)
    Equals = []
    listToInt =[]
    listToInt2 =[]
    for i in range(len(ReConstruct)):
        listToStr = ''.join(ReConstruct[i])
        try:
            strToInt = int(listToStr)
            listToInt.append(strToInt)
        except ValueError:
            pass      # or whatever

    for i in range(len(ReConstruct2)):
        listToStr = ''.join(ReConstruct2[i])
        try:
            strToInt = int(listToStr)
            listToInt2.append(strToInt)
        except ValueError:
            pass      # or whatever


    #togg1 = False      
    #ArStateChange = []        
    #for i in range(len(listToInt)-1):
    #    StChange = abs(listToInt[i] - listToInt[i-1])
    #    if StChange == 1:
    #        togg1 ^= True
    #    if togg == True:
    #        ArStateChange.append(1)
    #    else:
    #        ArStateChange.append(0)

    Equals = [] 
    minArray = min(len(listToInt) , len(listToInt2))
    for i in range(minArray):
        equal = listToInt[i] - listToInt2[i]
        Equals.append(abs(equal))

    sumz = 0.0
    precent = 0.0
    minArray = float(minArray)
    minArrayd = minArray
    totalSum = sum(Equals)
    # print('==>',totalSum)
    sumz = totalSum/minArray 
    precent = sumz * 100
    #final[numberCounter] = precent
    print('==>',precent)

    final.append(precent)

    #f = open('CompareData/Stage1/csvfile.csv','w')
    #f.write('hi there\n') #Give your csv text here.
    ### Python will convert \n to os.linesep
    #f.close()
    
    valval = []
    grades = []
    grades2 = []
    TokenDim = []
    listToInt = [] 
    listToInt2 = []
    Equals = []
    Xdim = []
    Ydim = []
    Zdim = []
    Tdim = []
    Angpi = []
    distance = []
    results = []
    ReConstruct = []
    ReConstruct2 = []
    togg = False
    final_human_output = []
    numberCounter = 0
    Real_human_detect = []
    Real_human_detect_int = []
    length_of_computer_export = 0
    variable = 0
    variable2 = 0


lasFinal = 0.0
finall = sum(final)
lasFinal = (finall/minArrayd) * 100
print('END',lasFinal)    
