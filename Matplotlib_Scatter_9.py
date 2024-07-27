##Matplotlib Scatter


#Creating Scatter Plots

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)
plt.show()



#Compare Plots

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y)
plt.show() 



#-------------------------------------------------------------------------------



#Colors

#You can set your own color for each scatter plot with the color or the c argument:

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color = 'hotpink')
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color = '#88c999')
plt.show() 



#Color Each Dot

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
plt.scatter(x, y, c=colors)
plt.show() 



#How to Use the ColorMap

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
plt.scatter(x, y, c=colors, cmap='viridis')
plt.show() 




x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')
plt.colorbar()
plt.show() 



#-----------------------------------------------------------------------



#Size

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
plt.scatter(x, y, s=sizes)
plt.show() 





#Alpha

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
plt.scatter(x, y, s=sizes, alpha=0.5)
plt.show() 



#Combine Color Size and Alpha


import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')
plt.colorbar()
plt.show() 









#-----------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------#



##matplotlib.pyplot.scatter() in Python




import matplotlib.pyplot as plt

x =[5, 7, 8, 7, 2, 17, 2, 9,
	4, 11, 12, 9, 6] 
y =[99, 86, 87, 88, 100, 86, 
	103, 87, 94, 78, 77, 85, 86]
plt.scatter(x, y, c ="blue")
plt.show()




#Plot Multiple Datasets on a Scatterplot 

x1 = [89, 43, 36, 36, 95, 10, 
      66, 34, 38, 20]
 
y1 = [21, 46, 3, 35, 67, 95, 
      53, 72, 58, 10]
x2 = [26, 29, 48, 64, 6, 5,
      36, 66, 72, 40]
 
y2 = [26, 34, 90, 33, 38, 
      20, 56, 2, 47, 15]
 
plt.scatter(x1, y1, c ="pink", 
            linewidths = 2, 
            marker ="s", 
            edgecolor ="green", 
            s = 50)
 
plt.scatter(x2, y2, c ="yellow",
            linewidths = 2,
            marker ="^", 
            edgecolor ="red", 
            s = 200)
 
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()



#Bubble Plots in Matplotlib 

import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [2, 3, 5, 7, 11]
bubble_sizes = [30, 80, 150, 200, 300]
plt.scatter(x_values, y_values, s=bubble_sizes, alpha=0.6, edgecolors='b', linewidths=2)
plt.title("Bubble Chart with Transparency")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()




#Custom a Matplotlib Scatterplot


x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 100 * np.random.rand(50)
plt.scatter(x, y, c=colors, s=sizes, alpha=0.7, cmap='viridis')
plt.title("Customized Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.colorbar(label='Color Intensity')
plt.show()






#-----------------------------------------------------------------------------------------------







#How to add a legend to a scatter plot in Matplotlib ?


# import required modules
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y1 = [2,4,6,8,10]
y2 = [3,6,9,12,15]
plt.scatter(x, y1)
plt.scatter(x,y2)
plt.legend(["x*2" , "x*3"])
plt.show()


x =  [1,2,3,4,5]
y1 = [2,4,6,8,10]
y2 = [3,6,9,12,15]
plt.scatter(x, y1)
plt.scatter(x,y2)
plt.legend(["x*2" , "x*3"], ncol = 2 , loc = "lower right")
plt.show()


x = np.arange(1, 6)
y1 = x**2
y2 = x**4
plt.scatter(x, y1, label="x**2")
plt.scatter(x, y2, label="x**4")
plt.legend()
plt.show()



#-----------------------------------------------------------------------------------------------------


#How to Connect Scatterplot Points With Line in Matplotlib?


import numpy as np 
import matplotlib.pyplot as plt 
  
x = [0.1, 0.2, 0.3, 0.4, 0.5] 
y = [6.2, -8.4, 8.5, 9.2, -6.3] 
plt.title("Connected Scatterplot points with lines") 
plt.scatter(x, y) 
plt.plot(x, y) 


x = [1, 2, 3] 
y = [1, 2, 3] 
plt.title("Connected Scatterplot points with lines") 
plt.scatter(x, y) 
plt.plot(x, y) 


x = [0.1, 0.2, 0.3, 0.4, 0.5] 
y = [6.2, -8.4, 8.5, 9.2, -6.3] 
plt.title("Connected Scatterplot points with line") 
plt.plot(x, y, marker="*") 
plt.show() 








#-------------------------------------------------------------------------------------



#How to create a Scatter Plot with several colors in Matplotlib?

import matplotlib.pyplot as plt
 
x = [1, 2, 3, 4]
y = [4, 1, 3, 6]
plt.scatter(x, y, c='green')
x = [5, 6, 7, 8]
y = [1, 3, 5, 2]
plt.scatter(x, y, c='red')
plt.show()



#Example 1: Create a Scatter Plot with RGB Colors

# import required modules
import matplotlib.pyplot as plt
import numpy

a = numpy.array([[9, 1, 2, 7, 5, 8, 3, 4, 6],
				[4, 2, 3, 7, 9, 1, 6, 5, 8]])
categories = numpy.array([0, 1, 2, 0, 1, 2, 0, 1, 2])
colormap = numpy.array(['r', 'g', 'b'])
plt.scatter(a[0], a[1], s=100, c=colormap[categories])
plt.show()





#Example 2: Create a Scatter Plot Using Color Codes

# import required modules
import matplotlib.pyplot as plt
import numpy

a = numpy.array([[1, 2, 3, 4, 5, 6, 7, 8, 9],
				[9, 8, 7, 6, 5, 4, 3, 2, 1]])

categories = numpy.array([0, 1, 1, 0, 0, 1, 1, 0, 1])

color1 = (0.69411766529083252, 0.3490196168422699, 
		0.15686275064945221, 1.0)
color2 = (0.65098041296005249, 0.80784314870834351,
		0.89019608497619629, 1.0)

colormap = numpy.array([color1, color2])
plt.scatter(a[0], a[1], s=500, c=colormap[categories])
plt.show()







