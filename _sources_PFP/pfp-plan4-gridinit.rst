..  shortname:: gridinit

..  description:: Split Data into Grid for Multiple Plots


.. setup for automatic question numbering.

.. qnum::
   :start: 1

Plan 4: Create Grid of Multiple Plots
================================================

.. plandisplay:: plans.json
   :plan: Create Grid of Multiple Plots


With this plan, we use the FacetGrid function to split our data over a grid, and create multiple plots for each split of the data.

FacetGrid is a powerful seaborn tool that allows you to visualize the distribution of one variable as well as the relationship between two variables, across levels of additional categorical variables. FacetGrid creates a grid of subplots based on the unique values in the categorical variable specified.

Plan 4 - When to use this plan?
--------------------------------

Use this plan when you have a categorical variable and want to create a subplot for each level of the category to compare trends or distributions, without combining them all into one graph.


Plan 4 - What parts can be customized to use this plan?
-------------------------------------------------------

To use this plan, you first need to replace *data_split_col* with a categorical variable in the dataset. This variable is used to create the grid, so for each unique value of this variable, there will be another plot in the grid.

Replace the *plot_type* with the type of plot you want to see in each cell of the grid. For instance, **sns.boxplot** from 'Plan 3 - Create a Box Plot' is a plot type you can use here. In our weather example, we used **sns.barplot**. We explore bar plots in the next plan.

Replace *x* and *y* with the columns that you want to compare from the DataFrame, and *palette* to the other preset seaborn color schemes. 


Plan 4 - Exercises
--------------------

.. image:: _static/box-plot-grid.png
   :scale: 90%
   :align: center
   :alt: A grid plot.


.. fillintheblank:: fitb_grid
   :code_template:
      import seaborn as sns
      dataset = load_dataset("bus_data")
      grid = sns.FacetGrid(dataset, col='@@blank1@@', sharey=False)
      grid.map(@@blank2@@, '@@blank3@@', '@@blank4@@', palette='Set2', errorbar=None)
      display(grid)
   :correct: ["season", "sns.boxplot", "bus_line", "ridership"]
   :feedback: ["The first box is incorrect. This box represents the variable that we use to split the data and create the grid. In this example, we split our data as Summer and Winter. Which column could represent that?", "The second box is incorrect. This should be a Seaborn plotting function, such as sns.boxplot or sns.barplot.", "The third box is incorrect. x-axis is our horizontal axis. What column of the data is plotted on the horizontal axis?", "The fourth box is incorrect. y-axis is our vertical axis. What column of the data is plotted on the vertical axis?"]
   :placeholder: ["", "", "x", "y"]

   Look at the plot above the question, which represents the distribution of the number of bus riders on three different lines for summer and winter. What code could have generated that? The dataset has three columns: "bus_line", "ridership", and "season". Using this information, fill in the blanks below to complete the code.
   






.. highlightedtextbox::
   :title:
   :color: #f4e36e
   :highlight-color: #ffe53e
   :highlight-on-load:

   Check out the plan below to learn more about barplots.

.. toctree::
   :maxdepth: 1

   pfp-plan5-bar.rst

.. plandisplay::
   :plan: Create a Box Plot
