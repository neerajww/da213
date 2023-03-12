#!/usr/bin/env python
# coding: utf-8

# # Data Visualization
# 
# Good things first.
# The Python community is extremely generous. People of this community every now and then create useful classes and functions, and document them as code modules. This documentation is also very neat as python codes are written not only for machines but also for humans. Sometimes a community (group of like minded individuals) create and pool multiple modules and form a package. The best thing is that many of these packages are released as open-access, enabling anyone to use it for free.
# 
# Some such popular packages are numpy, pandas, and scipy. A list is maintained [here](https://pypi.org/). You can install these packages into your local python directory using the pip command from your linux/windows terminal. Many python packages are also popular in the scientific community. Example, check [this one](https://www.nature.com/articles/s41586-020-2649-2) for numpy and [this one](https://www.nature.com/articles/s41592-019-0686-2) for scipy. We think, it is a good idea to aim for creating one or more packages and present them as return gift to the python community.
# Okay, now we bring focus to today’s class.
# 
# Today’s class we will learn about using a python package named matplotlib. As the name suggests, the package helps to make plots in python. Quoting from its [description](https://matplotlib.org/) - “Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. Matplotlib makes easy things easy and hard things possible”.
# 
# ### What is data visualization?
# Data visualization refers to drawing graphic displays to show data. This includes plotting a sequence of data points to visualize a trend (example, a line plot), plotting one sequence of data points against another (example, a scatter plot), plotting statistical summaries of the data points (example, a bar plot, a  histogram). The data can be ``raw data’’ or data obtained from applying some data science techniques on the raw data. As with many things in life, it becomes easier to create and appreciate graphics once we are aware of some basic concepts and terminologies.
# 
# ### What purpose does it serve in Data Science?
# Data cleaning, detecting outliers and unusual groups, identifying trends, clusters and patterns, evaluating and interpreting results are some things facilitated by data visualization. Often, the importance of data visualization is underplayed in textbooks, yet is very important in practical investigations.
# 
# ### Is it an old subject?
# Yes, we do know some amazing artists from the past who have created beautiful visualizations (and structures - pyramids). Plotting would have served a useful purpose a long long time back as well. But something interesting is happening in current times.
# 
# ### What's new now?
# Thanks to the increasing access to useful data and design of higher-level computer programming languages, it is becoming easier to draw and redraw graphics. What used to be a slow and wearisome process - for instance imagine making a plot using C programming, has now become fast and flexible. Further, enhanced printing and visualization technology, and social media has also increased the consumption of created data visualizations. You may like to take a quick glance over two interesting visualizations: [State of running in the world](https://runrepeat.com/state-of-running) and [Population density in the world](https://pudding.cool/2018/10/city_3d/). An inspiring article on importance of data visualization is available [here](https://hdsr.mitpress.mit.edu/pub/zok97i7p/release/4).
# 
# ### What we will learn today?
# By the end of today's exercise you will have answers for the following. 
# * What are the different kind of plots
# * What are the different features in a given plot
# * What kind of plot can provide what kind of information
# * How to choose colors and sizes which help interpret and draw attention
# * How to do all the above python
# 
# So, let’s begin.
# 

# 
