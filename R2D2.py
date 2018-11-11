
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
## todo import matplotlib.pyplot as plt  
## todo # matplotlib inline
## todo import numpy as np  
## todo from sklearn.cluster import KMeans  
## todo 
## todo X = np.array([[5,3],  
## todo      [10,15],
## todo      [15,12],
## todo      [24,10],
## todo      [30,45],
## todo      [85,70],
## todo      [71,80],
## todo      [60,78],
## todo      [55,52],
## todo      [80,91],])
## todo 
## todo YY = []
## todo Y = range(len(X))
## todo for i in Y:
## todo   YY.append(i)
## todo 
## todo print(X)  
## todo print("X") 
## todo print(type(X))
## todo print(YY) 
## todo # plt.scatter(X[:,0],X[:,1], label='True Position')  
## todo kmeans = KMeans(n_clusters=2)  
## todo kmeans.fit(X) 
## todo print(kmeans.cluster_centers_)  
## todo print(kmeans.labels_)  
## todo # plt.scatter(YY,X[:,1], c=kmeans.labels_, cmap='rainbow')  
## todo # plt.show()
## todo 
## todo print("***")
## todo Tx = np.arange(0, 10)
## todo Tx[:5]=0
## todo Tx[5:]=1
## todo print (Tx)


#? from sklearn.cluster import MeanShift
#? import matplotlib.pyplot as plt  
#? # matplotlib inline
#? import numpy as np  
#? from sklearn.datasets import load_iris
#? iris = load_iris()
#? 
#? x = iris.data
#? ms = MeanShift()
#? ms.fit(x)
#? labels = ms.labels_
#? cluster_center = ms.cluster_centers_
#? n_cluster = len(np.unique(labels))
#? print('Number of estimated cluster:' ,n_cluster)
#? plt.scatter(x[:,0], x[:,1], c=labels)
#? plt.scatter(cluster_center[:,0], cluster_center[:,1], marker='x', s=150, linewidth=5 )
#? plt.show()


# X = [[0], [1], [2], [3]]
# y = [0, 0, 1, 1]
# from sklearn.neighbors import KNeighborsClassifier
# neigh = KNeighborsClassifier(n_neighbors=3)
# neigh.fit(X, y) 

# print(neigh.predict([[1.1]]))

# print(neigh.predict([[0.9]]))


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")
from sklearn import svm

x = [1, 5, 1.5, 8, 1, 9]
y = [2, 8, 1.8, 8, 0.6, 11]

plt.scatter(x,y)
plt.show()

X = np.array([[1,2],
             [5,8],
             [1.5,1.8],
             [8,8],
             [1,0.6],
             [9,11]])

y = [0,1,0,1,0,1]

clf = svm.SVC(kernel='linear', C = 1.0)
clf.fit(X,y)

test = np.array([0.58, 0.76])
print (test)       # Produces: [ 0.58  0.76]
print (test.shape) # Produces: (2,) meaning 2 rows, 1 col

test = test.reshape(1, -1)
print (test)      # Produces: [[ 0.58  0.76]]
print (test.shape) # Produces (1, 2) meaning 1 row, 2 cols

print(clf.predict(test)) # Produces [0], as expected

