from scipy import integrate
import matplotlib.pyplot as plt
import numpy as np
from  dimes import *

# x = np.linspace(-2, 2, num=20)
# y = x
# y_int = integrate.cumtrapz(y, x, initial=0)
# plt.plot(x, y_int, 'ro', x, y[0] + 0.5 * x**2, 'b-')
# plt.show()
x=[0,0,1,0,0,0,0,0,0,0]
# xcxc=(1 / 3.0)
# print(xcxc)
# sum1=0
# for i in range(len(x)):
    
        
#     sum1 +=x[i]
#     # sum2 += sum1
#     # print(x[i])
    
#     fx=sum1*xcxc
#     z.append(sum1)


xx = np.linspace(0, len(x) )
y = xx
y_int = integrate.cumtrapz(y, xx, initial=0)
# plt.subplot(212)


zz=Integ(x)
print(zz)

plt.figure(1)

plt.subplot(211)
plt.plot(x)
plt.title('init ')

plt.subplot(212)
plt.plot(y_int)
plt.title('integral ')

plt.show()

    