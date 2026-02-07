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

For Seaborn, we usually have to put the data into something called a Pandas DataFrame. For this tutorial, we provide you with a custom Python function, ‘load_dataset‘, which does all the data processing in the background and provides you with a DataFrame object you can use right away. Click on the code editor below to see the first 5 entries in the restaurant dataset.

.. activecode:: pfp-p1_data_loading_restaurant
   :language: python3

   from tutorial.main import load_dataset

   # Load the Restaurants dataset
   restaurants = load_dataset("restaurants")

   # check the head
   print(restaurants.head()) 


Plan 1 - When to use this plan?
--------------------------------
Use this plan when you want to visualize any dataset.


Plan 1 - What parts can be customized to use this plan?
-------------------------------------------------------
Replace the *data_path* with the name of the dataset you want to load.


.. highlightedtextbox::
   :title:
   :color: #f4e36e
   :highlight-color: #ffe53e
   :highlight-on-load:

   If you completed all the activities on this page, click on the arrow on the bottom right to continue.