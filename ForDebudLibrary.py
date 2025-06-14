import numpy as np

Tokens = 0
xVector = 1
yVector = 2
zVector = 3
IrVector = 4
tVector = 5
steps = 6
steps2 = 5


# relay
grades = []
TokenDim = []
Xdim = []
Ydim = []
Zdim = []
Tdim = []
Angpi = []
distance = []
results = []


def CreateDimen(Vector, dataInput, Steps):
    dem = []
    for x in range(Vector, len(dataInput), Steps):
        dem.append(dataInput[x])
    return dem


def CreateDimen1(Vector, dataInput, Steps2):
    dem = []
    for x in range(Vector, len(dataInput), Steps2):
        dem.append(dataInput[x])
    return dem


def CreateFile(X, Y, Z, T):
    f = open("outPutDimen.txt", "w+")
    f.write(" X=> \r\n")
    f.write(str(X))
    f.write("\r\n")
    f.write(" Y=> \r\n")
    f.write(str(Y))
    f.write("\r\n")
    f.write(" Z=> \r\n")
    f.write(str(Z))
    f.write("\r\n")
    f.write(" T=> \r\n")
    f.write(str(T))
    f.write("\r\n")
    f.close()


def Integ(x):
    z = []
    sum1 = 0
    for i in range(len(x)):
        sum1 += x[i]
        z.append(sum1)

    return z


def normalize(dataInput, divide):
    dem = []
    for x in range(len(dataInput)):
        xx = dataInput[x]
        xx = np.sum(xx)
        xx = xx/divide
        dem.append(xx)
    return dem


def split_by(sequence, length):
    iterable = iter(sequence)

    def yield_length():
        for i in range(length):
            try:
                yield iterable.__next__()
            except StopIteration:
                return    
    while True:
        res = list(yield_length())
        if not res:
            return
        yield res


def ReSample(Datain, divide):
    cc = []
    zz = []
    for i in range(len(Datain)):
        xx = [Datain[i]] * divide
        cc.append(xx)
    for Item in range(len(cc)):
        for Item2 in range(divide):
            zz.append(cc[Item][Item2])
    return zz


def AliAlgoritms(baseLines, treshold, DataReSampleIn, DataIn_Difference):
    xcc = []
    stateFF = []
    state = 1
    for i in range(0, len(DataReSampleIn)-DataIn_Difference):

        Temp = (abs(DataReSampleIn[i]-DataReSampleIn[i+DataIn_Difference]))
        DiffData = abs(Temp-baseLines)
        if(DiffData < treshold):
            baseLines = Temp
            xcc.append(0)
        elif(DiffData > treshold):
            baseLines = Temp
            state ^= 1
            xcc.append(state)

    T = 0
    for i in range(len(xcc)):
        if xcc[i] == 1:
            T ^= 1
        if T == 1:
            stateFF.append(1)
        else:
            stateFF.append(0)
    return stateFF


def FilterAmplitude(DataIn, LowRange, HighRange):
    NewData = []
    for i in range(len(DataIn)):
        if ((DataIn[i] < HighRange) and (DataIn[i] > LowRange)):
            NewData.append(DataIn[i])
        else:
            NewData.append(0)

    return NewData




Real_human_detect = []


def CreateFileForHumandetector(inputData, nameOfFile):
    nameOfFile =  str (nameOfFile)
    f = open('outHumanAlgoritm/'+ nameOfFile, "w+")
    f.write(str(inputData))
    f.close()


def CreateFile_outputAloritm(inputData, nameOfFile):
    nameOfFile =  str (nameOfFile)
    f = open('OutputAlgoritm/'+ nameOfFile, "w+")
    f.write(str(inputData))
    f.close()


def CreateFlag(dataIn):
    togg1 = False 
    togg2 = True
    togg3 = True    
    Change = []        
    for i in range(len(dataIn)-1):
        StChange = abs(dataIn[i] - dataIn[i+1])
        if StChange == 1 :
            togg1 ^= True
        if togg1 == True and togg2:
            Change.append(1)
            togg2 = False
            togg3 = True
        if(togg1 == False and togg3):
            togg2 = True
            togg3 = False
            Change.append(0)
    return Change       

def Comrator2data(In1,In2):
    LengthIn1 = len(In1)
    LengthIn2 = len(In2)
    Toggle1 = True
    Number = 0
    if(LengthIn1 == LengthIn2):
        for i in range(LengthIn1):
            if(In1[i] == In2[i]):
                LengthIn1 = len(In1)
            else:
                Toggle1 = False
        if Toggle1:
            print ("    Match")
        else:
            print ("    NOT Match")
            Number = 1          
    else:
        print ("    NOT Match")
        Number = 1
    return  Number  


def matchFunc(refData,otherData):
  stackData = []
  for i in range(len(refData)):
    if(refData[i]==otherData[i]):
      stackData.append(1)
    else:
      stackData.append(0)
  final =  ((sum(stackData))/len(refData)) *100


def TheLastDataOut(inputInsretEmptyORFull):
    
    databack = []  
    lastEF = []
    stackCountLimiter = 0
    EFsum = 0.0

    QueueEnd = []
    QueueArrayZero = 5
    QueueEnd = [0] * QueueArrayZero # for last of EFEFFE
    # add data to end and last of array work with 5 array
    for i in range(5):
        inputInsretEmptyORFull.insert(0,inputInsretEmptyORFull[0])
        inputInsretEmptyORFull.insert(-1,inputInsretEmptyORFull[-1])
        inputDataToArray = np.array(inputInsretEmptyORFull)

    # here the queue working
    for i in range(len(inputDataToArray)):

        QueueEnd[stackCountLimiter] = inputDataToArray[i]
        stackCountLimiter += 1
        sumer = sum(QueueEnd)
        lene = float(len(QueueEnd))
        EFsum = sumer / lene
        lastEF.append(EFsum)
        if( EFsum > 0.2):
            databack.append(1)
        else:
            databack.append(0)    

        if stackCountLimiter == len(QueueEnd):
             stackCountLimiter = 0    

    return databack