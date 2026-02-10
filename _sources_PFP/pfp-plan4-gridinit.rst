..  shortname:: gridinit

..  description:: Initialize a FacetGrid


.. setup for automatic question numbering.

.. qnum::
   :start: 1

Plan 4: Initialize a FacetGrid
========================

.. plandisplay:: plans.json
   :plan: Initialize FacetGrid


A FacetGrid is a great way to simultaneously visualize relationships across different subsets of the dataset in the format of grids. Each unique value within the column in the dataset will have its own subplot.


Plan 4 - When to use this plan?
--------------------------------

Use this plan when you have a categorical variable and want to create a subplot for each level of the category to compare trends or distributions without combining them all into one graph.


Plan 4 - What parts can be customized to use this plan?
-------------------------------------------------------

Replace the col value with the column name you want to split the dataset by. The sharey can be set to True if you want all the subplots to use the same y-axis, and False if not.


Plan 4 - Exercises
--------------------

.. highlightedtextbox::
   :title:
   :color: #f4e36e
   :highlight-color: #ffe53e
   :highlight-on-load:

   If you completed all the activities on this page, click on the arrow on the bottom right to continue.