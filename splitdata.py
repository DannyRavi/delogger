import matplotlib.pyplot as plt
import numpy as np
from dimes import *
from numpy import *
from scipy import integrate
from numpy import linalg as LA
import random
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


eliminate_Item = '22222'  # '-5'#22222
plt.close('all')

all_files = os.listdir("BigData/") 
Len_all_files = len(all_files)
for numberCounter in range(Len_all_files):
    Read_selected_files = all_files[numberCounter]
    Read_selected_files = str(Read_selected_files)
    
with open('BigData/'+ all_files[5], "r") as f:
    variable = f.readlines()
# --------------------
for i in range(len(variable)):
    grades.append(variable[i].strip('\n'))


mini_size = len(grades[5].split(',') )    # for example 5
print (mini_size)
for i in range(len(grades)):
  for ii in range (mini_size):
    sd = grades[i].split(',')
    ReConstruct.append(sd[ii])


██╗    ██████╗ ██╗██████╗     ██╗████████╗
██║    ██╔══██╗██║██╔══██╗    ██║╚══██╔══╝
██║    ██║  ██║██║██║  ██║    ██║   ██║   
██║    ██║  ██║██║██║  ██║    ██║   ██║   
██║    ██████╔╝██║██████╔╝    ██║   ██║   
╚═╝    ╚═════╝ ╚═╝╚═════╝     ╚═╝   ╚═╝   
                                          