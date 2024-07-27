#Three-dimensional Plotting in Python using Matplotlib


#3-Dimensional Line Graph Using Matplotlib


from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

ax = plt.axes(projection ='3d')
z = np.linspace(0, 1, 100)
x = z * np.sin(25 * z)
y = z * np.cos(25 * z)
ax.plot3D(x, y, z, 'green')
ax.set_title('3D line plot geeks for geeks')
plt.show()



#3-Dimensional Scattered Graph Using Matplotlib


from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

ax = plt.axes(projection ='3d')

z = np.linspace(0, 1, 100)
x = z * np.sin(25 * z)
y = z * np.cos(25 * z)
c = x + y
ax.scatter(x, y, z, c = c)

ax.set_title('3d Scatter plot geeks for geeks')
plt.show()



#Surface Graphs using Matplotlib library  

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

x = np.outer(np.linspace(-2, 2, 10), np.ones(10))
y = x.copy().T
z = np.cos(x ** 2 + y ** 3)

fig = plt.figure()

ax = plt.axes(projection='3d')

ax.plot_surface(x, y, z, cmap='viridis',\
				edgecolor='green')
ax.set_title('Surface plot geeks for geeks')
plt.show()


#Wireframes graph using Matplotlib library  

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
	return np.sin(np.sqrt(x ** 2 + y ** 2))

x = np.linspace(-1, 5, 10)
y = np.linspace(-1, 5, 10)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = plt.axes(projection ='3d')
ax.plot_wireframe(X, Y, Z, color ='green')
ax.set_title('wireframe geeks for geeks');

def function(x, y):
	return np.sin(np.sqrt(x ** 2 + y ** 2))


x = np.linspace(-10, 10, 40)
y = np.linspace(-10, 10, 40)

X, Y = np.meshgrid(x, y)
Z = function(X, Y)

fig = plt.figure(figsize=(10, 8))
ax = plt.axes(projection='3d')

ax.plot_surface(X, Y, Z, cmap='cool', alpha=0.8)

ax.set_title('3D Contour Plot of function(x, y) =\
				sin(sqrt(x^2 + y^2))', fontsize=14)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_zlabel('z', fontsize=12)

plt.show()



#Plotting Möbius strip In Python 


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

R = 2

u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(-1, 1, 100)
u, v = np.meshgrid(u, v)
x = (R + v*np.cos(u/2)) * np.cos(u)
y = (R + v*np.cos(u/2)) * np.sin(u)
z = v * np.sin(u/2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x, y, z, alpha=0.5)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Möbius Strip')

ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])
plt.show()



#-------------------------------------------------------------------------------


#3D Scatter Plotting in Python using Matplotlib

# Import libraries
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


z = np.random.randint(100, size =(50))
x = np.random.randint(80, size =(50))
y = np.random.randint(60, size =(50))

fig = plt.figure(figsize = (10, 7))
ax = plt.axes(projection ="3d")

ax.scatter3D(x, y, z, color = "green")
plt.title("simple 3D scatter plot")

plt.show()




#Example 2 : For better understanding Let’s take another example.


from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

z = 4 * np.tan(np.random.randint(10, size =(500))) + np.random.randint(100, size =(500))
x = 4 * np.cos(z) + np.random.normal(size = 500)
y = 4 * np.sin(z) + 4 * np.random.normal(size = 500)

fig = plt.figure(figsize = (16, 9))
ax = plt.axes(projection ="3d")

ax.grid(b = True, color ='grey', 
		linestyle ='-.', linewidth = 0.3, 
		alpha = 0.2) 


my_cmap = plt.get_cmap('hsv')

sctt = ax.scatter3D(x, y, z,
					alpha = 0.8,
					c = (x + y + z), 
					cmap = my_cmap, 
					marker ='^')

plt.title("simple 3D scatter plot")
ax.set_xlabel('X-axis', fontweight ='bold') 
ax.set_ylabel('Y-axis', fontweight ='bold') 
ax.set_zlabel('Z-axis', fontweight ='bold')
fig.colorbar(sctt, ax = ax, shrink = 0.5, aspect = 5)

plt.show()





#-----------------------------------------------------------------------------------------


#3D Surface plotting in Python using Matplotlib

# Import libraries
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


x = np.outer(np.linspace(-3, 3, 32), np.ones(32))
y = x.copy().T # transpose
z = (np.sin(x **2) + np.cos(y **2) )

fig = plt.figure(figsize =(14, 9))
ax = plt.axes(projection ='3d')

ax.plot_surface(x, y, z)
plt.show()



#Gradient surface Plot
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

x = np.outer(np.linspace(-3, 3, 32), np.ones(32))
y = x.copy().T # transpose
z = (np.sin(x **2) + np.cos(y **2) )

fig = plt.figure(figsize =(14, 9))
ax = plt.axes(projection ='3d')

my_cmap = plt.get_cmap('hot')

surf = ax.plot_surface(x, y, z,
					cmap = my_cmap,
					edgecolor ='none')

