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

   import seaborn as sns
   from tutorial.main import load_dataset, display

   restaurants = load_dataset("restaurants")

   figure = sns.boxplot(x="restaurant_name", y="rating", data=restaurants)

   # Save the plot and show in tutorial environment
   display(figure)



Output:

.. stdoutimage::
  :source_id: ct_box_restaurant_1
  :title: Output Image
  :mime: image/png


Customize the box plot by TODO [orig:including `time` column from the dataset.]


.. activecode:: ct_box_2
   :language: python3

   from tutorial.main import load_dataset, display
   import seaborn as sns

   # load the tips dataset from Seaborn
   restaurants = load_dataset("restaurants")

   # create a box plot of total bill by day and meal time, using the "hue" parameter to differentiate between lunch and dinner
   # customize the color scheme using the "palette" parameter
   # adjust the linewidth and fliersize parameters to make the plot more visually appealing
      # , palette="Set3", linewidth=1.5, fliersize=4
   figure = sns.boxplot(x="restaurant_name", y="rating", hue="student_id", data=restaurants)

   # add a title, xlabel, and ylabel to the plot using Matplotlib function
   #plt.title("Box Plot of Rating by Student and Restaurant")
   #plt.xlabel("Restaurants")
   #plt.ylabel("Rating")

   # display the plot
   display(figure)





Output:

.. stdoutimage::
  :source_id: ct_box_2
  :title: Output Image
  :mime: image/png

