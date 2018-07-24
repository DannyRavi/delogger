Tokens=0
xVector=1
yVector=2
zVector=3
IrVector=4
tVector=5
steps=6




def CreateDimen(Vector,dataInput,Steps):
    dem=[]
    for x in range(Vector,len(dataInput),Steps):
        dem.append(dataInput[x])
    return dem 


def CreateFile(X,Y,Z,T):
    f= open("outPutDimen.txt","w+")
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