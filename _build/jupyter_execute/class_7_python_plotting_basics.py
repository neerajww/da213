#!/usr/bin/env python
# coding: utf-8

# # Plotting with python
# 
# First, let's install matplotlib python package into your machine. For this, go to the linux terminal and make use of pip as follows.
# ```
# pip install matplotlib
# ```
# Next, do one of the following.
# * open Visual Studio Code and create a new Jupyter notebook inside it
# * open Visual Studio Code and create a new python script inside it
# * open any other IDE of your choice and do one of the above.
# 
# Next, follow along with the code snippets below.
# 
# ## Plotting a simple line graph

# In[1]:


import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 1)
cubes = x**3

fig, ax = plt.subplots()
ax.plot(x, cubes)
plt.show()


# 

# Take 2 mins and read the above code line by line. You might notice the following.
# * We import the `pyplot` module from the `matplotlib` package. The pyplot module contains a variety of functions for plotting. Note that we assign it an short alias `plt`. Think - why? Importing functions from the module directly will led to importing with their original name. This can result in conflict and confusion, and is a bad practice. Assigning an alias helps avoid this. 
# * We import `numpy` and use an alias `np` for it. We creat two variable and assigned them numpy arrays.
# * We call the `subplots()` method contained in `plt`. The `subplots()` method returns a tuple with two objects. This tuple is unpacked and the two objects are assigned to the variables `fig` and `ax`, respetively.
# * After the above assignment, `fig` denotes a (rectangular) figure frame. By passing additional arguments to `subplots()` we can set the size (in inches) of this frame. But remember it denotes only the frame. We cannot draw on the frame. We need a canvas inside it. This canvas is contained in variable `ax`.
# * `ax` denotes the canvas inside the frame. We draw on this canvas. It can only belong to one figure. Note, `ax` is short for axes and denotes an axes object.
# * Next, we used the `plot()` method to make a line plot for `x` versus `cubes`.
# * Subsequently, `show()` method opens matplotlib's viewer and displays the plot.  
# 
# Now again read the above code and make sure you understand each line. Let's see how we can:
# * alter the framesize
# * overlay plotting

# In[2]:


fig, ax = plt.subplots(nrows=1, ncols=1, figsize=[4,6]) #[len, width] of the frame in inches

ax.plot(x, cubes)
plt.show()


# 

# Let's improvise somethings in the above plot. What you think is missing?
# 1. Labels on the x-axis and y-axis
# 2. Data points on the curve.
# 3. Can we:
#     1. thinken the curve and choose a different color
#     2. add grid lines
#     3. increase the font size of the xticks and yticks
#     4. turn off the top and right spine
#     5. add a textbox stating something about the curve
# 
# Let's see how we do all the above. Please read the below code line be line.

# In[3]:


fig, ax = plt.subplots(nrows=1, ncols=1, figsize=[4,6]) #[len, width] of the frame in inches

FS = 14 # fontsize
LW = 2 # linewidth
MS = 10 # markersize

ax.plot(x, cubes, linestyle='-', linewidth=LW, color='blue', marker='o', markersize=MS, markeredgecolor='blue', markerfacecolor='gray')
ax.grid(color='gray', linestyle='--', linewidth=.3,alpha=.5)
ax.set_xlabel('x', fontsize=FS)
ax.set_ylabel('y=$x^3$', fontsize=FS)
ax.tick_params(which='both', labelsize=FS) # increase fontsize of xtick and ytick
ax.spines['right'].set_color('none') # turn off right spine
ax.spines['top'].set_color('none') # turn top left spine
ax.text(3, 600, 'Increasing trend', fontsize=FS, color='gray')
plt.show()


# Which of the two plots above is easy to understand? Let's plot them side by side. But how do we plot side by side? We can place two canvas in one figure frame. The `subplots()` methods takes arguments for this. Let's see how.

# In[4]:


fig, ax = plt.subplots(nrows=1, ncols=2, figsize=[14,8]) #[len, width] of the frame in inches

# ax is now an axis array with two objects inside, one for each canvas.
# We use the first one below
ax[0].plot(x, cubes)

# Next we use the second one below
FS = 14 # fontsize
LW = 2 # linewidth
MS = 10 # markersize
ax[1].plot(x, cubes, linestyle='-', linewidth=LW, color='blue', marker='o', markersize=MS, markeredgecolor='blue', markerfacecolor='gray')
ax[1].grid(color='gray', linestyle='--', linewidth=.3,alpha=.5)
ax[1].set_xlabel('x', fontsize=FS)
ax[1].set_ylabel('y=$x^3$', fontsize=FS)
ax[1].tick_params(which='both', labelsize=FS) # increase fontsize of xtick and ytick
ax[1].spines['right'].set_color('none') # turn off right spine
ax[1].spines['top'].set_color('none') # turn top left spine
ax[1].text(3, 600, 'Increasing trend', fontsize=FS, color='gray')
plt.show()


