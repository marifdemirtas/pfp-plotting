..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

..  shortname:: Example 2
..  description:: Second example for showcasing Seaborn

.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: ex1-
   

Example 2: Comparing rainfall and temperatures in Champaign in the last ten years
###########################################################################################################

.. highlightedtextbox::
   :title:
   :color: #f4e36e
   :highlight-color: #ffe53e
   :highlight-on-load:
   
   Here's another example visualization problem that is about the weather data collected in Champaign. Read through the explanation below and run the code by clicking on 'Save and Run' to see how you can create a visualization for this problem!

In the city of Champaign, the regional planning commission manages a weather dataset containing records of the total precipitation and the average temperature in the city from 2015 to 2024. The city wants to analyze the trends in the dataset to make sure they can accurately forecast future infrastructure needs and agricultural impacts for the local community.

In the weather dataset, we have two types of measurement for each month: rainfall_total and temperatuve_avg.

+------+----------+--------------------------+--------------------------+
| year | month    | rainfall_total           | temperature_avg          |
+======+==========+==========================+==========================+
| 2015 | January  | 1.69                     | 25.4                     |
+------+----------+--------------------------+--------------------------+
| 2015 | February | 1.6                      | 20                       |
+------+----------+--------------------------+--------------------------+
| 2015 | March    | 3.72                     | 54.6                     |
+------+----------+--------------------------+--------------------------+
| 2015 | April    | 3.72                     | 54.6                     |
+------+----------+--------------------------+--------------------------+
| 2015 | May      | 6.07                     | 66.1                     |
+------+----------+--------------------------+--------------------------+

The goal is to create two side-by-side bar plots using the average value of total rainfall and average temperature for each month. For this exercise, we will use a modified version of this dataset to be in *long-form*. That version of the dataset will look like this:

+------+----------+--------------------------+--------+
| Year | Month    | measurement_type         | value  |
+======+==========+==========================+========+
| 2015 | January  |  rainfall_total          | 1.69   |
+------+----------+--------------------------+--------+
| 2015 | January  | temperature_avg          | 25.4   |
+------+----------+--------------------------+--------+
| 2015 | February |  rainfall_total          | 1.6    |
+------+----------+--------------------------+--------+
| 2015 | February | temperature_avg          | 20     |
+------+----------+--------------------------+--------+
| 2015 | March    | rainfall_total           | 3.72   |
+------+----------+--------------------------+--------+
| 2015 | March    | temperature_avg          | 54.6   |
+------+----------+--------------------------+--------+
| 2015 | April    |  rainfall_total          | 3.72   |
+------+----------+--------------------------+--------+
| 2015 | April    | temperature_avg          | 54.6   |
+------+----------+--------------------------+--------+
| 2015 | May      |  rainfall_total          | 6.07   |
+------+----------+--------------------------+--------+
| 2015 | May      | temperature_avg          | 66.1   |
+------+----------+--------------------------+--------+

This dataset is in *long form*, which means that different measurements for the same month (e.g. total rainfall and average temperature for January 2015) are represented in separate rows of the table, as opposed to the *wide form*, where different measurements for the same month were in different columns in the same row. Seaborn uses long form data for most operations, and this is why we provide the long form version of the weather dataset.


.. activecode:: pfp-weather-ex
   :language: python3

   from tutorial.main import display, load_dataset
   
   # Plan 1: Import Packages and Load Data
   import seaborn as sns

   dataset = load_dataset("weather_long")
   
   # Plan 4: Create Grid of Multiple Plots
   grid = sns.FacetGrid(dataset, col='measurement_type', sharey=False)
   grid.map(sns.barplot, 'month', 'value', palette='magma', errorbar=None)

   # Plan 6: Customize Figure
   grid.set_xlabels("Month")
   grid.set_ylabels("Average Value")
   grid.set_xticklabels(rotation=45)

   # Plan 7: Display Figure
   display(grid)

.. stdoutimage::
  :source_id: pfp-weather-ex
  :title: Output Image
  :mime: image/png


Again, this example might look complicated at first. However, we can break it into four plans, and we have already learned about three of them. Let's explore the new plan, which shows how to create a grid of plots.

.. toctree::
   :maxdepth: 1

   pfp-plan1-intro
   pfp-plan4-gridinit
   pfp-plan6-customize
   pfp-plan7-display

.. plandisplay::
   :plan: Import Packages and Load Data

.. plandisplay::
   :plan: Create Grid of Multiple Plots

.. plandisplay::
   :plan: Customize Figure

.. plandisplay::
   :plan: Display Figure
