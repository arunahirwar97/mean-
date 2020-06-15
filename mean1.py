#find the mean given data
import numpy as np
# question 2 
x = np.array([8,10,15,20])
y = np.array([5,8,8,4])
xy=[]
for i in range(len(x)):
    xx = x[i]*y[i]
    xy.append(xx)
    
y = y.sum() 
xy = np.array(xy)
mean = xy.sum()/y

print("mean : ", mean)
