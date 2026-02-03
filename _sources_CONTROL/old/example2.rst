..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

..  shortname:: Plan1
..  description:: Worked examples plus practice for Plan 1.

.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: ex2-
   

Get news links from faculty webpages
#####################################

Let's say that you want to get the link to the first news article on your favorite SCDS faculty's webpages. 

.. image:: _static/faculty_pages_scoll.gif
    :scale: 20%
    :align: center
    :alt: News articles on faculty pages


But clicking through to gather all those links would be a pain. Fortunately, we can do that task with BeautifulSoup! 

Run the code below to see what it collects.

.. activecode:: prof_homepages_example
   :language: python3
   :nocodelens:

   #Get the webpages
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
       # Get info from tag
       info = tag.get('href')  

       #Do something with the info
       # Print the info
       print(info)

This code is made up of three plans. Click on each of the plans below to learn more about it.

.. toctree::
    :maxdepth: 1
    
    plan2
    plan4
    plan5

.. raw:: html

   <pre><strong>Plan 2: Get a soup from multiple URLs</strong>
   <a href="/ns/books/published/cs102web/plan2.html"><pre style="background-color:#FDEBD0;">
   # Load libraries for web scraping
   from bs4 import BeautifulSoup
   import requests
   # Get a soup from multiple URLs
   base_url = 'https://siebelschool.illinois.edu/about/people/faculty/'
   endings = ['katcun', 'challen', 'mnowak1']
   for ending in endings:
       url = base_url + ending
       r = requests.get(url)
       soup = BeautifulSoup(r.content, 'html.parser')</pre></a></pre>
       <pre><strong>Plan 4: Get info from a single tag</strong><a href="/ns/books/published/cs102web/plan4.html"><pre style="background-color:#A9DFBF;">
       # Get first tag of a certain type from the soup
       tag = soup.find('a', class_='text-decoration-none')
       # Get info from tag
       info = tag.get('href')</pre></a></pre>  
       <pre><strong>Plan 5: Print info</strong><a href="/ns/books/published/cs102web/plan5.html"><pre style="background-color:#D6EAF8;">
       # Print the info
       print(info)</pre></a></pre>
