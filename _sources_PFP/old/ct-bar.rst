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
   

Seaborn Bar Plots
###########################################

Bar plots are used to visualize the relationship between a categorical variable and a continuous variable. In a bar plot, each bar represents the mean or median (or any aggregation) of the continuous variable for each category. In Seaborn, bar plots can be created using the barplot() function. 


In this tutorial, we created two example datasets we will use that are saved in the same Pandas DataFrame format. The first one shows ratings of 10 restaurants around the campus by 50 students.
Here's how to load and preview this example dataset:

.. activecode:: ct_data_loading_restaurant
   :language: python3

   from tutorial.main import load_dataset

   # Load the Restaurants dataset
   restaurants = load_dataset("restaurants")

   # check the head
   print(restaurants.head()) 
   import seaborn as sns

titanic = sns.load_dataset("titanic")

sns.barplot(x="class", y="fare", data=titanic)


Output:

Let’s customize this plot by including `sex` column from the dataset.



.. activecode:: ct_data_loading_weather
   :language: python3

   import seaborn as sns

import matplotlib.pyplot as plt




titanic = sns.load_dataset("titanic")




# customize the bar plot

sns.barplot(x="class", y="fare", hue="sex", ci=None, palette="muted", data=titanic)




# add labels and title

plt.xlabel("Class")

plt.ylabel("Fare")

plt.title("Average Fare by Class and Gender on the Titanic")




# display the plot

plt.show()

Output: