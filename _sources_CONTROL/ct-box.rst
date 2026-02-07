..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

..  shortname:: Box
..  description:: Box Plots

.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: ex1-
   

Seaborn Box Plots
###########################################

Box plots are a type of visualization that shows the distribution of a dataset. They are commonly used to compare the distribution of one or more variables across different categories.


.. activecode:: ct_box_restaurant_1
   :language: python3

   from tutorial.main import load_dataset, display
   import seaborn as sns

   restaurants = load_dataset("restaurants")

   figure = sns.boxplot(x="restaurant_name", y="rating", data=restaurants)

   # Save the plot and show in tutorial environment
   display(figure)


Display the figure below:

.. stdoutimage::
  :source_id: ct_box_restaurant_1
  :title: Restaurant Box Plot
  :mime: image/png


Customize the box plot by grouping restaurants by price level.

.. activecode:: ct_box_2
   :language: python3

   from tutorial.main import load_dataset, display
   import seaborn as sns

   # load the tips dataset from Seaborn
   restaurants = load_dataset("restaurants")

   # create a box plot of ratings by restaurant and price level, using the "hue" parameter to differentiate between cheaper and expensive restaurants
   # customize the color scheme using the "palette" parameter
   figure = sns.boxplot(x="restaurant_name", y="rating", hue="price_level", data=restaurants, palette="Set3")

   # add labels and title
   plt.xlabel("Restaurant")
   plt.ylabel("Ratings")

   # display the plot
   display(figure)


Display the output of the modified plot below:

.. stdoutimage::
  :source_id: ct_box_2
  :title: Improved Restaurant Box Plot
  :mime: image/png

