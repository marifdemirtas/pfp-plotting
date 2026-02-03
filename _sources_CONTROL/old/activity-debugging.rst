..  shortname:: Debugging
..  description:: Debugging activity.

.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: debugging-

Code debugging activity
:::::::::::::::::::::::::

Moore's Rescue Ranch in Champaign has |pets for adoption|. The code below is supposed to **get the webpage of adoptable cat Frodo, scrape the text of the description excerpt shown, and print it**.

.. |pets for adoption| raw:: html

        <a href="https://mooresrescueranch.org/product/frodo/"" target="_blank">pets for adoption</a>


.. image:: _static/frodo_adoption.png
    :scale: 40%
    :align: center
    :alt: Adoptable cat Frodo.

However, it doesn't work! Instead of printing the title text, it prints nothing.

Can you fix it? Here is the buggy code:

.. raw:: html

   <pre>Plan 1: Get a soup from a URL
   <a href="/ns/books/published/cs102web/plan1.html"><pre style="background-color:#FCF3CF;">
   <strong># Load libraries for web scraping</strong>
   from bs4 import BeautifulSoup
   import requests
   <strong># Get a soup from <mark>a URL</mark></strong> 
   url = <mark style="border:2px; border-style:solid; border-color:#1A5276; "background-color:#FCF3CF;">'https://mooresrescueranch.org/product/frodo/'</mark>
   r = requests.get(url)
   soup = BeautifulSoup(r.content, 'html.parser')</pre></a></pre>

   <pre>Plan 4: Get info from a single tag
   <a href="/ns/books/published/cs102web/plan4.html"><pre style="background-color:#A9DFBF;">
   <strong># Get first tag of <mark>a certain type</mark> from the soup</strong>
   tag = soup.find(<mark style="border:2px; border-style:solid; border-color:#1A5276; "background-color:#FCF3CF;">'p', class_='wp-block-post-excerpt__excerpt'</mark>)
   <strong># Get <mark>info</mark> from tag</strong>
   info = tag.<mark style="border:2px; border-style:solid; border-color:#1A5276">get('href')</mark></pre></a></pre>

   <pre>Plan 5: Print the info
   <a href="/ns/books/published/cs102web/plan5.html"><pre style="background-color:#D6EAF8;">
   <strong># Print <mark>the info</mark></strong>
   print(<mark style="border:2px; border-style:solid; border-color:#1A5276">info</mark>)</pre></a></pre>

Try to fix the buggy code below. Run the code to save your progress.

.. activecode:: debug_code_1
        :language: python3
        :nocodelens:

        #Get the webpage
        # Load libraries for web scraping
        from bs4 import BeautifulSoup
        import requests
        # Get a soup from a URL 
        url = 'https://mooresrescueranch.org/product/frodo/'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')

        #Get info from one tag
        # Get first tag of a certain type from the soup
        tag = soup.find('p', class_='wp-block-post-excerpt__excerpt')
        # Get info from tag
        info = tag.get('href')

        #Do something with the info
        # Print the info
        print(info)


.. sidebar:: Links to plans

    |plan_1|

    |plan_2|

    |plan_3|

    |plan_4|

    |plan_5|

    .. |plan_1| raw:: html


        <a href="/ns/books/published/cs102web/plan1.html" target="_blank">Plan 1: Get a soup from a URL</a>

    .. |plan_2| raw:: html

        <a href="/ns/books/published/cs102web/plan2.html" target="_blank">Plan 2: Get a soup from multiple URLs</a> 

    .. |plan_3| raw:: html

        <a href="/ns/books/published/cs102web/plan3.html" target="_blank">Plan 3: Get info from all tags of a certain type</a> 

    .. |plan_4| raw:: html

        <a href="/ns/books/published/cs102web/plan4.html" target="_blank">Plan 4: Get info from a single tag</a>
   
    .. |plan_5| raw:: html

        <a href="/ns/books/published/cs102web/plan5.html" target="_blank">Plan 5: Print info</a> 


