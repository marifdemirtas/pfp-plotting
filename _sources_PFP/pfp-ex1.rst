..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

..  shortname:: Example 1
..  description:: First example for showcasing Seaborn

.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: ex1-
   

Example 1: Comparing rainfall and temperatures in Champaign in the last ten years
###########################################################################################################

In the city of Champaign, the regional planning commission manages a weather dataset containing records of the total precipitation and the average temperature in the city from 2015 to 2024. The city wants to analyze the trends in the dataset to make sure they can accurately forecast future infrastructure needs and agricultural impacts for the local community.

The weather dataset may include columns such as:

+------+----------+--------------------------+---------------------------+
| Year | Month | Total Precipitation (in) | Average Temperature (°F) |
+======+==========+==========================+===========================+ 
|2015 | January | 1.69 | 25.4 | 
+------+----------+--------------------------+---------------------------+ 
| 2015 | February | 1.6 | 20 | 
+------+----------+--------------------------+---------------------------+ 
| 2015 | March | 3.72 | 54.6 | 
+------+----------+--------------------------+---------------------------+ 
| 2015 | April | 3.72 | 54.6 | 
+------+----------+--------------------------+---------------------------+ 
| 2015 | May | 6.07 | 66.1 | 
+------+----------+--------------------------+---------------------------+

The goal is to create two side-by-side bar plots using the average value of total precipitation and average temperature for each month.

.. activecode:: pfp-weather-ex
   :language: python3

   import seaborn as sns
   import matplotlib.pyplot as plt
   import pandas as pd
   from figshow.main import show_figure

   load dataset

# Plan 4: Initialize FacetGrid
g = sns.FacetGrid(df_long, col='Measurement', sharey=False, height=5, aspect=1.5)


# Plan 5: Map categorical plot on grid
g.map(sns.barplot, 'Month', 'Value', palette='magma', errorbar=None)


# Plan 6: Set labels/titles
g.figure.suptitle('Weather Trends of Monthly Precipitation and Temperature (2015-2024)', fontsize=16)
g.set_axis_labels("Month", "Average Value")
# Create titles for individual subplots
g.set_titles(col_template="{col_name}")
# Rotate x-axis labels for readability
g.set_xticklabels(rotation=45)
# Make sure all annotations are visible within the figure area
plt.tight_layout()


# Plan 7: Visualize
plt.show()

   # Save the plot
   filename = "seaborn_plot1.png"
   plt.savefig(filename)

   # Show figure in this environment
   show_figure(filename)

.. stdoutimage::
  :source_id: pfp-weather-ex
  :title: Output Image
  :mime: image/png


This code probably seems a bit complicated. In this ebook, we will break down each example into a few common "plans". This example is made up of five plans. Click on each of them to learn more.


.. toctree::
   :maxdepth: 1

   plan1
   plan3
   plan5

.. raw:: html

   <pre><strong>Plan 1: Get a soup from a URL</strong>
   <a href="/ns/books/published/cs102web/plan1.html"><pre style="background-color:#FCF3CF;">
   # Load libraries for web scraping
   from bs4 import BeautifulSoup
   import requests
   # Get a soup from a URL 
   url = 'https://web.archive.org/web/20250309231002/https://bbqchicken.com/locations/'
   r = requests.get(url)
   soup = BeautifulSoup(r.content, 'html.parser')</pre></a></pre>
   
   <pre><strong>Plan 3: Get info from all tags of a certain type</strong><a href="/ns/books/published/cs102web/plan3.html"><pre style="background-color:#D5F5E3;">
   # Get all tags of a certain type from the soup
   tags = soup.find_all('h4')
   # Collect info from the tags
   collect_info = []
   for tag in tags:
       # Get info from tag
       info = tag.text
       collect_info.append(info)</pre></a></pre>

   <pre><strong>Plan 5: Print the info</strong><a href="/ns/books/published/cs102web/plan5.html"><pre style="background-color:#D6EAF8;">
   # Print the info
   print(collect_info)</pre></a></pre>

