##Matplotlib Plotting




#Plotting a and b points

import matplotlib.pyplot as plt
import numpy as np

apoints = np.array([1, 15])
bpoints = np.array([5, 20])
plt.plot(apoints, bpoints)
plt.show()



#Plotting Without Line

apoints = np.array([1,15])
bpoints = np.array([5,20])
plt.plot(apoints, bpoints, 'o')
plt.show()


#Multiple Points

xpoints = np.array([1,2,5,8,10,12,18])
ypoints = np.array([3,8,5,2,4,10,17])
plt.plot(xpoints, ypoints)
plt.show()



#Default X-Points

bpoints = np.array([1,5,7,10,6,2,7])

plt.plot(bpoints)
plt.show()