##Matplotlib Pyplot


#Pyplot

import matplotlib.pyplot as plt
import numpy as np

apoints = np.array([0, 6])
bpoints = np.array([0, 250])
plt.plot(apoints, bpoints)
plt.show()




#How to Add Title to Subplots in Matplotlib?

# Example 1: (Using set_title() method)
import numpy as np
import matplotlib.pyplot as plt

x=np.array([5,6,7,8,9,10])

fig, ax = plt.subplots(2, 2)

ax[0,0].plot(x, x)
ax[1,0].plot(x, x*2)
ax[0,1].plot(x, x*x)
ax[1,1].plot(x, x*x*x)

ax[0,0].set_title("Linear")
ax[1,0].set_title("Double")
ax[0,1].set_title("Square")
ax[1,1].set_title("Cube")

fig.tight_layout()
plt.show()


#Example 2: (Using title.set_text() method)

x=np.array([1, 2, 3, 4, 5])
fig, ax = plt.subplots(2, 2)
ax[0, 0].plot(x, x)
ax[0, 1].plot(x, x*2)
ax[1, 0].plot(x, x*x)
ax[1, 1].plot(x, x*x*x)
 
ax[0, 0].title.set_text("Linear")
ax[0, 1].title.set_text("Double")
ax[1, 0].title.set_text("Square")
ax[1, 1].title.set_text("Cube")
 
fig.tight_layout()
plt.show()



#Example 3: (Using plt.gca().set_title() method)


x=np.array([5,6,7,8,9,10])
 
fig, ax = plt.subplots(2, 2)
 
title = ["Linear", "Double", "Square", "Cube"]
y = [x, x*2, x*x, x*x*x] 
for i in range(4):      
    plt.subplot(2, 2, i+1) 
    plt.plot(x, y[i]) 
    plt.gca().set_title(title[i]) 
fig.tight_layout()
plt.show()



#Example 4: (Using plt.gca().title.set_text() method)


x=np.array([5,6,7,8,9,10])

fig, ax = plt.subplots(2, 2)

title = ["Linear","Double","Square","Cube"]
y = [x, x*2, x*x, x*x*x]

for i in range(4):
	plt.subplot(2, 2, i+1)
	plt.plot(x, y[i])
	plt.gca().title.set_text(title[i]) 
fig.tight_layout()
plt.show()





#-------------------------------------------------------------------------------------


#How to Set a Single Main Title for All the Subplots in Matplotlib?


#Setting a Single Title for All the Subplots


# importing packages
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(2, 2)
ax[0][0].plot(np.random.randint(0, 5, 5), np.random.randint(0, 5, 5))
ax[0][1].plot(np.random.randint(0, 5, 5), np.random.randint(0, 5, 5))
ax[1][0].plot(np.random.randint(0, 5, 5), np.random.randint(0, 5, 5))
ax[1][1].plot(np.random.randint(0, 5, 5), np.random.randint(0, 5, 5))
fig.suptitle(' Set a Single Main Title for All the Subplots ', fontsize=30)

plt.show()











