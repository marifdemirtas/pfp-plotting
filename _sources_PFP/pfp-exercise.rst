..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

..  shortname:: Exercises
..  description:: Seaborn Exercises

.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: ex1-
   


Exercises
###########################################
.. highlightedtextbox::
   :title:
   :color: #f4e36e
   :highlight-color: #ff9b3e
   :highlight-on-load:
   
   These exercises provide some practice for the concepts we have covered so far. If you need to go back to the previous examples and look up a definition, use the arrow at the bottom left to go back, or click <a href="/index.html">HERE</a> to go back to the table of contents.


.. parsonsprob:: parsons_box
   
      
   .. image:: _static/weather-box.png
      :scale: 90%
      :align: center
      :alt: A plot example
   Look at the provided plot. What code could produce that? Drag and drop the lines of code from below in the correct order to achieve that plot. You will not use all of the blocks.
   
   -----
   import seaborn as sns
   =====
   weather = load_dataset("weather")
   =====
   figure = sns.boxplot(x="year", y="temperature_avg", data=weather)
   =====
   figure = sns.barplot(x="year", y="temperature_avg", data=weather)#distractor
   =====
   figure = sns.FacetGrid(x="month", y="temperature_avg", data=weather)#distractor
   =====
   figure = weather.map(sns.boxplot, x="year", y="temperature_avg")#distractor
   =====
   figure = sns.boxplot(x="month", y="temperature_avg", data=weather)#distractor
   =====
   figure = sns.barplot(x="temperature_avg", y="month", data=weather)#distractor
   =====
   figure = sns.FacetGrid(x="temperature_avg", y="year", data=weather)#distractor
   =====
   figure = weather.map(sns.barplot, x="year", y="temperature_avg")#distractor
   =====
   display(figure)
   

.. mchoice:: box_plot_scenarios
   :answer_a: sns.boxplot(data=libraries, x="month", y="attendance")
   :feedback_a: This would show which months have more variance across libraries, but not which libraries have more variance across months.
   :answer_b: sns.boxplot(data=libraries, x="library", y="attendance")
   :feedback_b: Correct!
   :answer_c: sns.barplot(data=libraries, x="library", y="attendance")
   :feedback_c: No, a box plot would be more appropriate for this.
   :answer_d: sns.barplot(data=libraries, x="month", y="attendance")
   :feedback_d: No, a box plot would be more appropriate for this.
   :correct: b

   You are given a dataset that shows the average number of people who studied at each library on campus for each month in 2025. You want to see what libraries experience major changes in occupancy throughout the year. What line of code would be the most useful for visualizing this?






.. highlightedtextbox::
   :title:
   :color: #f4e36e
   :highlight-color: #ff883e
   :highlight-on-load:
   
   If you are done with the exercises, click on the arrow on the bottom right to move to the last page of this tutorial!