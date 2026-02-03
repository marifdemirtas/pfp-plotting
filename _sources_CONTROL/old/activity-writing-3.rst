..  shortname:: Writing 2
..  description:: Writing activity 2.

.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: writing3-


Code writing activity part 3
:::::::::::::::::::::::::::::

On this page, you will complete the final activity to write code that:

**Scrapes all the comments on the Rate My Professor page for Prof. Geoffrey Herman and Prof. Abdu Alawini and prints them**

Here is |alawini_link|.

Here is |herman_link|.

.. |herman_link| raw:: html

   <a href="https://web.archive.org/web/20250331181529/https://www.ratemyprofessors.com/professor/2442487" target="_blank">the link to Prof. Herman's Rate My Professor page</a>

.. |alawini_link| raw:: html

   <a href="https://web.archive.org/web/20250331181529/https://www.ratemyprofessors.com/professor/1799030" target="_blank">the link to Prof. Alawini's Rate My Professor page</a> 

You can see that both the pages have the same layout.

.. image:: _static/rate_my_prof_herman.png
    :scale: 20%
    :align: center
    :alt: Prof. Herman's Rate My Professor page

.. image:: _static/rate_my_prof_alawini.png
    :scale: 20%
    :align: center
    :alt: Prof. Alawini's Rate My Professor page

The comments all have the same tag name, which is ``'div'`` tag with ``class='Comments__StyledComments-dzzyvm-0'``. Here's what it looks like when you inspect Prof. Herman's page:

.. image:: _static/rate_my_prof_herman_tags.png
    :scale: 40%
    :align: center
    :alt: Inspecting the tags on the Rate My Professor page


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

    
Here is the code that you assembled from the plans. 
Now that you've assembled the correct plans, fill in the blanks to complete the code.

.. activecode:: write_code_fill_in
        :language: python3
        :nocodelens:

        #Get the webpage
        # Load libraries for web scraping
        from bs4 import BeautifulSoup
        import requests
        # Get a soup from multiple URLs
        base_url = 'https://web.archive.org/web/20250331181529/https://www.ratemyprofessors.com/professor/'
        endings = ['_endings_go_here_', '_endings_go_here_']
        for ending in endings:
            url = base_url + ending
            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')

            # Get all tags of a certain type from the soup
            tags = soup.find_all(____tag_description_goes_here___)
            # Collect info from the tags
            collect_info = []
            for tag in tags:
                # Get info from tag
                info = tag.______
                collect_info.append(info)

            #Do something with the info
            # Print the info
            print(______)



