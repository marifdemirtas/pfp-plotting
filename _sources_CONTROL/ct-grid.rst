..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

..  shortname:: Bar
..  description:: Bar Plots

.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: ex1-
   

Seaborn facet grids
###########################################

FacetGrid is a powerful seaborn tool that allows you to visualize the distribution of one variable as well as the relationship between two variables, across levels of additional categorical variables. 

FacetGrid creates a grid of subplots based on the unique values in the categorical variable specified.



.. activecode:: ct_grid_1
   :language: python3

   from tutorial.main import load_dataset

   # Load the Restaurants dataset
   restaurants = load_dataset("restaurants")


   # create a FacetGrid for day vs total_bill
   g = sns.FacetGrid(tips, col="day")

   # plot histogram for total_bill in each day
   g.map(sns.histplot, "total_bill")


Output:

.. stdoutimage::
  :source_id: ct_grid_1
  :title: Output Image
  :mime: image/png



.. activecode:: ct_grid_2
   :language: python3
   
   import seaborn as sns
   import matplotlib.pyplot as plt

   # load the tips dataset from Seaborn
   tips = sns.load_dataset("tips")

   # create a box plot of total bill by day and meal time, using the "hue" parameter to differentiate between lunch and dinner
   # customize the color scheme using the "palette" parameter
   # adjust the linewidth and fliersize parameters to make the plot more visually appealing
   sns.boxplot(x="day", y="total_bill", hue="time", data=tips, palette="Set3", linewidth=1.5, fliersize=4)

   # add a title, xlabel, and ylabel to the plot using Matplotlib functions
   plt.title("Box Plot of Total Bill by Day and Meal Time")
   plt.xlabel("Day of the Week")
   plt.ylabel("Total Bill ($)")

   # display the plot
   plt.show()




Output:

.. stdoutimage::
  :source_id: ct_grid_1
  :title: Output Image
  :mime: image/png