# ## Exercise A
# The COVID-19 pandemic is gradually fading. We will do some data visualization to help us understand the COVID-19 case count across the globe. For this we will use the data made available by the World Health Organization through the CSV file `WHO-COVID-19-global-data.csv`.
# 
# 1. Create a new python notebook and name it as your_roll_number_class_7_assign_1.ipynb. You will submit this.
# 2. Load the WHO-COVID-19-global-data.csv
# 3. Make a line plot illustrating the global COVID-19 "new case count" as a function of "days since 2020-01-03 (YYYY-MM-DD)"
# 4. On to the same plot overlay the COVID-19 "new case count" for India, US, and Brasil. Add a legend for each trace.
# 5. Write three or more (bulletted) observations you make from your plot.
# 5. (Bonus question) Alongside the trend of increase and decrease in "new case count" on the scale of months, do you notice a fast variation within a week? Can you confirm this fast variation using some mathematical analysis tool? Hint: Use the Fourier transform utility (`np.fft.rfft()`), plot the magnitude Fourier spectrum, and estimate the periodicity from the peak depicted in the spectrum.

# ## Making a scatter plot
# 
# In a line plot there is a relationship between consecutive data points. The data points form a sequence. For example, it can be a temporal sequence (like, the COVID-19 count as a function of time) or something else. Often we have scenarios in which there is no relationship between consecutive data points. Consider, you have a database of dogs documenting the `height` and `weight` of each dog. How will you establish if there exists a relationship between these two variables?
# * To begin, you can make a scatter plot between `height` and `weight`
# * How? Using the `scatter()` instead of `plot()`

# In[5]:


import matplotlib.pyplot as plt
import numpy as np

# first we sample some random number between 0 to 10. Note, there is no temporal relation between adjacent samples
x = np.random.uniform(low=0, high=10, size=100)
# cube each number
cubes = x**3
# square each number
squares = x**2

fig, ax = plt.subplots()
ax.scatter(squares, cubes)
plt.show()


# Observations from the plot
#  - the variables plotted on the x-axis and y-axis are correlated
#  
# Can we improve the presentation to make this more evident? Yes! Please read the code line by line and note the changes.

# In[6]:


fig, ax = plt.subplots(nrows=1, ncols=2, figsize=[14,8]) #[len, width] of the frame in inches

# ax is now an axis array with two objects inside, one for each canvas.
# We use the first one below
ax[0].scatter(squares, cubes)

# Next we use the second one below
FS = 14 # fontsize
LW = 2 # linewidth
MS = 100 # markersize

ax[1].scatter(squares, cubes, c=cubes, cmap=plt.cm.Blues, s=MS, edgecolors='black')
ax[1].grid(color='white', linestyle='--', linewidth=.3,alpha=.5)
ax[1].set_xlabel('$x^2$', fontsize=FS)
ax[1].set_ylabel('$x^3$', fontsize=FS)
ax[1].tick_params(which='both', labelsize=FS) # increase fontsize of xtick and ytick
ax[1].spines['right'].set_color('none') # turn off right spine
ax[1].spines['top'].set_color('none') # turn top left spine
ax[1].set_facecolor((0.5, 0.5, 0.5)) # changing the color of the canvas
plt.show()


# ## Exercise B
# 
# * Use the data in `WHO-COVID-19-global-data.csv` and create a scatter plot of daily COVID-19 new case count between India and Brasil. List your observations.
# * Draw a scatter plot between global `New_cases` and `Cummulative_deaths`.
#     * Now make three scatter plots within a figure frame (that, is (three columns, one row)). These will correspond to data from 2020, 2021, and 2022 only, respectively.
#     * List your obervations
# 

# ## Making a bar plot
# 
# Often you wish to present a quick summary about different conditions. For example, what is the mean (or average) for data derived from experiment A and data derived from experiment B. The bar plot utility comes handy in such scenarios.
# * Can we do a bar plot in python? Yes! We use `bar()` instead of `scatter()` and `plot()`.
# * Read the below code line by line 
# 

# In[7]:


import matplotlib.pyplot as plt
import numpy as np

# seeding a random number generator helps reproducibility. Without it, you will get a different draw of samples for each function call.
np.random.seed(1001)

# samples to be drawn from the experiment
nsamples = 10000
# Exaeriment A: we sample some data points from a uniform distribution
y_A = np.random.uniform(low=-1, high=1, size=nsamples)
# Exaeriment B: we sample some data points from a gaussian distribution
y_B = np.random.randn(nsamples)

data_y = [np.mean(y_A), np.mean(y_B)]
data_x = [1,2]
fig, ax = plt.subplots()
ax.bar(data_x, data_y)
plt.show()


