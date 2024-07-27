##Matplotlib Histograms


import numpy as np

x = np.random.normal(170, 10, 250)
print(x)



import matplotlib.pyplot as plt
import numpy as np
x = np.random.normal(170, 10, 250)
plt.hist(x)
plt.show() 



#--------------------------------------------------------------


#Plotting Histogram in Python using Matplotlib


import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)
plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Basic Histogram')
plt.show()



#Customized Histogram with Watermark



import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

np.random.seed(23685752)
N_points = 10000
n_bins = 20

x = np.random.randn(N_points)
y = .8 ** x + np.random.randn(10000) + 25
legend = ['distribution']

fig, axs = plt.subplots(1, 1, figsize=(10, 7), tight_layout=True)

for s in ['top', 'bottom', 'left', 'right']: 
    axs.spines[s].set_visible(False) 

axs.xaxis.set_ticks_position('none') 
axs.yaxis.set_ticks_position('none') 

axs.xaxis.set_tick_params(pad=5) 
axs.yaxis.set_tick_params(pad=10) 

axs.grid(visible=True, color='grey', linestyle='-.', linewidth=0.5, alpha=0.6) 

fig.text(0.9, 0.15, 'Jeeteshgavande30', fontsize=12, color='red',
         ha='right', va='bottom', alpha=0.7) 

N, bins, patches = axs.hist(x, bins=n_bins)
fracs = ((N**(1 / 5)) / N.max())
norm = colors.Normalize(fracs.min(), fracs.max())

for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)

plt.xlabel("X-axis")
plt.ylabel("y-axis")
plt.legend(legend)
plt.title('Customized histogram')
plt.show()






#Multiple Histograms with Subplots


import matplotlib.pyplot as plt
import numpy as np

data1 = np.random.randn(1000)
data2 = np.random.normal(loc=3, scale=1, size=1000)
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 4))
axes[0].hist(data1, bins=30, color='Yellow', edgecolor='black')
axes[0].set_title('Histogram 1')
axes[1].hist(data2, bins=30, color='Pink', edgecolor='black')
axes[1].set_title('Histogram 2')
for ax in axes:
	ax.set_xlabel('Values')
	ax.set_ylabel('Frequency')
plt.tight_layout()

plt.show()




#Stacked Histogram using Matplotlib

import matplotlib.pyplot as plt
import numpy as np

