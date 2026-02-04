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

   from tutorial.main import load_dataset, display
   import seaborn as sns

   # Load the Weather dataset in long form
   weather = load_dataset("weather_long")

   # create a FacetGrid for measurement type vs measurement value
   grid = sns.FacetGrid(weather, col="measurement_type", sharey=False, height=5, aspect=1.5)

   # plot barplot for each measurement
   grid.map(sns.barplot, "month", "value", palette='magma', errorbar=None)

   # OPTIONAL / TODO
   # Plan 6: Set labels/titles
   # g.figure.suptitle('Weather Trends of Monthly Precipitation and Temperature (2015-2024)', fontsize=16)
   # g.set_axis_labels("Month", "Average Value")
   # Create titles for individual subplots
   # g.set_titles(col_template="{col_name}")
   # Rotate x-axis labels for readability
   # g.set_xticklabels(rotation=45)
   # Make sure all annotations are visible within the figure area
   # plt.tight_layout()

   # Plan 7: Visualize
   display(grid)


Output:

.. stdoutimage::
  :source_id: ct_grid_1
  :title: Output Image
  :mime: image/png


TODO removed an example from here. Is that alright?