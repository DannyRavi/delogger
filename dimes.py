

Tokens=0
xVector=1
yVector=2
zVector=3
IrVector=4
tVector=5
steps=6
steps2=5


# relay
grades = []
TokenDim=[]
Xdim=[]
Ydim=[]
Zdim=[]
Tdim=[]
Angpi=[]
distance=[]
results=[]




def CreateDimen(Vector,dataInput,Steps):
    dem=[]
    for x in range(Vector,len(dataInput),Steps):
        dem.append(dataInput[x])
    return dem 

def CreateDimen1(Vector,dataInput,Steps2):
    dem=[]
    for x in range(Vector,len(dataInput),Steps2):
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

def Integ(x):
    z=[]
    sum1=0
    for i in range(len(x)):
        sum1 +=x[i]
        z.append(sum1)

    return z


def normalize(dataInput,divide):
    dem=[]
    for x in range(len(dataInput)):
        xx=dataInput[x]/float(divide)
        dem.append(xx)
    return dem





def split_by(sequence, length):
    iterable = iter(sequence)
    def yield_length():
        for i in range(length):
             yield iterable.next()
    while True:
        res = list(yield_length())
        if not res:
            return
        yield res


def ReSample(Datain,divide):
    cc=[]
    for i in range(len(Datain)):
        cc.append(Datain[i]*divide)
    return cc   

