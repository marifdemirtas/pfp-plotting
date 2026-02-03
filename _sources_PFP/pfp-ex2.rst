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

The goal is to create two side-by-side bar plots using the average value of total precipitation and average temperature for each month. For this exercise, we will use a modified version of this dataset to be in long-form. That version of the dataset will look like this:

+------+----------+--------------------------+--------+
| Year | Month    | measurement_name         | value  |
+======+==========+==========================+========+
| 2015 | January  | Total Precipitation (in) | 1.69   |
+------+----------+--------------------------+--------+
| 2015 | January  | Average Temperature (°F) | 25.4   |
+------+----------+--------------------------+--------+
| 2015 | February | Total Precipitation (in) | 1.6    |
+------+----------+--------------------------+--------+
| 2015 | February | Average Temperature (°F) | 20     |
+------+----------+--------------------------+--------+
| 2015 | March    | Total Precipitation (in) | 3.72   |
+------+----------+--------------------------+--------+
| 2015 | March    | Average Temperature (°F) | 54.6   |
+------+----------+--------------------------+--------+
| 2015 | April    | Total Precipitation (in) | 3.72   |
+------+----------+--------------------------+--------+
| 2015 | April    | Average Temperature (°F) | 54.6   |
+------+----------+--------------------------+--------+
| 2015 | May      | Total Precipitation (in) | 6.07   |
+------+----------+--------------------------+--------+
| 2015 | May      | Average Temperature (°F) | 66.1   |
+------+----------+--------------------------+--------+

This dataset is in *long form*, which means that different measurements for the same month (e.g. total precipitation and average temperature for January 2015) are separate rows of the table, as opposed to the *wide form*, where different measurements for the same month were in different columns of the same row. Seaborn uses long form data for most operations, and this is why we provide the long form version of the weather dataset.


.. activecode:: pfp-weather-ex
   :language: python3

   from tutorial.main import display, load_dataset
   
   # Plan 1: Set Up Packages and Data
   import seaborn as sns
   import matplotlib.pyplot as plt
   import pandas as pd

   weather = load_dataset("weather_long")
   
   # Plan 4: Initialize FacetGrid
   figure = sns.FacetGrid(df_long, col='Measurement', sharey=False, height=5, aspect=1.5)


   # Plan 5: Map categorical plot on grid
   figure.map(sns.barplot, 'Month', 'Value', palette='magma', errorbar=None)


   # Plan 6: Set labels/titles
   g.figure.suptitle('Weather Trends of Monthly Precipitation and Temperature (2015-2024)', fontsize=16)
   g.set_axis_labels("Month", "Average Value")
   # Create titles for individual subplots
   g.set_titles(col_template="{col_name}")
   # Rotate x-axis labels for readability
   g.set_xticklabels(rotation=45)
   # Make sure all annotations are visible within the figure area
   plt.tight_layout()

   # Plan 7: Display Figure
   display(figure)

.. stdoutimage::
  :source_id: pfp-weather-ex
  :title: Output Image
  :mime: image/png


This code probably seems a bit complicated. In this ebook, we will break down each example into a few common "plans". This example is made up of five plans. Click on each of them to learn more.


.. toctree::
   :maxdepth: 1

   pfp-plan1-intro
   pfp-plan4-gridinit
   pfp-plan5-gridplot
   pfp-plan6-customize
   pfp-plan7-display

.. plandisplay::
   :plan: Update Records Conditionally

.. plandisplay::
   :plan: Update Records Conditionally

.. plandisplay::
   :plan: Update Records Conditionally

.. plandisplay::
   :plan: Update Records Conditionally
