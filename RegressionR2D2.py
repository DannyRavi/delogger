from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn import datasets
import pandas as pd
import numpy as np

x = np.arange(1,10)
y= np.array([28, 25, 26, 31, 32, 29, 30, 35, 36])
plt.scatter(x,y)
plt.show()

x = x.reshape(-1,1)
y = y.reshape(-1,1)
reg = LinearRegression()
reg.fit(x,y)
yhat = reg.predict(x)
plt.scatter(x,y)
plt.plot(x,yhat)
plt.show()