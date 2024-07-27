##Matplotlib Line

#Linestyle

#You can use the keyword argument linestyle, or shorter ls, to change the style of the plotted line:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([5,8,2,10,4,1,13])
plt.plot(ypoints, linestyle = 'dotted')
plt.show()


ypoints = np.array([5,8,2,10,4,1,13])
plt.plot(ypoints, linestyle = 'dashed')
plt.show()





#Shorter Syntax

'''
linestyle can be written as ls.

dotted can be written as :.

dashed can be written as --.

'''


ypoints = np.array([5,8,2,10,4,1,13])
plt.plot(ypoints, ls = ':')
plt.show()


#Line Styles


'''
Style 	Or
'solid' (default) 	'-' 	
'dotted' 	':' 	
'dashed' 	'--' 	
'dashdot' 	'-.' 	
'None' 	'' or ' '
'''



#-----------------------------------------------------


#Line Color


import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([5,8,2,10,4,1,13])
plt.plot(ypoints, color = 'r')
plt.show()


ypoints = np.array([5,8,2,10,4,1,13])
plt.plot(ypoints, c = '#4CAF50')
plt.show()


ypoints = np.array([5,8,2,10,4,1,13])
plt.plot(ypoints, c = 'hotpink')
plt.show()


#-----------------------------------------------------------


#Line Width

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([5,8,2,10,4,1,13])
plt.plot(ypoints, linewidth = '25.5')
plt.show()


#Multiple Lines

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
plt.plot(y1)
plt.plot(y2)

plt.show()


#The x- and y- values come in pairs:

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()





#-------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
#---------------------------#


#Line Chart with Annotations

import matplotlib.pyplot as plt

# Sample data
x = [6,7,8,9,10]
y = [6,5,4,3,2]

plt.figure(figsize=(8, 6))
plt.plot(x, y, marker='o', linestyle='-')

for i, (xi, yi) in enumerate(zip(x, y)):
	plt.annotate(f'({xi}, {yi})', (xi, yi), textcoords="offset points", xytext=(0, 10), ha='center')

plt.title('Line Chart with Annotations')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')

plt.grid(True)

plt.show()



#Multiple Line Charts Using Matplotlib


import matplotlib.pyplot as plt
import numpy as np
x = np.array([6,7,8,9])
y = x*2

plt.plot(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Any suitable title")
plt.show() 

plt.figure()
x1 = [2, 4, 6, 8]
y1 = [3, 5, 7, 9]
plt.plot(x1, y1, '-.')

plt.show()



#Multiple Plots on the Same Axis

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,9,10])
y = x*2

plt.plot(x, y)

x1 = [2,4,6,8,12]
y1 = [3,5,7,9,13]

plt.plot(x1, y1, '-.')

plt.xlabel("X-axis data")
plt.ylabel("Y-axis data")
plt.title('multiple plots')
plt.show()



#Fill the Area Between Two Lines


import matplotlib.pyplot as plt
import numpy as np


x = np.array([5,7,8,9,10])
y = x*2

plt.plot(x, y)

x1 = [2,4,6,8,12]
y1 = [3,5,7,9,13]

plt.plot(x, y1, '-.')
plt.xlabel("X-axis data")
plt.ylabel("Y-axis data")
plt.title('multiple plots')

plt.fill_between(x, y, y1, color='red', alpha=0.5)
plt.show()





#-------------------------------------------------------------------------

#Line plot styles in Matplotlib


import matplotlib.pyplot as plt
import random

students = ["Jane","Joe","Beck","Tom",
            "Sam","Eva","Samuel","Jack",
            "Dana","Ester","Carla","Steve",
            "Fallon","Liam","Culhane","Candance",
            "Ana","Mari","Steffi","Adam"]

marks = [random.randint(0, 101) for _ in students]

plt.figure(figsize=(10, 6)) 
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("CLASS RECORDS")
plt.xticks(rotation=45)  
plt.plot(students, marks, 'm--')
plt.tight_layout()  
plt.show()



#Example 2: Adding Markers to Line Plots


import matplotlib.pyplot as plt
import random

students = ["Jane","Joe","Beck","Tom","Sam",
            "Eva","Samuel","Jack","Dana","Ester",
            "Carla","Steve","Fallon","Liam","Culhane",
            "Candance","Ana","Mari","Steffi","Adam"]

marks = [random.randint(0, 101) for _ in students]

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("CLASS RECORDS")
plt.plot(students, marks, color='green', linestyle='solid', marker='o', markerfacecolor='red', markersize=12)
plt.xticks(rotation=45)  
plt.tight_layout()
plt.show()



#Example 3: Adding Grid Lines in Line Plots

import matplotlib.pyplot as plt
import random as random

students = ["Jane", "Joe", "Beck", "Tom",
			"Sam", "Eva", "Samuel", "Jack",
			"Dana", "Ester", "Carla", "Steve",
			"Fallon", "Liam", "Culhane", "Candance",
			"Ana", "Mari", "Steffi", "Adam"]

marks = []
for i in range(0, len(students)):
	marks.append(random.randint(0, 101))

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("CLASS RECORDS")
plt.plot(students, marks, 'm--')

plt.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.show()





#---------------------------------------------------------------------------------



#Plot Multiple lines in Matplotlib

import matplotlib.pyplot as plt 

x = [50,60,70,80,90] 
y = [40,40,40,40,40] 
plt.plot(x, y) 
plt.show()
#Plotting a single Vertical Line


