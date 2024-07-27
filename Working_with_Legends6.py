##Working with Legends


#Matplotlib.pyplot.legend() in Python

import numpy as np 
import matplotlib.pyplot as plt 

x = [1,2,3,4,5] 
y = [1,5,8,9,12] 
plt.plot(x, y) 
plt.legend(['single element']) 
plt.show() 



#Change the Position of the Legend



y1 = [2, 4, 5.5]
y2 = [1, 2.5, 6]
plt.plot(y1)
plt.plot(y2)
plt.legend(["blue", "black"], loc="lower right")

plt.show()



#Combine Multiple labels in legend



x = np.arange(5)

y1 = [1, 2, 3, 4, 5,]
y2 = [2,5,6,10,25]
plt.plot(x, y1, label='Numbers')
plt.plot(x, y2, label='Square of numbers')
plt.legend()
plt.show()



#Plotting Sine and Cosine Functions with Legends in Matplotlib


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
fig, ax = plt.subplots()

ax.plot(x, np.sin(x), '--b', label='Sine')
ax.plot(x, np.cos(x), c='r', label='Cosine')
ax.axis('equal')

leg = ax.legend(loc="lower left")



#Place the Legend Outside the Plot in Matplotlib

import numpy as np
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5, 6, 7, 8]

y1 = [0, 3, 6, 9, 12, 15, 18, 21, 24]
y2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]

plt.plot(y1, label="y = x")
plt.plot(y2, label="y = 3x")

plt.legend(bbox_to_anchor=(0.75, 1.15), ncol=2)
plt.show()


