..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.2 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".


..  shortname:: Plan2
..  description:: Worked examples plus practice for Plan 2.

.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: p2-

.. _plan_2:

Plan 2: Get a soup from multiple URLs
#####################################

Plan 2: Example
====================================

Sometimes we want to get information from multiple web pages that have the same layout. For example, all of the SCDS faculty pages have the same general design.

.. image:: _static/katie_cunningham.png
    :scale: 20%
    :align: center
    :alt: Plan 2 outline

.. image:: _static/geoffrey_challen.png
    :scale: 20%
    :align: center
    :alt: Plan 2 outline

We are interested in getting information about mutliple SCDS professors: Prof. Katie Cunningham, Prof. Geoffrey Challen, and Prof. Michael Nowak. 

Their webpages are:

``https://siebelschool.illinois.edu/about/people/faculty/katcun``

``https://siebelschool.illinois.edu/about/people/faculty/challen``

``https://siebelschool.illinois.edu/about/people/faculty/mnowak1``

In this code, we get a **soup** from multiple **SCDS faculty pages**.

.. raw:: html

   <pre>Goal: Get a soup from multiple webpages
   <pre style="background-color:#FDEBD0;">
   <strong># Load libraries for web scraping</strong>
   from bs4 import BeautifulSoup
   import requests
   <strong># Get a soup from <mark style="background-color:#FEF5E7">multiple URLs</mark></strong>
   base_url = <mark style="background-color:#FEF5E7">'https://siebelschool.illinois.edu/about/people/faculty/'</mark>
   endings = <mark style="background-color:#FEF5E7">['katcun', 'challen', 'mnowak1']</mark>
   for ending in endings:
       url = base_url + ending
       r = requests.get(url)
       soup = BeautifulSoup(r.content, 'html.parser')</pre></pre>


Plan 2: When to use this plan
====================================

Use this plan when you want to scrape the same thing from multiple webpages.

Plan 2: How to use this plan
====================================

Look at the webpages you want to scrape and determine which parts they have in common, and which parts are different. The parts that they have in common are the ``base_url``. The parts that are different are the ``endings``.

Plan 2: Exercises
====================================

If you want to also get the link to the most recent news item from Director Nancy Amato's page, how would you change the code below? Director Amato's web page is ``https://siebelschool.illinois.edu/about/people/faculty/namato``.

Change the code and run it to see if you're right!

.. activecode:: plan2_edit_finholt
   :language: python3
   :nocodelens:

   #Get the webpage
   # Load libraries for web scraping
   from bs4 import BeautifulSoup
   import requests
   # Get a soup from multiple URLs
   base_url = 'https://web.archive.org/web/20250314223200/https://siebelschool.illinois.edu/about/people/faculty/' # replaced with web archive link for tutorial purposes
   endings = ['katcun', 'challen', 'mnowak1']
   for ending in endings:
       url = base_url + ending
       r = requests.get(url)
       soup = BeautifulSoup(r.content, 'html.parser')

       #Extract info from the page
       # Get first tag of a certain type from the soup
       tag = soup.find('a', class_='text-decoration-none')
       # Get link from tag
       info = tag.get('href')  

       #Do something with the info
       # Print the info
       print(info)


.. note:: 
      
        .. raw:: html

           <a href="/ns/books/published/cs102web/example2.html" >Click here to go back to the Faculty Pages example</a>

