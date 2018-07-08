from  dimes import *

grades = []
eliminate_Item='222222'
with open('readlog.txt',"r") as f:
    variable=f.readlines()
#--------------------

for i in range(len(variable)):
    grades.append(variable[i].strip('\n'))
# print(grades)


newgrades = list(filter(lambda x : x != eliminate_Item, grades))
print("allItem=>\n")
print(newgrades)
print("\n \n")
print("token=>\n")
print(CreateDimen(Tokens,newgrades,steps))
print("\n \n")
print("X=>\n")
print(CreateDimen(xVector,newgrades,steps))
print("\n \n")
print("Y=>\n")
print(CreateDimen(yVector,newgrades,steps))
print("\n \n")
print("Z=>\n")
print(CreateDimen(zVector,newgrades,steps))
print("\n \n")
print("t=>\n")
print(CreateDimen(tVector,newgrades,steps))



    