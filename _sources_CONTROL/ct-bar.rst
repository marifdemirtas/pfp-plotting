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

.. highlightedtextbox::
   :title:
   :color: #f4e36e
   :highlight-color: #ffe53e
   :highlight-on-load:
   
   Run the code below to see an example of a barplot using the 'weather' dataset.



.. activecode:: ct_bar_weather_1
   :language: python3

   from tutorial.main import load_dataset, display
   import seaborn as sns
   
   weather = load_dataset("weather")

   figure = sns.barplot(x="month", y="temperature_avg", data=weather)
   figure.tick_params(axis='x', labelrotation=45)

   # Display figure below
   display(figure)


Display the generated plot below:

.. stdoutimage::
  :source_id: ct_bar_weather_1
  :title: Average Temperature Bar Plot
  :mime: image/png


Let's customize this plot by including the 'year' column from the dataset to see the differences in average temperature across years for each month.


.. activecode:: ct_bar_weather_2
   :language: python3

   from tutorial.main import load_dataset, display
   import seaborn as sns
   import matplotlib.pyplot as plt

   weather = load_dataset("weather")

   # customize the bar plot
   figure = sns.barplot(x="month", y="temperature_avg", hue="year", palette="muted", data=weather)
   figure.tick_params(axis='x', labelrotation=45)

   # add labels and title
   plt.xlabel("Month")
   plt.ylabel("Average temperature")
   plt.title("Average temperature by month and year in Champaign")

   # Save the plot and show in tutorial environment
   display(figure)



Display the modified plot below:

.. stdoutimage::
  :source_id: ct_bar_weather_2
  :title: Average Temperature for Each Year
  :mime: image/png


.. highlightedtextbox::
   :title:
   :color: #f4e36e
   :highlight-color: #ffe53e
   :highlight-on-load:
   
   Click on the arrow on the bottom right to move to the next page.