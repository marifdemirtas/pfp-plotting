..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

..  shortname:: Example 1
..  description:: First example for showcasing Seaborn

.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: ex1-
   

Example 1: Finding the most reliable restaurants in Champaign area
###########################################################################################################


.. highlightedtextbox::
   :title:
   :color: #f4e36e
   :highlight-color: #ffe53e
   :highlight-on-load:
   
   We will start by exploring an example visualization problem about restaurants in Champaign. Read through the explanation below and run the code by clicking on 'Save and Run' to see how you can create a visualization for this problem!

At the University of Illinois Urbana-Champaign, a group of students completed a survey asking 50 students to rate 10 restaurants around the campus. After creating their *restaurants* dataset, the group wants to analyze the rating distribution of the restaurants in order to determine which restaurants are the most consistent in terms of student opinion.

The *restaurants* dataset looks like this:


+------------+--------------------------+--------+--------+
| student_id | Name                     | Rating | Cost   |
+============+==========================+========+========+
| 0          | Maize Mexican Grill      | 4      | Low    |
+------------+--------------------------+--------+--------+
| 5          | Maize Mexican Grill      | 2      | Low    |
+------------+--------------------------+--------+--------+
| 32         | Papa Del's Pizza Factory | 4      | High   |
+------------+--------------------------+--------+--------+
| 49         | Sakanaya                 | 5      | High   |
+------------+--------------------------+--------+--------+
| 27         | The Bread Company        | 3      | Medium |
+------------+--------------------------+--------+--------+

The goal is to use the student ratings of each restaurant to create 10 box plots in a single figure.

.. activecode:: pfp-restaurant-ex
   :language: python3

   from tutorial.main import display, load_dataset

   # Plan 1: Import Packages and Load Data
   import seaborn as sns

   dataset = load_dataset('restaurants')

   # Plan 3: Create a Box Plot
   figure = sns.boxplot(x="restaurant_name", y="rating", hue="cost", palette="magma", data=dataset)


   # Plan 6: Customize Figure  
   figure.set_title("Most reliable Champaign restaurants, organized by cost")
   figure.set_xlabel("Restaurant Name")
   figure.set_ylabel("Rating (1-5)")
   # Rotate x-axis labels for readability
   figure.tick_params(axis='x', labelrotation=90)

   
   # Plan 7: Display Figure
   display(figure)


.. stdoutimage::
  :source_id: pfp-restaurant-ex
  :title: Output Image
  :mime: image/png


.. highlightedtextbox::
   :title:
   :color: #f4e36e
   :highlight-color: #ffe53e
   :highlight-on-load:
   
   This code probably seems a bit complicated. In this ebook, we will break down each example into a few common "plans". Each "plan" is a piece of code that we will study in more detail.
   

This example is made up of four plans. Click on each of them to learn more.

.. toctree::
   :maxdepth: 1

   pfp-plan1-intro
   pfp-plan3-box
   pfp-plan6-customize
   pfp-plan7-display

.. highlightedtextbox::
   :title:
   :color: #f4e36e
   :highlight-color: #ffe53e
   :highlight-on-load:
   
   For each plan, you can see a 'template', which shows the generic version of that piece of code, and you can see an 'example', which shows what values you could put in that template in this particular example.

.. plandisplay::
   :plan: Import Packages and Load Data

.. plandisplay::
   :plan: Create a Box Plot

.. plandisplay::
   :plan: Customize Figure

.. plandisplay::
   :plan: Display Figure

.. highlightedtextbox::
   :title:
   :color: #f4e36e
   :highlight-color: #ffe53e
   :highlight-on-load:
   
   Click on the arrow on the bottom right to move to the page for the first plan.