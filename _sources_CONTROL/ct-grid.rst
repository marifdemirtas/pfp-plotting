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

FacetGrid is a powerful Seaborn tool that allows you to visualize the distribution of one variable as well as the relationship between two variables, across levels of additional categorical variables. 

FacetGrid creates a grid of subplots based on the unique values in the categorical variable specified.

.. highlightedtextbox::
   :title:
   :color: #f4e36e
   :highlight-color: #ffe53e
   :highlight-on-load:
   
   Run the code below to see an example of how you can use FacetGrid to create two plots in a single figure to show two quantitites side by side.


.. activecode:: ct_grid_1
   :language: python3

   from tutorial.main import load_dataset, display
   import seaborn as sns

   # Load the weather dataset in long form
   weather = load_dataset("weather_long")

   # Create a FacetGrid with a plot for each 'measurement_type'
   grid = sns.FacetGrid(weather, col="measurement_type", sharey=False)

   # Plot barplot for each measurement
   grid.map(sns.barplot, "month", "value", palette='magma', errorbar=None)
   grid.set_xticklabels(rotation=45)

   display(grid)


Look at the plot below:

.. stdoutimage::
  :source_id: ct_grid_1
  :title: Combined Plot
  :mime: image/png


.. highlightedtextbox::
   :title:
   :color: #f4e36e
   :highlight-color: #ffe53e
   :highlight-on-load:
   
   Click on the arrow on the bottom right to move to the next page.