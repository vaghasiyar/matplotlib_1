##Matplotlib Bars

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x,y)
plt.show()


#Horizontal Bars

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.barh(x, y)
plt.show()


#--------------------------------------------------------------------------------------



#Bar Color

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x, y, color = "red")
plt.show()





#Color Names

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x, y, color = "hotpink")
plt.show()



#Color Hex

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x, y, color = "#4CAF50")
plt.show()



#Bar Width


x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x, y, width = 0.1)
plt.show()


#Bar Height

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.barh(x, y, height = 0.1)
plt.show()



#-----------------------------------------------------------------------------------------------


#Create a stacked bar plot in Matplotlib


#Example 1: (Simple stacked bar plot)

import matplotlib.pyplot as plt

x = ['A', 'B', 'C', 'D']
y1 = [10, 20, 10, 30]
y2 = [20, 25, 15, 25]
plt.bar(x, y1, color='r')
plt.bar(x, y2, bottom=y1, color='b')
plt.show()



#Example 2: (Stacked bar chart with more than 2 data)


x = ['A', 'B', 'C', 'D']
y1 = np.array([10, 20, 10, 30])
y2 = np.array([20, 25, 15, 25])
y3 = np.array([12, 15, 19, 6])
y4 = np.array([10, 29, 13, 19])
plt.bar(x, y1, color='r')
plt.bar(x, y2, bottom=y1, color='b')
plt.bar(x, y3, bottom=y1+y2, color='y')
plt.bar(x, y4, bottom=y1+y2+y3, color='g')
plt.xlabel("Teams")
plt.ylabel("Score")
plt.legend(["Round 1", "Round 2", "Round 3", "Round 4"])
plt.title("Scores by Teams in 4 Rounds")
plt.show()




#Example 3: (Stacked Bar chart using dataframe plot)

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.DataFrame([['A', 10, 20, 10, 26], ['B', 20, 25, 15, 21], ['C', 12, 15, 19, 6],
				['D', 10, 18, 11, 19]],
				columns=['Team', 'Round 1', 'Round 2', 'Round 3', 'Round 4'])
print(df)
df.plot(x='Team', kind='bar', stacked=True,
		title='Stacked Bar Graph by dataframe')
plt.show()






#-------------------------------------------------------------------------------------------------------+




#Plotting back-to-back bar charts Matplotlib


import numpy as np
import matplotlib.pyplot as plt

A = np.array([3,6,9,4,2,5])
X = np.arange(6)

plt.bar(X, A, color = 'r')
plt.bar(X, -A, color = 'b')
plt.title("Back-to-Back Bar Chart")
plt.show()




#Example 2: Horizontal Back-to-Back Bar Chart. 


# import packages
import numpy as np
import matplotlib.pyplot as plt

A = np.array([3,6,9,4,2,5])
B = np.array([2,8,1,9,7,3])
X = np.arange(6)

plt.barh(X, A, color = 'r')
plt.barh(X, -B, color = 'b')
plt.title("Back-to-Back Bar Chart")
plt.show()



#Example 3: Complete Back-to-Back Bar Chart with Some styles in matplotlib. 



# import packages
import numpy as np
import matplotlib.pyplot as plt

A = np.array([3,6,9,4,2,5])
B = np.array([2,8,1,9,7,3])
X = np.arange(6)

plt.barh(X, A, align='center',
		alpha=0.9, color = 'y')

plt.barh(X, -B, align='center', 
		alpha=0.6, color = 'c')

plt.grid()
plt.title("Back-to-Back Bar Chart")
plt.ylabel("Indexes")
plt.xlabel("Values")
plt.show()



#---------------------------------------------------------------------------



#How to display the value of each bar in a bar chart using Matplotlib?


#Example 1: Using matplotlib.axes.Axes.text() function:


import os
import numpy as np
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5, 6, 7]
y = [160, 167, 17, 130, 120, 40, 105, 70]
fig, ax = plt.subplots()
width = 0.75
ind = np.arange(len(y))
ax.barh(ind, y, width, color = "green")
for i, v in enumerate(y):
	ax.text(v + 3, i + .25, str(v), 
			color = 'blue', fontweight = 'bold')
plt.show()


#Example 2: Use matplotlib.pyplot.text() function:

import matplotlib.pyplot as plt
x = ["A", "B", "C", "D"]
y = [1, 2, 3, 4]
plt.barh(x, y)
for index, value in enumerate(y):
	plt.text(value, index,
			str(value))
plt.show()



#