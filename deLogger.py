grades = []
demX=[]
Token-0
XVector=1
yVector=2
zVector=3
steps=4
with open('readlog.txt',"r") as f:
    variable=f.readlines()
#--------------------
for i in range(len(variable)):
    grades.append(variable[i].strip('\n'))
print(grades)


newgrades = list(filter(lambda x : x != '222222', grades))
print("ruslaka")

print(newgrades)
o=0
for x in range(1,len(newgrades),4):
    
    demX.append(newgrades[x])
    # print(newgrades[x]) 
print(demX)    

def CreateDimen(Vector,dataInput,Steps):
    