fig.colorbar(surf, ax = ax,
			shrink = 0.5, aspect = 5)

ax.set_title('Surface plot')

plt.show()



#3D surface Plot having 2D contour plot projections


from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

x = np.outer(np.linspace(-3, 3, 32), np.ones(32))
y = x.copy().T # transpose
z = (np.sin(x **2) + np.cos(y **2) )

fig = plt.figure(figsize =(14, 9))
ax = plt.axes(projection ='3d')

my_cmap = plt.get_cmap('hot')

surf = ax.plot_surface(x, y, z, 
					rstride = 8,
					cstride = 8,
					alpha = 0.8,
					cmap = my_cmap)
cset = ax.contourf(x, y, z,
				zdir ='z',
				offset = np.min(z),
				cmap = my_cmap)
cset = ax.contourf(x, y, z,
				zdir ='x',
				offset =-5,
				cmap = my_cmap)
cset = ax.contourf(x, y, z, 
				zdir ='y',
				offset = 5,
				cmap = my_cmap)
fig.colorbar(surf, ax = ax, 
			shrink = 0.5,
			aspect = 5)

ax.set_xlabel('X-axis')
ax.set_xlim(-5, 5)
ax.set_ylabel('Y-axis')
ax.set_ylim(-5, 5)
ax.set_zlabel('Z-axis')
ax.set_zlim(np.min(z), np.max(z))
ax.set_title('3D surface having 2D contour plot projections')

plt.show()



#----------------------------------------------------------------------------





#3D Wireframe plotting in Python using Matplotlib


# importing modules
from mpl_toolkits.mplot3d import axes3d
from matplotlib import pyplot 

fig = pyplot.figure()
wf = fig.add_subplot(111, projection='3d')
x, y, z = axes3d.get_test_data(0.05)
wf.plot_wireframe(x,y,z, rstride=2, 
				cstride=2,color='green')

wf.set_title('Example 1')
pyplot.show()





from mpl_toolkits import mplot3d
import numpy 
from matplotlib import pyplot
a = numpy.linspace(-5, 5, 25)
b = numpy.linspace(-5, 5, 25)
x, y = numpy.meshgrid(a, b)
z = numpy.sin(numpy.sqrt(x**2 + y**2))

fig = pyplot.figure()
wf = pyplot.axes(projection ='3d')
wf.plot_wireframe(x, y, z, color ='green')

wf.set_title('Example 2')
pyplot.show()







#--------------------------------------------------------------------------






#3D Contour Plotting in Python using Matplotlib



#Example 1:


from mpl_toolkits import mplot3d 
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import cm 
import math 

x = [i for i in range(0, 200, 100)] 
y = [i for i in range(0, 200, 100)] 

X, Y = np.meshgrid(x, y) 
Z = [] 
for i in x: 
	t = [] 
	for j in y: 
		t.append(math.cos(math.sqrt(i*2+j*2))) 
	Z.append(t) 

fig = plt.figure() 
ax = plt.axes(projection='3d') 
ax.contour3D(X, Y, Z, 50, cmap=cm.cool) 
ax.set_xlabel('a') 
ax.set_ylabel('b') 
ax.set_zlabel('c') 
ax.set_title('3D contour for cosine') 
plt.show() 





#Example 2: Let’s look at another 3d diagram for better understanding of the concept. This time, of a 3d tan function.

from mpl_toolkits import mplot3d 
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import cm 
import math 

x = [i for i in range(0, 200, 100)] 
y = [i for i in range(0, 200, 100)] 

X, Y = np.meshgrid(x, y) 
Z = [] 
for i in x: 
	t = [] 
	for j in y: 
		t.append(math.tan(math.sqrt(i*2+j*2))) 
	Z.append(t) 

fig = plt.figure() 
ax = plt.axes(projection='3d') 
ax.contour3D(X, Y, Z, 50, cmap=cm.cool) 
ax.set_xlabel('a') 
ax.set_ylabel('b') 
ax.set_zlabel('c') 
ax.set_title('3D contour for tan') 
plt.show() 




#------------------------------------------------------------------------------------



#Tri-Surface Plot in Python using Matplotlib



#Example 1: Let’s create a basic Tri-Surface plot using the ax.plot_trisurf() function. 


# Import libraries
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


z = np.linspace(0, 50000, 100)
x = np.sin(z)
y = np.cos(z) 

fig = plt.figure(figsize =(14, 9))
ax = plt.axes(projection ='3d')
ax.plot_trisurf(x, y, z,
				linewidth = 0.2,
				antialiased = True);
plt.show()




#Example 2 : For better understanding Let’s take another example. 


# Import libraries
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt 
import numpy as np 


r = np.linspace(0.125, 1.0, 100) 
a = np.linspace(0, 2 * np.pi, 
				100,
				endpoint = False) 

a = np.repeat(a[..., np.newaxis], 100, axis = 1) 

