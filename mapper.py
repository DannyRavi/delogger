import csv
import os

counter = 0

all_files = os.listdir("BigData/")
Len_all_files = len(all_files)

# a = "abc"
# a, result = a[:-1], a[-1]
data = []
title = ['number  ', 'name    ', 'act     ']
data.append(title)
for numberCounter in range(Len_all_files):
    Read_selected_files = all_files[numberCounter]
    Read_selected_files = str(Read_selected_files)

    inputmapper = raw_input("insert your map ==>  ")
    inputmapper = str(inputmapper)
    counter += 1
    strCounter = str(counter)

    for i in range(4):
        Read_selected_files, result = Read_selected_files[:-1], Read_selected_files[-1]
    for i in range(1):
        inputmapper, result = inputmapper[:-1], inputmapper[-1]


    rows = [strCounter, Read_selected_files, inputmapper]
    data.append(rows)
    

    
    # with open('hamid.csv', 'w') as csvFile:

# with open('person.csv', 'w') as csvFile:
#     fields = ['number', 'nameOfFile','act']
#     writer = csv.DictWriter(csvFile, fieldnames=fields)
#     writer.writeheader()
#     writer.writerows(data)

with open('hamid.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(data)

csvFile.close()

print("writing completed")

data = []

# csvFile.close()


#     csvFile.close()
