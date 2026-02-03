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
   :prefix: p1-

.. _plan_1:

Plan 1: Get a soup from a URL
#####################################

Plan 1: Example
====================================

The first step in web scraping is getting information from a webpage. 
To use the BeautifulSoup web scraping library, we have to put the webpage into something called a *soup*.

Here is the code for getting a **soup** from the **bb.q Chicken locations page**.

.. raw:: html

  <pre>Goal: Get a soup from one webpage
  <pre style="background-color:#FCF3CF;">
  <strong># Load libraries for web scraping</strong>
  from bs4 import BeautifulSoup
  import requests
  <strong># Get a soup from <mark style="background-color:#F1948A">a URL</mark></strong>
  url = <mark style="background-color:#F1948A">'https://web.archive.org/web/20250309231002/https://bbqchicken.com/locations/'</mark>
  r = requests.get(url)
  soup = BeautifulSoup(r.content, 'html.parser')</pre></pre>

Plan 1: When to use this plan
====================================

Use this plan when you want to scrape **one webpage**.

Plan 1: How to use this plan
====================================

**Replace the URL with the URL of the website you want to scrape.**

A URL is a web address, like you see in your web browser. 
It should be complete (starting with http:// or https://). 
In this plan, a URL should be surrounded by quotes (:code:`' '`).

.. image:: _static/bbq_URL.gif
    :scale: 25%
    :align: center
    :alt: Copying a URL from the bb.q Chicken locations page


Plan 1: Exercises
====================================

.. clickablearea:: plan1_click
    :question: If you wanted to get a soup from the Illini Union Bookstore homepage instead of the bb.q Chicken locations page, which part(s) of the code below would you change? Click on those part(s) of the code.
    :iscode:
    :feedback: Check out the example of this plan above to identify the area that should be changed.

    :click-incorrect:# Load libraries for web scraping:endclick:
    :click-incorrect:from bs4 import BeautifulSoup:endclick:
    :click-incorrect:import requests:endclick:

    :click-incorrect:# Get a soup from a URL:endclick: 
    :click-incorrect:url =:endclick: :click-correct:'https://bbqchicken.com/locations/':endclick:
    :click-incorrect:r = requests.get(url):endclick:
    :click-incorrect:soup = BeautifulSoup(r.content, 'html.parser')::endclick:

.. fillintheblank:: plan1_fill

   Fill in the plan in order to get a soup from the University of Illinois Urbana-Champaign wikipedia page.

   ``# Load libraries for web scraping``

   ``from bs4 import BeautifulSoup``

   ``import requests``

   ``# Get a soup from a URL`` 

   ``url =`` |blank|

   ``r = requests.get(url)``

   ``soup = BeautifulSoup(r.content, 'html.parser')``


   -    :['"]https://en.wikipedia.org/wiki/University_of_Illinois_Urbana-Champaign['"]: Correct.  
        :https://en.wikipedia.org/wiki/University_of_Illinois_Urbana-Champaign: Remember that URLs in this plan should have quotes around them.
        :en.wikipedia.org/wiki/University_of_Illinois_Urbana-Champaign: Remember that URLs in this plan should start with https:// or http://
        :.*: Incorrect. 
        

.. note:: 
      
        .. raw:: html

           <a href="/ns/books/published/cs102web/example1.html" >Click here to go back to the bb.q Chicken example</a>


 
