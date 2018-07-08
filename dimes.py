Tokens=0
xVector=1
yVector=2
zVector=3
tVector=4
steps=5




def CreateDimen(Vector,dataInput,Steps):
    dem=[]
    for x in range(Vector,len(dataInput),Steps):
        dem.append(dataInput[x])
    return dem,len(dem)  