# Can we improve the presentation?
# * Can we add text labels on the x-axis, below each bar
# * Can we add an errorbar on top of each bar. This errorbar will denote the standard deviation
# 
# Read the below code line by line to understand how it can be done - easily!

# In[8]:


fig, ax = plt.subplots(nrows=1, ncols=2, figsize=[16,8]) #[len, width] of the frame in inches

# ax is now an axis array with two objects inside, one for each canvas.
# We use the first one below
ax[0].bar(data_x, data_y)


# Next we use the second one below
FS = 14 # fontsize
LW = 2 # linewidth
MS = 100 # markersize
BW = .5 # barwidth
# compute the normalized standard deviation for data from each experiment
data_std = [.001, .005] # choice of these values if only for illustartion

ax[1].bar(data_x, data_y, yerr=data_std, width=BW, color='tab:red', edgecolor='gray', alpha=1, linewidth=LW, hatch='//')
ax[1].set_xticks(data_x)
ax[1].set_xticklabels(['A', 'B'], rotation=0, fontsize=FS)
ax[1].set_xlabel('Experiment', fontsize=FS)
ax[1].set_ylabel('Average', fontsize=FS)

ax[1].grid(color='white', linestyle='--', linewidth=.3,alpha=.5)
ax[1].tick_params(which='both', labelsize=FS) # increase fontsize of xtick and ytick
ax[1].spines['right'].set_color('none') # turn off right spine
ax[1].spines['top'].set_color('none') # turn top left spine
ax[1].set_ylim([0,.02])
ax[1].set_facecolor((0.5, 0.5, 0.5)) # changing the color of the canvas
plt.show()


# ## Exercise C
# 
# * Use the data in `WHO-COVID-19-global-data.csv`
# * Create dataframe containing three colums: country code (or name), cummulative covid case count, cummulative covid death count. Using this data frame:
#     * Make a scatter plot of cummulative covid case count, cummulative covid death count. List your observations.
#     * Make a bar plot illustrating the cummulative case count for top five countries. List your observations.
# 
# 

# ## Making histograms
# Histograms help to plot the distribution of data. Like other things, it easy to plot these in python.

# In[9]:


fig, ax = plt.subplots(nrows=1, ncols=1, figsize=[16,8]) #[len, width] of the frame in inches

FS = 14 # fontsize
LW = 2 # linewidth
MS = 100 # markersize
BW = .5 # barwidth
# compute the normalized standard deviation for data from each experiment

ax.hist(y_A, bins=100, label='Experiment A')
ax.hist(y_B, bins=100, label='Experiment B', alpha=.5)
ax.set_xlabel('Samples values', fontsize=FS)
ax.set_ylabel('Count', fontsize=FS)
ax.legend(frameon=False, loc='upper right', fontsize=FS)
ax.grid(color='black', linestyle='--', linewidth=.3,alpha=.5)
ax.tick_params(which='both', labelsize=FS) # increase fontsize of xtick and ytick
ax.spines['right'].set_color('none') # turn off right spine
ax.spines['top'].set_color('none') # turn top left spine
plt.show()


# ## Exercise D
# Make a histogram of cummulative COVID-19 case using the new data frame you made. List your observations. Does it look Gaussian? Yes or no and explain why so?
# 
# Let's move to the next section now.

# ## (Bonus) Exercise E
# 
# You can also overlay datapoints onto a world map - easily. Use the below code and fill the missing piece to illustrate this.

# In[10]:


from geopy.geocoders import Nominatim
from mpl_toolkits.basemap import Basemap

geolocator = Nominatim(user_agent="geoapiExercises")

# function resturn lat and long for a country
def geolocate(country):
    try:
        # Geolocate the center of the country
        loc = geolocator.geocode(country)
        # And return latitude and longitude
        return (loc.latitude, loc.longitude)
    except:
        # Return missing value
        return np.nan

# create a dictionary with four columns: country name lat, long, and cummulative covid case count

#########################################
# plot world map distribution
#########################################
fig = plt.subplots(figsize=[9,7])
m = Basemap(llcrnrlon=-180, llcrnrlat=-65, urcrnrlon=180, urcrnrlat=80)
m.drawmapboundary(fill_color='#FFF', linewidth=0)
m.fillcontinents(color='grey', alpha=0.5)
m.drawcoastlines(linewidth=0.1, color="white")

# prepare a color for each point depending on the continent.
# df['labels_enc'] = pd.factorize(df['country'])[0]
 
# Add a point per position
# m.scatter(
#     x=df['long'], 
#     y=df['lat'], 
#     s=np.log2(df['count'])*100, 
#     alpha=0.7, 
#     c=df['labels_enc']/100, 
#     cmap="Set1"
# )
plt.show()

