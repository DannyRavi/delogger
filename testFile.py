QueueEnd = []
QueueArrayZero = 5
QueueEnd = [0] * QueueArrayZero # for last of EFEFFE


def TheLastDataOut(inputInsretEmptyORFull):
    
    databack = []  
    lastEF = []
    stackCountLimiter = 0
    EFsum = 0.0
    # add data to end and last of array
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




# print(databack)  


