##Matplotlib Markers



#Markers

#You can use the keyword argument marker to emphasize each point with a specified marker:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([5,8,2,10,4,1,13])
plt.plot(ypoints, marker = '5')
plt.show()

'''
Marker Reference

You can choose any of these markers:
Marker 	Description
'o' 	Circle 	
'*' 	Star 	
'.' 	Point 	
',' 	Pixel 	
'x' 	X 	
'X' 	X (filled) 	
'+' 	Plus 	
'P' 	Plus (filled) 	
's' 	Square 	
'D' 	Diamond 	
'd' 	Diamond (thin) 	
'p' 	Pentagon 	
'H' 	Hexagon 	
'h' 	Hexagon 	
'v' 	Triangle Down 	
'^' 	Triangle Up 	
'<' 	Triangle Left 	
'>' 	Triangle Right 	
'1' 	Tri Down 	
'2' 	Tri Up 	
'3' 	Tri Left 	
'4' 	Tri Right 	
'|' 	Vline 	
'_' 	Hline

'''


#Format Strings fmt


#This parameter is also called fmt, and is written with this syntax:
ypoints = np.array([5,8,2,10,4,1,13])
plt.plot(ypoints, 'o--m')
plt.show()


'''

Line Reference
Line Syntax 	Description
'-' 	Solid line 	
':' 	Dotted line 	
'--' 	Dashed line 	
'-.' 	Dashed/dotted line

'''



'''

Color Reference
Color Syntax 	Description
'r' 	Red 	
'g' 	Green 	
'b' 	Blue 	
'c' 	Cyan 	
'm' 	Magenta 	
'y' 	Yellow 	
'k' 	Black 	
'w' 	White

'''



#Marker Size


ypoints = np.array([5,8,2,10,4,1,13])
plt.plot(ypoints, marker = '*', ms = 25)
plt.show()



#Marker Color

ypoints = np.array([5,8,2,10,4,1,13])
plt.plot(ypoints, marker = '*', ms = 25, mec = 'k')
plt.show()

#You can use the keyword argument markerfacecolor or the shorter mfc to set the color inside the edge of the markers:

ypoints = np.array([5,8,2,10,4,1,13])
plt.plot(ypoints, marker = '*', ms = 25, mfc = 'k')
plt.show()


#Use both the mec and mfc arguments to color the entire marker:
ypoints = np.array([5,8,2,10,4,1,13])
plt.plot(ypoints, marker = '*', ms = 25, mec = 'k', mfc = 'r')
plt.show()


ypoints = np.array([5,8,2,10,4,1,13])
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')
plt.show()







#-------------------------------------------------------------------

#Example 2: Here, we are creating data to plot our graph and using a marker.

import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(1, 5, figsize=(20, 5))

x1 = [1, 2, 3, 4, 5, 6]
y1 = [45, 34, 30, 45, 50, 38]
y2 = [36, 28, 30, 40, 38, 48]
z1 = [78, 56, 98, 56, 95, 45]
Z2 = [65, 68, 78, 36, 30, 58]
a1 = [98, 56, 23, 78, 56, 45]

labels = ["student 1", "student 2", "student 3", "student 4", "student 5"]

fig.suptitle('Student Marks', fontsize=20)

l1, = ax1.plot(x1, y1, 'o-', color='g')
l2, = ax2.plot(x1, y2, 'o-')
l3, = ax3.plot(x1, z1, 'o-', color='g')
l4, = ax4.plot(x1, Z2, 'o-')
l5, = ax5.plot(x1, a1, 'o-', color='g')

fig.legend([l1, l2, l3, l4, l5], labels=labels, loc="upper right")
plt.subplots_adjust(right=0.9)

plt.show()



#How to Turn Off the Axes for Subplots in Matplotlib?


import matplotlib.pyplot as plt 
import matplotlib.tri as mtri 
import numpy as np 
	
a = np.asarray([0, 1, 2, 3, 0.5, 
				1.5, 2.5, 1, 2, 
				1.5]) 

b = np.asarray([0, 0, 0, 0, 1.0, 
				1.0, 1.0, 2, 2, 
				3.0]) 

triangles = [[0, 1, 4], [1, 5, 4], 
			[2, 6, 5], [4, 5, 7], 
			[5, 6, 8], [5, 8, 7], 
			[7, 8, 9], [1, 2, 5], 
			[2, 3, 6]] 

triang = mtri.Triangulation(a, b, triangles) 
z = np.cos(1.5 * a) * np.cos(1.5 * b) 
	
fig, axs = plt.subplots() 
axs.tricontourf(triang, z) 
axs.triplot(triang, 'go-', color ='black') 

axs.set_axis_off()

axs.set_title('Triangle') 

plt.show() 






#Method 2: Using matplotlib.axes.Axes.set_axis_off()

import matplotlib.pyplot as plt 
import numpy as np 
     
geeksx = np.array([25.50, 120.28, 30.25, 
                26.00, 70.105, 7.2, 
                20.00,80.56,100.00]) 
 
geeksy = np.array([25.50, 120.28, 30.25, 
                26.00, 70.105, 7.2, 
                20.00,80.56,100.00]) 

fig, ax = plt.subplots() 
ax.xcorr(geeksx, geeksy, maxlags = 6, 
        color ="green") 
 
ax.set_axis_off() 
ax.set_title('Music series graph') 
plt.show()


#Method 3: Using matplotlib.pyplot.axis()

import matplotlib.pyplot as plt

x = [-5,-6,-7,-8,-9, 0, 5,6,7,8,9]
y = []

for i in range(len(x)):
	y.append(max(0, x[i]))

ax = plt.plot(x, y, color='black')

#plt.axis('on')
plt.axis('off')

plt.title("ReLU function graph")

plt.show()




#How to Create ifferent Subplot Sizes in Matplotlib?



import matplotlib.pyplot as plt
from matplotlib import gridspec
import numpy as np

fig = plt.figure()
fig.set_figheight(8)

fig.set_figwidth(8)
spec = gridspec.GridSpec(ncols=2, nrows=2,
						width_ratios=[2, 1], wspace=0.5,
						hspace=0.5, height_ratios=[1, 2])
x = np.arange(0, 10, 0.1)
y = np.cos(x)

ax0 = fig.add_subplot(spec[0])
ax0.plot(x, y)

ax1 = fig.add_subplot(spec[1])
ax1.plot(x, y)

ax2 = fig.add_subplot(spec[2])
ax2.plot(x, y)

ax3 = fig.add_subplot(spec[3])
ax3.plot(x, y)

plt.show()
