..  shortname:: customize

..  description:: Customize a plot


.. setup for automatic question numbering.

.. qnum::
   :start: 1

Plan 6: Customize Figure
========================

.. plandisplay:: plans.json
   :plan: Customize Figure

The next step in data visualization is making sure your graph is clear to be easily analyzed by others. Seaborn is a powerful data visualization library that provides numerous ways to customize the appearance of plots. Customizing Seaborn plots is an essential part of creating meaningful and visually appealing visualizations. 
Customizing allows you to clearly define what each axis represents and adjust the rotation of your labels so they do not overlap.

Plan 6 - When to use this plan?
--------------------------------
Use this plan when your graph labels are overlapping, or you need to add descriptive titles to explain your figure more clearly.


Plan 6 - What parts can be customized to use this plan?
-------------------------------------------------------
Replace the text in *title*, *xlabel*, and *ylabel* to describe your specific data. If the x-axis names are too long, you can rotate them for a better fit using *angle*.


**Challenge**: can you add a title and labels to the plot below, using the template you have just learned?


.. activecode:: ct_title
   :language: python3

   from tutorial.main import load_dataset, display
   import seaborn as sns

   # load the tips dataset from Seaborn
   restaurants = load_dataset("restaurants")

   # create the boxplot from above
   figure = sns.boxplot(x="restaurant_name", y="rating", hue="cost", data=restaurants, palette="magma")

   # TODO -- add labels and title here


   # display the plot
   display(figure)


.. reveal:: debug_code_cl_reveal_1
        :showtitle: Click here to reveal the code for adding a title.
        :hidetitle: Hide this code.

        .. code-block:: python
           
           figure.set_xlabel("Restaurant Names")
           figure.set_ylabel("Ratings (1-5)")
           figure.set_title("Restaurant ratings in Champaign, organized by cost")




Plan 6 - Exercises
--------------------
.. mchoice:: rotation_question
   :answer_a: figure.tick_params(axis='x', labelrotation=45)
   :feedback_a: Correct!
   :answer_b: figure.tick_params(axis='y', labelrotation=45)
   :feedback_b: No, this would rotate the labels on the vertical axis (y-axis).
   :answer_c: figure.set_xlabel(45)
   :feedback_c: No, this would set the label for the x-axis to "45", but it would not rotate the labels.
   :answer_d: figure.tick_params(axis='x', labelrotation=90)
   :feedback_d: No, this would rotate the labels so that they would seem as vertical.
   :correct: b

   How would you rotate the labels on the horizontal axis diagonally (e.g. similar to the image below)?

   .. image:: _static/diagonal-label.png
      :scale: 45%
      :align: left
      :alt: An x-axis with diagonal labels.
    

.. highlightedtextbox::
   :title:
   :color: #f4e36e
   :highlight-color: #ffe53e
   :highlight-on-load:

   If you completed all the activities on this page, click on the arrow on the bottom right to continue.