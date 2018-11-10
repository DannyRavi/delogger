
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


#! import os
#! import shutil
#! src = 'E:/Danny/Ground Sensor/Delogger/delogger/BigData/'
#! dest = 'E:/Danny/Ground Sensor/Delogger/delogger/OutputAlgoritm'
#! src_files = os.listdir(src)
#! 
#! for file_name in src_files:
#!     full_file_name = os.path.join(src, file_name)
#!     new_file_name = "uu "+file_name
#!     if (os.path.isfile(full_file_name)):
#!         shutil.copy2(full_file_name, dest)
#!         dst_file = os.path.join(dest, full_file_name)
#!         new_dst_file_name = os.path.join(dest, new_file_name)
#!         os.rename(dst_file, new_dst_file_name)
#! 



# In Windows
# os.system('copy instructable.txt dd2.txt')
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



# csvData = [['Person', 'Age'], ['Peter', '22'], ['Jasmine', '21'], ['Sam', '24']]

# with open('person.csv', 'w') as csvFile:
#     writer = csv.writer(csvFile)
#     writer.writerows(csvData)

# csvFile.close()

# a = "ss"
# data = [{'mountain': a , 'height': '8848'},
#         {'mountain': 'K2 ', 'height': '8611'},
#         {'mountain': 'Kanchenjunga', 'height': '8586'}]
# print(data[0])
# with open('person.csv', 'w') as csvFile:
#     fields = ['mountain', 'height']
#     writer = csv.DictWriter(csvFile, fieldnames=fields)
#     writer.writeheader()
#     writer.writerows(data)

# print("writing completed")

# csvFile.close()
import matplotlib.pyplot as plt  
# matplotlib inline
import numpy as np  
from sklearn.cluster import KMeans  

X = np.array([[5,3],  
     [10,15],
     [15,12],
     [24,10],
     [30,45],
     [85,70],
     [71,80],
     [60,78],
     [55,52],
     [80,91],])

YY = []
Y = range(len(X))
for i in Y:
  YY.append(i)

print(X)  
print("X") 
print(type(X))
print(YY) 
# plt.scatter(X[:,0],X[:,1], label='True Position')  
kmeans = KMeans(n_clusters=2)  
kmeans.fit(X) 
print(kmeans.cluster_centers_)  
print(kmeans.labels_)  
# plt.scatter(YY,X[:,1], c=kmeans.labels_, cmap='rainbow')  
# plt.show()

print("***")
Tx = np.arange(0, 10)
Tx[:5]=0
Tx[5:]=1
print (Tx)