..  shortname:: gridplot

..  description:: Create a bar plot


.. setup for automatic question numbering.

.. qnum::
   :start: 1

Plan 5: Create a Bar Plot
========================

.. plandisplay:: plans.json
   :plan: Create A Bar Plot

Bar plots are used to visualize the relationship between a categorical variable and a continuous variable. In a bar plot, each bar represents the mean or median (or any aggregation) of the continuous variable for each category. In Seaborn, bar plots can be created using the sns.barplot() function, which has a similar structure to sns.boxplot().

Plan 5 - When to use this plan?
--------------------------------
Use this plan when you want to compare the summarized values of a numerical variable across different categories. Bar plots highlight the **summary values** (e.g. means) of categories, whereas box plots highlight the **distribution** of categories.

Plan 5 - What parts can be customized to use this plan?
-------------------------------------------------------
Replace the *x* and *y* values with the columns that you want to compare from the dataset, replace *hue* with with another column from the dataset if you would like to split your plot into categories (or remove *hue* if you do not have any other columns to split), and change *palette* to other preset seaborn color schemes. 


Plan 5 - Exercises
--------------------

.. mchoice:: bar_plot_scenarios
   :answer_a: Finding out the movies that were seen by the most people
   :feedback_a: Correct! Bar plots can show use the total number.
   :answer_b: Finding out the movies that were the most divisive in terms of audience ratings
   :feedback_b: No, a box plot would be more appropriate for this since we need to see the distribution of audience ratings.
   :answer_c: Comparing the relation between the rating of a movie and the number of people who have seen it
   :feedback_c: No, other plot types (such as a scatterplot) would be more appropriate for this.
   :correct: a

   Assume that you can obtain a large dataset from a movie theater chain. What of the following problems would be best addressed with a bar plot?



.. highlightedtextbox::
   :title:
   :color: #f4e36e
   :highlight-color: #ffe53e
   :highlight-on-load:

   If you completed all the activities on this page, click on the arrow on the bottom right to continue.