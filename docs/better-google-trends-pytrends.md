<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

# Better Google Trends graphs using Python and seaborn
[TOC]

## Overview
In this article we will be looking at generation good-looking graphs with Google Trends.
We are tackling this topic as the visualizations on Google Trends can often times lack visual appeal.
We will obtain the data using pytrends - an unofficial Google Trends api. To visualize the data we will use seaborn - a matplotlib based library.

## Pre-requisites
Prior experience with Python and data visualizations will be beneficial, but ultimately, you will be just fine without it.

Let's get started.

## Setup
So, let's begin by installing the the modules we need. Type the following into your terminal:

`pip install pytrends` or `python -m pip install pytrends`

`pip install seaborn` or `python -m pip install seaborn`

Since seaborn is built on top of matplotlib, it will install the other required dependies for us (`numpy`, `scipy`, `pandas` and `matplotlib`). We won't get into using all of those, but it is good to be aware of them.

Now, create your python file - name it anything you want besides 'seaborn.py' or 'pytrends.py'. 
Essentially, you do not want your file name to be the same name as any of the modules you are importing because Python sees your local file first, thinks it is the module and then tries to import that. This leads to attribute and circular import errors which we always want to avoid as best as we can.

At the top of your python file, import the modules with the following:
```
import seaborn
import matplotlib.pyplot as plt
import pytrends
from pytrends.request import TrendReq
```

Before we start coding away, let's create a plan of action to help us keep perspective while we are creating this script. Add this basic outline as multi-line comments:
```
'''
1. Connect to Google Trends using pytrends.
'''

'''
2. Get the data we require.
'''

'''
3. Process the data for plotting.
'''

'''
4. Plotting the data.
'''
```
We will be writing our code underneath each relevant section. 
Let's begin.

## Connecting to Google Trends
Fortunately, our first step is quickly achieved using the following code - Go ahead and type it in underneath the first section:
```
pytrends = TrendReq()
```
- This simply establishes the connection to Google Trends. We use will use this to query Google and retrieve our data.

On to the next one, excelsior! 

## Getting the data
Now, underneath our second section. Let's imagine pytrends as a rocket, and our data as the payload the rocket will be delivering to us.
Fortunately, pytrends plays well with this metaphor as it uses `pytrends.build_payload(keywords)` to fetch and deliver our data from Google.

Before we can build our payload, we will need to supply pytrends with the keywords of the data we want.
Since we can supply just one or multiple keywords, let's create a function to dynamically get these keywords from us. Write the following code:
```
kw_list = []

while True:
    kw = input("Keyword:        (Enter '0' to proceed) \n> ")
    
    if kw == str(0):
        break
    else: 
        kw_list.append(kw) 
```
- Using a while-loop with a condition of True will automatically activate the loop when Python gets to that line. 
- This way, Python will continue asking us for and storing the keywords until we enter the number 0 to stop the loop.

Now with our keyword list ready, we can then build the payload and query the specific data we need. In this example we will query the interest over time data. Let's do just that using:
```
pytrends.build_payload(kw_list, geo='', timeframe='2016-01-01 2020-12-31')

keyword_interest = pytrends.interest_over_time()
```
- When building our payload, we specify that we don't want region-specific data within our 5 year time frame beginning in 2016.
- `interest_over_time()` is one of the methods that pytrends uses to get us specific data - The interest and search activity of our keywords in this case.

With that done, let's move on ahead to the next section.

## Processing the data
In this step we will clean up our data and make sure it is ready to be plotted.
Once again, we won't have much to do in this step. Pytrends has conveniently returned the data in a 
pandas dataframe (table) - This just makes it relatively easy to manipulate and plot. However, we won't be getting into that on this tutorial. Type in the following:  
```
print(keyword_interest.head())
del keyword_interest['isPartial']
```
- To confirm what we're working with, we print the top part of our table - Using `.head()`, which is one of the many pandas methods. 
- We then delete the extra 'isPartial' column from our table as we won't need to plot it. 

Go ahead and run the code to confirm. You can then add another `print(time_interest.head())` statement to confirm that the extra column is gone.

Now, we're ready for the last step. Let's move on.

## Plotting the data
With our data ready, let's go ahead and use seaborn to visualize it.
Write the following code in your remaining section.
```
seaborn.set_theme(style="darkgrid")
ax = seaborn.lineplot(data=keyword_interest)

legend = ax.legend()

for i in range(len(kw_list)):
    ax.lines[i].set_linestyle("-")
    legend.get_lines()[i].set_linestyle("-")

plt.show()
```
- Seaborn visualizations are appealing by default. However, here we set a different theme as it might suit the style of our current data more - This of course is personal preference and so, any or no theme at all is okay.    
- Passing in our data as a parameter we use `seaborn.lineplot()` to plot the data in a way that suits our needs - We then save this plot into an `ax` variable.
- From our `ax` variable we can access the legend and the line styles. We then use a loop (based on the number of keywords in our `kw_list`) to change every line style -from a dotted line to a straight line- on the plot and legend.
- Finally, we use `plt.show()` to see our plot. 

At this point you can run the code and a graph should appear on your screen.
We have accomplished all the objectives set out by our plan of action.

## Extra
Say you got tired of pressing the Enter key after every keyword and you wanted to enter all of them in one line. How would you go about doing that?
What if you wanted to separate the list using a comma? Or a 'vs.'? or either?
Try that out on your own and see if you can achieve it. 


## Conclusion
In this tutorial we learned how to create custom appealing visualizations using a library built on matplotlib and an unofficial Google Trends api in Python. We have also learned how to automate our input process. I hope you enjoyed it and have come up with a solution for the extra section.