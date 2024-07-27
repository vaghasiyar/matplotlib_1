##Matplotlib Pie Charts

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
plt.pie(y)
plt.show() 



#Labels


import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels = mylabels)
plt.show() 



#Start Angle

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels = mylabels, startangle = 90)
plt.show() 


#Explode

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]
plt.pie(y, labels = mylabels, explode = myexplode)
plt.show() 




#Shadow

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]
plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show() 


#Colors

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["black", "hotpink", "b", "#4CAF50"]
plt.pie(y, labels = mylabels, colors = mycolors)
plt.show() 




#Legend

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels = mylabels)
plt.legend()
plt.show() 




#Legend With Header

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")
plt.show() 


#-------------------------------------------------------------------------------------------






#Plot a pie chart in Python using Matplotlib

# Import libraries
from matplotlib import pyplot as plt
import numpy as np

cars = ['AUDI', 'BMW', 'FORD',
		'TESLA', 'JAGUAR', 'MERCEDES']
data = [23, 17, 35, 29, 12, 41]
fig = plt.figure(figsize=(10, 7))
plt.pie(data, labels=cars)
plt.show()




import numpy as np
import matplotlib.pyplot as plt


cars = ['AUDI', 'BMW', 'FORD',
		'TESLA', 'JAGUAR', 'MERCEDES']

data = [23, 17, 35, 29, 12, 41]

explode = (0.1, 0.0, 0.2, 0.3, 0.0, 0.0)

colors = ("orange", "cyan", "brown",
		"grey", "indigo", "beige")

wp = {'linewidth': 1, 'edgecolor': "green"}

def func(pct, allvalues):
	absolute = int(pct / 100.*np.sum(allvalues))
	return "{:.1f}%\n({:d} g)".format(pct, absolute)

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(data,
								autopct=lambda pct: func(pct, data),
								explode=explode,
								labels=cars,
								shadow=True,
								colors=colors,
								startangle=90,
								wedgeprops=wp,
								textprops=dict(color="magenta"))
ax.legend(wedges, cars,
		title="Cars",
		loc="center left",
		bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")
ax.set_title("Customizing pie chart")
plt.show()



#Nested Pie Chart
from matplotlib import pyplot as plt
import numpy as np
size = 6
cars = ['AUDI', 'BMW', 'FORD',
		'TESLA', 'JAGUAR', 'MERCEDES']

data = np.array([[23, 16], [17, 23],
				[35, 11], [29, 33],
				[12, 27], [41, 42]])

norm = data / np.sum(data)*2 * np.pi

left = np.cumsum(np.append(0,
						norm.flatten()[:-1])).reshape(data.shape)

cmap = plt.get_cmap("tab20c")
outer_colors = cmap(np.arange(6)*4)
inner_colors = cmap(np.array([1, 2, 5, 6, 9,
							10, 12, 13, 15,
							17, 18, 20]))

fig, ax = plt.subplots(figsize=(10, 7),
					subplot_kw=dict(polar=True))

ax.bar(x=left[:, 0],
	width=norm.sum(axis=1),
	bottom=1-size,
	height=size,
	color=outer_colors,
	edgecolor='w',
	linewidth=1,
	align="edge")

ax.bar(x=left.flatten(),
	width=norm.flatten(),
	bottom=1-2 * size,
	height=size,
	color=inner_colors,
	edgecolor='w',
	linewidth=1,
	align="edge")

ax.set(title="Nested pie chart")
ax.set_axis_off()
plt.show()



#--------------------------------------------------------------------------------------


#Radially displace pie chart wedge in Matplotlib

import matplotlib.pyplot as plt 

 
continents = ['Asia', 'Europe', 'North America', 
			'South America','Australia', 
			'Africa','Antarctica'] 
area = [25, 20, 15, 10,15,10,5] 
explode = (0.1, 0, 0.1, 0,0.1,0.1,0.1) 

plt.pie(area, explode = explode, labels = continents, 
		autopct = '%1.1f%%',startangle = 0, 
		wedgeprops = {"edgecolor" : "black", 
					'linewidth' : 2, 
					'antialiased': True}) 
plt.axis('equal') 

plt.show() 




#Example 2:

import matplotlib.pyplot as plt 

sales = ['Product A', 'Product B', 
		'Product C', 'Product D'] 
profit = [20, 30, 25, 20] 
explode = (0.1, 0, 0.1, 0) 
plt.pie(profit, explode = explode, labels = sales, 
		autopct = '%1.1f%%',shadow = True, 
		startangle = 90, 
		wedgeprops = {"edgecolor":"black", 
					'linewidth': 2, 
					'antialiased': True})  
plt.axis('equal') 

plt.show() 
