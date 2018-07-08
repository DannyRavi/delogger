grades = []

Tokens=0
xVector=1
yVector=2
zVector=3
steps=4
with open('readlog.txt',"r") as f:
    variable=f.readlines()
#--------------------


def CreateDimen(Vector,dataInput,Steps):
    dem=[]
    for x in range(Vector,len(dataInput),Steps):
        dem.append(dataInput[x])
    return dem,len(dem)   



for i in range(len(variable)):
    grades.append(variable[i].strip('\n'))
print(grades)


newgrades = list(filter(lambda x : x != '222222', grades))
print("ruslaka")

print(newgrades)
print("token=>")
print(CreateDimen(Tokens,newgrades,steps))
print("X=>")
print(CreateDimen(xVector,newgrades,steps))
print("Y=>")
print(CreateDimen(yVector,newgrades,steps))
print("Z=>")
print(CreateDimen(zVector,newgrades,steps))
   



    