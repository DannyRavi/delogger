
# import numpy as np

# a = range(10)

# def Distance_with_filter():
#    dem = []
#    for i in range(ranges):
#        # Angpi=IDXdim[i]**2
#        # Angpi=LA.norm(IDXdim[i])
#        Angpi = LA.norm([IDXdim[i], IDYdim[i], IDZdim[i]])
#        # Angpi=LA.norm([IDXdim[i],IDZdim[i]])
#        dem.append(Angpi)
#        return dem

# buckets = []
# buckets = [1] * 10
# for i in range(len(buckets)//3):
#     b = 7
#     buckets.pop()
# print(buckets)

#!dist = np.array(distance)
#!print(dist)
#!#Idist = int(dist)
#!stackCount = 0
#!for i in range(len(Idist)):
#!    midNumber[stackCount] = Idist[i]
#!    stackCount += 1
#!    SummidNumber = sum(midNumber)
#!    if stackCount == 10:
#!        stackCount = 0

import csv

# with open('names.csv', 'w', newline='') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
# #     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
# a = "aa"
# print(type(a))

# csvData = [["perssssion", 'Age'], ['Peter', '22'], ['Jasmine', '21'], ['Sam', '24']]

# with open('person.csv', 'w') as csvFile:
#     writer = csv.writer(csvFile)
#     spamwriter.writerows(csvData)

# csvFile.close()


import csv

# csvData = [['Person', 'Age'], ['Peter', '22'], ['Jasmine', '21'], ['Sam', '24']]

# with open('person.csv', 'w') as csvFile:
#     writer = csv.writer(csvFile)
#     writer.writerows(csvData)

# csvFile.close()

a = "ss"
data = [{'mountain': a , 'height': '8848'},
        {'mountain': 'K2 ', 'height': '8611'},
        {'mountain': 'Kanchenjunga', 'height': '8586'}]
print(data[0])
with open('person.csv', 'w') as csvFile:
    fields = ['mountain', 'height']
    writer = csv.DictWriter(csvFile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)

print("writing completed")

csvFile.close()