data1 = np.random.randn(1000)
data2 = np.random.normal(loc=3, scale=1, size=1000)
plt.hist([data1, data2], bins=30, stacked=True, color=['cyan', 'Purple'], edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Stacked Histogram')
plt.legend(['Dataset 1', 'Dataset 2'])
plt.show()


#Plot 2D Histogram (Hexbin Plot) using Matplotlib

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(1000)
y = 2 * x + np.random.normal(size=1000)
plt.hexbin(x, y, gridsize=30, cmap='Blues')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('2D Histogram (Hexbin Plot)')
plt.colorbar()
plt.show()





#------------------------------------------------------------------------------------------


#Create a cumulative histogram in Matplotlib


import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

x = [10, 40, 20, 10, 30, 10, 56, 45]

res = stats.cumfreq(x, numbins=4,
					defaultreallimits=(1.5, 5))
rng = np.random.RandomState(seed=12345)

samples = stats.norm.rvs(size=1000,
						random_state=rng)
res = stats.cumfreq(samples,
					numbins=25)
x = res.lowerlimit + np.linspace(0, res.binsize*res.cumcount.size,
								res.cumcount.size)
fig = plt.figure(figsize=(10, 4))

ax1 = fig.add_subplot(1, 2, 1)

ax2 = fig.add_subplot(1, 2, 2)

ax1.hist(samples, bins=25,
		color="green")
ax1.set_title('Histogram')
ax2.bar(x, res.cumcount, width=4, color="blue")
ax2.set_title('Cumulative histogram')
ax2.set_xlim([x.min(), x.max()])
plt.show()




#Example 2:

import numpy as np
from scipy import stats

x = [10, 40, 20, 10, 30, 10, 56, 45]

res = stats.cumfreq(x, numbins=4,
					defaultreallimits=(1.5, 5))

rng = np.random.RandomState(seed=12345)

samples = stats.norm.rvs(size=1000,
						random_state=rng)

res = stats.cumfreq(samples,
					numbins=25)

x = res.lowerlimit + np.linspace(0, res.binsize*res.cumcount.size,
							res.cumcount.size)

fig = plt.figure(figsize=(10, 4))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
ax1.hist(samples, bins=25, color="green")
ax1.set_title('Histogram')
ax2.bar(x, x, width=2, color="blue")
ax2.set_title('Cumulative histogram')
ax2.set_xlim([x.min(), x.max()])
plt.show()




#-----------------------------------------------------------------------------------------




#How to plot two histograms together in Matplotlib?


import matplotlib.pyplot as plt
import numpy as np


series1 = np.random.randn(500, 1)
series2 = np.random.randn(400, 1)
plt.hist(series1)
plt.hist(series2)
plt.show()


#Example 2:

# importing libraries
import matplotlib.pyplot as plt

age_g1 = [1, 3, 5, 10, 15, 17, 18, 16, 19,
		21, 23, 28, 30, 31, 33, 38, 32, 
		40, 45, 43, 49, 55, 53, 63, 66, 
		85, 80, 57, 75, 93, 95]

age_g2 = [6, 4, 15, 17, 19, 21, 28, 23, 31, 
		36, 39, 32, 50, 56, 59, 74, 79, 34, 
		98, 97, 95, 67, 69, 92, 45, 55, 77,
		76, 85]
plt.hist(age_g1, label='Age group1', bins=14, alpha=.7, edgecolor='red')

plt.hist(age_g2, label="Age group2", bins=14, alpha=.7, edgecolor='yellow')
plt.legend()
plt.show()



#Example 3


# importing libraries
import matplotlib.pyplot as plt

age_g1 = [1, 3, 5, 10, 15, 17, 18, 16, 19, 21,
		23, 28, 30, 31, 33, 38, 32, 40, 45, 
		43, 49, 55, 53, 63, 66, 85, 80, 57, 
		75, 93, 95]

age_g2 = [6, 4, 15, 17, 19, 21, 28, 23, 31, 36,
		39, 32, 50, 56, 59, 74, 79, 34, 98, 97,
		95, 67, 69, 92, 45, 55, 77, 76, 85]

plt.hist(age_g1, label='Age group1', alpha=.7, color='red')
plt.hist(age_g2, label="Age group2", alpha=.5,
		edgecolor='black', color='yellow')
plt.legend()

plt.show()




#-------------------------------------------------------------------------------



#Bin Size in Matplotlib Histogram

#Method 1 : 
#Example 1 :
import matplotlib.pyplot as plt 

height = [189, 185, 195, 149, 189, 147, 154, 
		174, 169, 195, 159, 192, 155, 191, 
		153, 157, 140, 144, 172, 157, 181, 
		182, 166, 167] 

plt.hist(height, edgecolor="red", bins=5) 
plt.show() 



#Example 2 :


import matplotlib.pyplot as plt 

values = [87, 53, 66, 61, 67, 68, 62, 
		110, 104, 61, 111, 123, 117, 
		119, 116, 104, 92, 111, 90, 
		103, 81, 80, 101, 51, 79, 107, 
		110, 129, 145, 139, 110] 

plt.hist(values, bins=7, edgecolor="yellow", color="green") 
plt.show() 


#Method 2 :

#Example 1 : Equal bin width


import matplotlib.pyplot as plt 

marks = [1, 2, 3, 2, 1, 2, 3, 2, 
		1, 4, 5, 4, 3, 2, 5, 4, 
		5, 4, 5, 3, 2, 1, 5] 

plt.hist(marks, bins=[1, 2, 3, 4, 5], edgecolor="black") 
plt.show() 



#Example 2 : Unequal bin width

import matplotlib.pyplot as plt 

data = [189, 185, 195, 149, 189, 147, 
		154, 174, 169, 195, 159, 192, 
		155, 191, 153, 157, 140, 144, 
		172, 157, 181, 182, 166, 167] 

plt.hist(data, bins=[140, 150, 160, 175, 185, 200], 
		edgecolor="yellow", color="grey") 

plt.show() 



#Method 3:


import matplotlib.pyplot as plt 

data = [87, 53, 66, 61, 67, 68, 62, 110, 
		104, 61, 111, 123, 117, 119, 116, 
		104, 92, 111, 90, 103, 81, 80, 101, 
		51, 79, 107, 110, 129, 145, 128, 
		132, 135, 131, 126, 139, 110] 
binwidth = 8
plt.hist(data, bins=range(min(data), max(data) + binwidth, binwidth), 
		edgecolor="yellow", color="brown") 
plt.show() 