x = [50,60,70,80,90] 
y = [40,40,40,40,40] 
plt.plot(y,x) 
plt.show()
#Plotting a Horizontal and a Vertical Line 


x = [10,20,30,40,50] 
y = [30,30,30,30,30] 
plt.plot(x, y, label = "line 1") 
plt.plot(y, x, label = "line 2") 
plt.legend() 
plt.show()
#Plotting Multiple Lines

# importing package 
import matplotlib.pyplot as plt 
import numpy as np 

# create data 
x = [1,2,3,4,5] 
y = [3,3,3,3,3] 

plt.plot(x, y, label = "line 1") 
plt.plot(y, x, label = "line 2") 
plt.plot(x, np.sin(x), label = "curve 1") 
plt.plot(x, np.cos(x), label = "curve 2") 
plt.legend() 
plt.show()


#-----------------------------------------------------------------------


#Change the line opacity in Matplotlib

import matplotlib.pyplot as plt 

x = [1, 2, 3, 4, 5] 
y = x 
plt.plot(x, y, linewidth=10, alpha=0.2) 
plt.show() 

#Example 2: (Lines with different opacities)


import matplotlib.pyplot as plt 
import numpy as np 


x = np.array([-2, -1, 0, ]) 
y1 = x*0
y2 = x*x 
y3 = -x*x 
plt.plot(x, y2, alpha=0.2) 
plt.plot(x, y1, alpha=0.5) 
plt.plot(x, y3, alpha=1) 
plt.legend(["op = 0.2", "op = 0.5", "op = 1"]) 
plt.show() 


#Example 3: (Multiple line plots with multiple opacity)

import matplotlib.pyplot as plt 
import numpy as np 


x = [1, 2, 3, 4, 5] 

for i in range(10): 
	plt.plot([1, 2.8], [i]*2, linewidth=5, color='red', alpha=0.1*i) 
	plt.plot([3.1, 4.8], [i]*2, linewidth=5, color='green', alpha=0.1*i) 
	plt.plot([5.1, 6.8], [i]*2, linewidth=5, color='yellow', alpha=0.1*i) 
	plt.plot([7.1, 8.8], [i]*2, linewidth=5, color='blue', alpha=0.1*i) 
for i in range(10): 
	plt.plot([1, 2.8], [-i]*2, linewidth=5, color='red', alpha=0.1*i) 
	plt.plot([3.1, 4.8], [-i]*2, linewidth=5, color='green', alpha=0.1*i) 
	plt.plot([5.1, 6.8], [-i]*2, linewidth=5, color='yellow', alpha=0.1*i) 
	plt.plot([7.1, 8.8], [-i]*2, linewidth=5, color='blue', alpha=0.1*i) 
plt.show() 




#------------------------------------------------------------------------------------



#Increase the thickness of a line with Matplotlib

import matplotlib.pyplot as plt

places = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
literacy_rate = [100, 98, 90, 85, 75, 50, 30, 45, 65, 70]
female_literacy = [95, 100, 50, 60, 85, 80, 75, 99, 70, 30]

plt.xlabel("Places")
plt.ylabel("Percentage")

plt.plot(places, literacy_rate, color='blue', linewidth=6, label="Literacy rate")
plt.plot(places, female_literacy, color='fuchsia', linewidth=4, label="Female Literacy rate")

plt.legend(loc='lower left', ncol=1)
plt.show()




#Example 2:

import matplotlib.pyplot as plt

age = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
cardiac_cases = [5, 15, 20, 40, 55, 55, 70, 80, 90, 95]
survival_chances = [99, 99, 90, 90, 80, 75, 60, 50, 30, 25]

plt.xlabel("Age")
plt.ylabel("Percentage")

plt.plot(age, cardiac_cases, color='red', linewidth=2,
         label="Cardiac Cases", marker='o', markerfacecolor='red', markersize=12)

plt.plot(age, survival_chances, color='yellow', linewidth=3,
         label="Survival Chances", marker='o', markerfacecolor='green', markersize=12)

plt.legend(loc='lower right', ncol=1)
plt.show()




#-------------------------------------------------------------------------------------





#How to Fill Between Multiple Lines in Matplotlib?


import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 2, 0.01)
y1 = np.sin(2 * np.pi * x)
y2 = 0.8 * np.sin(4 * np.pi * x)

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(6, 6))

ax1.fill_between(x, y1)
ax1.set_title('Fill between y1 and 0')

ax2.fill_between(x, y1, 1)
ax2.set_title('Fill between y1 and 1')

ax3.fill_between(x, y1, y2)
ax3.set_title('Fill between y1 and y2')
ax3.set_xlabel('x')

fig.tight_layout()
plt.show()




# Example 2: Color between the curve of the mathematical function f(x)=cos(x) and f(x)=exp(x) :-

import pylab as plt
import numpy as np

X = np.linspace(0, 3, 200)
Y1 = X**2 + 3
Y2 = np.sin(X)
Y3 = np.cos(X)

plt.plot(X, Y1, lw=4)
plt.plot(X, Y2, lw=4)
plt.plot(X, Y3, lw=4)

plt.fill_between(X, Y1, Y2, color='k', alpha=.5)
plt.fill_between(X, Y1, Y3, color='y', alpha=.5)

plt.show()




#Example 3: Color the Rhombus :-

import matplotlib.pyplot as plt


x = [1, 2, 1, 0]
y = [2, 1, 0, 1]

plt.fill(x, y)
plt.show()








