..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

..  shortname:: Dataset
..  description:: Sample Datasets and Dataset Loading in Seaborn

.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: ex1-
   

Sample Datasets
###########################################

Seaborn provides several built-in functions that we can use for data visualization and statistical analysis. These datasets are stored in pandas dataframes, making them easy to use with Seaborn's plotting functions.

In this tutorial, we created two example datasets we will use that are saved in the same Pandas DataFrame format. The first one shows ratings of 10 restaurants around the campus by 50 students.
Here's how to load and preview this example dataset:

.. activecode:: ct_data_loading_restaurant
   :language: python3

   from tutorial.main import load_dataset

   # Load the Restaurants dataset
   restaurants = load_dataset("restaurants")

   # check the head
   print(restaurants.head()) 


Here's the other dataset, which shows records of the total precipitation and the average temperature in Champaign from 2015 to 2024.


.. activecode:: ct_data_loading_weather
   :language: python3

   from tutorial.main import load_dataset

   # Load the Restaurants dataset
   weather = load_dataset("weather")

   # check the head
   print(weather.head()) 


We will be using a slightly different version of this dataset, where the dataset is in *long form*, which means that different measurements for the same month (e.g. total precipitation and average temperature for January 2015) are separate rows of the table, as opposed to the *wide form*, where different measurements for the same month were in different columns of the same row. Seaborn uses long form data for most operations, and this is why we provide the long form version of the weather dataset.


.. activecode:: ct_data_loading_weather_long
   :language: python3

   from tutorial.main import load_dataset

   # Load the Restaurants dataset
   weather = load_dataset("weather_long")

   # check the head
   print(weather.head()) 

