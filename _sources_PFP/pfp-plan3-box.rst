..  shortname:: box

..  description:: Create a box plot


.. setup for automatic question numbering.

.. qnum::
   :start: 1

Plan 3: Create a Box Plot
========================

.. plandisplay:: plans.json
   :plan: Create a Box Plot

A box plot is a great way to visualize the distribution, median, quartiles, and outliers in your dataset. The box plots are commonly used to compare the distribution of one or more variables across different categories. In our example, we used box plots to visualize the distribution of ratings for each restaurant. 

By adding the hue information, we can show how restaurants in different categories might have different distributions. By changing the color palette, we can make our plot more readable.

Plan 3 - When to use this plan?
--------------------------------
Use this plan when you want to compare the distribution of a numerical variable across different categories.

Plan 3 - What parts can be customized to use this plan?
-------------------------------------------------------
Replace the *x* and *y* values with the columns that you want to compare from the dataset, replace *hue* with with another column from the dataset if you would like to split your plot into categories (or remove *hue* if you do not have any other columns to split), and change *palette* to other preset seaborn color schemes. 



Plan 3 - Exercises
--------------------

.. fillintheblank:: fitb_box
   :code_template:
      import seaborn as sns
      dataset = load_dataset('sales_data')
      figure = sns.@@blank1@@(x = "@@blank2@@", y = "@@blank3@@", data=dataset)
      display(figure)
   :correct: ["boxplot", "store", "sales"]
   :feedback: ["The first box is incorrect. What type of plot could we use to plot distributions? Check the earlier example if you need a hint!", "The second box is incorrect. x-axis is our horizontal axis, and we want to have different categories we want to compare here. For instance, we are comparing different 'stores' in this problem.", "The third box is incorrect. y-axis is our vertical axis, and we want to have variable that we are interested in the distribution of. For instance, we are interested in the distribution of 'sales' in this problem."]
   :placeholder: ["", "", ""]

   Fill in the blanks in the following code piece to plot the distribution of "sales" for each different "store".


.. highlightedtextbox::
   :title:
   :color: #f4e36e
   :highlight-color: #ffe53e
   :highlight-on-load:

   If you have completed the activities on this page, click on the arrow on the bottom right to move to the next page.