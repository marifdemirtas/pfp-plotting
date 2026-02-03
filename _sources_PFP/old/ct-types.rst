..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

..  shortname:: Types
..  description:: Seaborn Plot Types

.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: ex1-
   

Seaborn Plot Types
###########################################

Seaborn provides a wide range of plot types that can be used for data visualization and exploratory data analysis. Broadly speaking, any visualization can fall into one of the three categories. 

* Univariate: x only (contains only one axis of information)
* Bivariate: x and y (contains two axis of information)
* Trivariate: x, y, z (contains three axis of information)

.. image:: _static/ct-plot-types-fig1.png
    :scale: 25%
    :align: center
    :alt: Three types of plots

Here are some of the most commonly used plot types in Seaborn that we will cover today:

* Bar Plot. A bar plot is used to visualize the relationship between a categorical variable and a continuous variable. Seaborn's barplot() function provides a simple way to create scatter plots.
* Scatter Plot. A scatter plot is used to visualize the relationship between two variables. Seaborn's scatterplot() function provides a simple way to create scatter plots.
* Line Plot. A line plot is used to visualize the trend of a variable over time. Seaborn's lineplot() function provides a simple way to create line plots.
* Box Plot. A box plot is used to visualize the distribution of a variable. Seaborn's boxplot() function provides a simple way to create box plots.

Today, we will focus on examples and detailed explanations of bar and box plots.

