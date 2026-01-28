..  shortname:: Writing
..  description:: Writing activity.

.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: writing1-


Code writing activity part 1
:::::::::::::::::::::::::::::

On this page, you will complete an activity to write code that:

**Scrapes all the comments on the Rate My Professor page for Prof. Geoffrey Herman and Prof. Abdu Alawini and prints them**

Here is |alawini_link|.

Here is |herman_link|.

.. |alawini_link| raw:: html

   <a href="https://www.ratemyprofessors.com/professor/2442487" target="_blank">the link to Prof. Herman's Rate My Professor page</a>

.. |herman_link| raw:: html

   <a href="https://www.ratemyprofessors.com/professor/1799030" target="_blank">the link to Prof. Alawini's Rate My Professor page</a> 

You can see that both the pages have the same layout.

.. image:: _static/rate_my_prof_herman.png
    :scale: 20%
    :align: center
    :alt: Prof. Herman's Rate My Professor page

.. image:: _static/rate_my_prof_alawini.png
    :scale: 20%
    :align: center
    :alt: Prof. Alawini's Rate My Professor page

The comments all have the same tag name, which is ``'div'`` tag with ``class='Comments__StyledComments-dzzyvm-0 dvnRbr'``. Here's what it looks like when you inspect Prof. Herman's page:

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



.. parsonsprob:: write_code_order_plans_goals
   
   Choose which of the following plans you will use, and put them in the correct order.
   
   -----
   Plan #2: Get a soup from multiple webpages
   =====
   Plan #1: Get a soup from a webpage#paired
   =====
   Plan #3: Get info from all tags of a certain type
   =====
   Plan #4: Get info from a single tag#paired
   =====
   Plan #5: Print info




