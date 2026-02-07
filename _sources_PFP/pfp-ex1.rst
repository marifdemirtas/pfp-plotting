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
   

Example 1: Finding the most reliable restaurants in Champaign area
###########################################################################################################

At the University of Illinois Urbana-Champaign, a group of students completed a survey asking 50 students to rate 10 restaurants around the campus. After creating their restaurant_ratings dataset, the group wants to analyze the rating distribution of the restaurants in order to determine which restaurants are the most consistent in terms of student opinion.

The *restaurants* dataset looks like this:


+------------+--------------------------+--------+
| student_id | Name                     | Rating |
+============+==========================+========+
| 0          | Maize Mexican Grill      | 4      |
+------------+--------------------------+--------+
| 5          | Maize Mexican Grill      | 2      |
+------------+--------------------------+--------+
| 32         | Papa Del's Pizza Factory | 4      |
+------------+--------------------------+--------+
| 49         | Sakanaya                 | 5      |
+------------+--------------------------+--------+
| 27         | The Bread Company        | 3      |
+------------+--------------------------+--------+


The goal is to use the student ratings of each restaurant to create 10 box plots in a single figure.

.. activecode:: pfp-restaurant-ex
   :language: python3

   from tutorial.main import display, load_dataset

   # Plan 1: Import Packages and Load Data
   import seaborn as sns
   import matplotlib.pyplot as plt

   restaurants = load_dataset('restaurants')

   # Plan 3: Create a Box Plot
   figure = sns.boxplot(x="restaurant_name", y="rating", palette="magma", data=restaurants, hue='price_level')

   # Plan 6: Customize Figure
   plt.title("Ratings Distribution by Restaurant")
   plt.xlabel("Restaurant Name")
   plt.ylabel("Rating (1-5)")
   # Rotate x-axis labels for readability
   plt.xticks(rotation=45, ha='right')
   # Set y-axis range limits and labels
   plt.ylim(0.5, 5.5)
   plt.yticks([1, 2, 3, 4, 5])
   # Make sure all annotations are visible within the figure area
   plt.tight_layout()
   
   # Plan 7: Display Figure
   display(figure)


.. stdoutimage::
  :source_id: pfp-restaurant-ex
  :title: Output Image
  :mime: image/png


This code probably seems a bit complicated. In this ebook, we will break down each example into a few common "plans". This example is made up of five plans. Click on each of them to learn more.


.. toctree::
   :maxdepth: 1

   pfp-plan1-intro
   pfp-plan3-box
   pfp-plan6-customize
   pfp-plan7-display

.. plandisplay::
   :plan: Import Packages and Load Data

.. plandisplay::
   :plan: Create a Box Plot

.. plandisplay::
   :plan: Customize Figure

.. plandisplay::
   :plan: Display Figure
