..  shortname:: customize

..  description:: Customize a plot


.. setup for automatic question numbering.

.. qnum::
   :start: 1

Plan 6: Customize Figure
========================

.. plandisplay:: plans.json
   :plan: Customize Figure

The final step is making sure your graph is clear to be easily analyzed by others. By default, Python might choose labels that do not fit what you are trying to show with your data. Customizing allows you to clearly define what each axis represents and adjust the rotation of your labels so they do not overlap.

Plan 6 - When to use this plan?
--------------------------------
Use this plan when your graph labels are overlapping, or you need to add descriptive titles to explain your figure more clearly.


Plan 6 - What parts can be customized to use this plan?
-------------------------------------------------------
Replace the text in *title*, *xlabel*, and *ylabel* to describe your specific data. If the x-axis names are too long, you can rotate them for a better fit using *angle*.


Plan 6 - Exercises
--------------------
.. mchoice:: rotation_question
   :answer_a: figure.tick_params(axis='x', labelrotation=45)
   :feedback_a: Correct!
   :answer_b: figure.tick_params(axis='y', labelrotation=45)
   :feedback_b: No, this would rotate the labels on the vertical axis (y-axis).
   :answer_c: figure.set_xlabel(45)
   :feedback_c: No, this would set the label for the x-axis to "45", but it would not rotate the labels.
   :answer_d: figure.tick_params(axis='x', labelrotation=45)
   :feedback_d: No, this would rotate the labels so that they would seem as vertical.
   :correct: b

   How would you rotate the labels on the horizontal axis diagonally (e.g. similar to the image below)?

.. image:: _static/update.png
    :scale: 45%
    :align: left
    :alt: An x-axis with diagonal labels.
    

.. highlightedtextbox::
   :title:
   :color: #f4e36e
   :highlight-color: #ffe53e
   :highlight-on-load:

   If you completed all the activities on this page, click on the arrow on the bottom right to continue.