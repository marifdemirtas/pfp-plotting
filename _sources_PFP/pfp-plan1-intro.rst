..  shortname:: intro

..  description:: Import necessary packages and import data


.. setup for automatic question numbering.

.. qnum::
   :start: 1

Plan 1: Import Packages and Load Data
========================

.. plandisplay:: plans.json
   :plan: Import Packages and Load Data

The first step in data visualization is importing the necessary Python packages, and loading our dataset in a format that Python can understand. This includes importing Seaborn, but you might need additional packages, such as Matplotlib or Pandas, based on your problem.

Seaborn provides several built-in functions that we can use for data visualization and statistical analysis. These datasets are stored in pandas dataframes, making them easy to use with Seaborn's plotting functions.

For this tutorial, we provide you with a custom Python function, ‘load_dataset‘, which does all the data processing in the background and provides you with a DataFrame object you can use right away. Click on the code editor below to see the first example dataset, which shows ratings of 10 restaurants around the campus by 50 students.

.. activecode:: pfp-p1_data_loading_restaurant
   :language: python3

   from tutorial.main import load_dataset

   # Load the Restaurants dataset
   dataset = load_dataset("restaurants")

   # check the head
   print(dataset.head()) 


Plan 1 - When to use this plan?
--------------------------------
Use this plan when you want to visualize any dataset. You will need to import packages and load data for all visualizations!


Plan 1 - What parts can be customized to use this plan?
-------------------------------------------------------
Replace the *data_path* with the name of the dataset you want to load.


.. highlightedtextbox::
   :title:
   :color: #f4e36e
   :highlight-color: #ffe53e
   :highlight-on-load:

   If you have read through the description of this plan, click on the arrow on the bottom right to move to the next page.