..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

..  shortname:: Customization
..  description:: Seaborn Customization

.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: ex1-
   

Customizing Seaborn plots
###########################################

Seaborn is a powerful data visualization library that provides numerous ways to customize the appearance of plots. Customizing Seaborn plots is an essential part of creating meaningful and visually appealing visualizations. 

Here are some examples of customizing seaborn plots:

Changing Color Palettes
########################

Here is an example of how you can change the color palettes of your seaborn plots:


.. activecode:: ct_palette
   :language: python3

   from tutorial.main import load_dataset, display
   import seaborn as sns

   # load the tips dataset from Seaborn
   restaurants = load_dataset("restaurants")

   # create a box plot of ratings by restaurant and price level, using the "hue" parameter to differentiate between cheaper and expensive restaurants
   # customize the color scheme using the "palette" parameter
   figure = sns.boxplot(x="restaurant_name", y="rating", hue="cost", data=restaurants, palette="magma")
   figure.tick_params(axis='x', labelrotation=90)

   # display the plot
   display(figure)



Display the output of the modified color palette below:

.. stdoutimage::
  :source_id: ct_palette
  :title: Modified Color Palette
  :mime: image/png



Label your axes and use clear titles
################################################
Labels and titles are essential for effective data visualization. Make sure to label your axes clearly and provide a descriptive title for your visualization. This will help your audience understand the message you are trying to convey.

Here's how you can add a title, a label for the X-axis, and a label for the Y-axis using *matplotlib* with *seaborn*:



.. activecode:: ct_title
   :language: python3

   from tutorial.main import load_dataset, display
   import seaborn as sns

   # load the tips dataset from Seaborn
   restaurants = load_dataset("restaurants")

   # create the boxplot from above
   figure = sns.boxplot(x="restaurant_name", y="rating", hue="cost", data=restaurants, palette="magma")
   figure.tick_params(axis='x', labelrotation=90)

   # add labels and title
   figure.set_title("Restaurant ratings in Champaign, organized by cost")
   figure.set_xlabel("Restaurant")
   figure.set_ylabel("Ratings (1-5)")

   # display the plot
   display(figure)



Display the figure with new labels:

.. stdoutimage::
  :source_id: ct_palette
  :title: Figure with the Updated Title
  :mime: image/png