x = np.append(0, (r * np.cos(a))) 
y = np.append(0, (r * np.sin(a))) 
z = (np.sin(x ** 4) + np.cos(y ** 4)) 

fig = plt.figure(figsize =(16, 9)) 
ax = plt.axes(projection ='3d') 

my_cmap = plt.get_cmap('hot')

trisurf = ax.plot_trisurf(x, y, z,
						cmap = my_cmap,
						linewidth = 0.2, 
						antialiased = True,
						edgecolor = 'grey') 
fig.colorbar(trisurf, ax = ax, shrink = 0.5, aspect = 5)
ax.set_title('Tri-Surface plot')

ax.set_xlabel('X-axis', fontweight ='bold') 
ax.set_ylabel('Y-axis', fontweight ='bold') 
ax.set_zlabel('Z-axis', fontweight ='bold')
plt.show()




#------------------------------------------------------------------------



#Surface plots and Contour plots in Python



#Example 1:

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D 

a = np.array([1, 2, 3]) 
b = np.array([4, 5, 6, 7]) 

a, b = np.meshgrid(a, b) 

# surface plot for a + b 
fig = plt.figure() 
axes = fig.gca(projection ='3d') 
axes.plot_surface(a, b, a + b) 

plt.show() 



#Example 2:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D 

a = np.array([1, 2, 3]) 
b = np.array([4, 5, 6, 7]) 
a, b = np.meshgrid(a, b) 

a = np.arange(-1, 1, 0.02) 
b = a 
a, b = np.meshgrid(a, b) 
fig = plt.figure() 
axes = fig.gca(projection ='3d') 
axes.plot_surface(a, b, a**2 + b**2) 
plt.show() 






#Creating Contour plots



#Example 1:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D 

a = np.array([1, 2, 3]) 
b = np.array([4, 5, 6, 7]) 

a, b = np.meshgrid(a, b) 

fig = plt.figure() 
axes = fig.gca(projection ='3d') 
axes.contour(a, b, a + b) 

plt.show() 




#Example 2:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D 

a = np.array([1, 2, 3]) 
b = np.array([4, 5, 6, 7]) 

a, b = np.meshgrid(a, b) 
a = np.arange(-1, 1, 0.02) 
b = a 
a, b = np.meshgrid(a, b) 

fig = plt.figure() 
axes = fig.gca(projection ='3d') 
axes.contour(a, b, a**2 + b**2) 

plt.show() 





#------------------------------------------------------------------------------------






#How to change angle of 3D plot in Python?

import numpy as np 
from matplotlib import pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D 
from math import sin, cos 

fig = plt.figure(figsize = (8,8)) 
ax = fig.add_subplot(111, projection = '3d') 

y = np.linspace(-1, 1, 200) 
x = np.linspace(-1, 1, 200) 
x,y = np.meshgrid(x, y) 

z = x + y 

a = 50

t = np.transpose(np.array([x, y, z]), ( 1, 2, 0)) 

m = [[cos(a), 0, sin(a)],[0, 1, 0], 
	[-sin(a), 0, cos(a)]] 

X,Y,Z = np.transpose(np.dot(t, m), (2, 0, 1)) 

ax.set_xlabel('X') 
ax.set_ylabel('Y') 
ax.set_zlabel('Z') 

ax.plot_surface(X,Y,Z, alpha = 0.5, 
				color = 'red') 

plt.show()





#-----------------------------------------------------------------------------------------




#How to animate 3D Graph using Matplotlib?



#Example 1: In this example, we plot a square wave, and we will see its 360-degree view.


from numpy import linspace
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy import signal

fig = plt.figure(figsize = (8, 8))
ax = plt.axes(projection = '3d')

t = np.linspace(0, 1, 1000, endpoint = True)
ax.plot3D(t, signal.square(2 * np.pi * 5 * t))

for angle in range(0, 360):
    ax.view_init(angle, 30)
    plt.draw()
    plt.pause(.001)
	
plt.show()




#Example 2: In this example, we plot a spiral graph, and we will see its 360-degree view


from numpy import linspace
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy import signal

fig = plt.figure(figsize = (8,8))
ax = plt.axes(projection='3d')

z = np.linspace(0, 15, 1000)
x = np.sin(z)
y = np.cos(z)
ax.plot3D(x, y, z, 'green')

for angle in range(0, 360):
	ax.view_init(angle, 30)
	plt.draw()
	plt.pause(.001)

plt.show()




#Example 3: In this example, we will display the Parabola Graph.


from numpy import linspace
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy import signal

fig = plt.figure(figsize = (8,8))
ax = plt.axes(projection = '3d')
color_cycle = plt.rcParams['axes.prop_cycle']()
x = linspace(0, 1, 51)
a = x*( 1 - x) 
b = 0.25 - a 
c = x*x*(1 - x)
d = 0.25-c 

ax.plot3D(x, a, **next(color_cycle))

for angle in range(0, 360):
    ax.view_init(angle, 30)
    plt.draw()
    plt.pause(.001)

plt.show()
