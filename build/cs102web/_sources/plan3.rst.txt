..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".


..  shortname:: Plan3
..  description:: Worked examples plus practice for Plan 3.

.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: p3-

.. _plan_3:

Plan 3: Get info from all tags of a certain type
#################################################

To get information from the bb.q Chicken locations page, we need to figure out which tags we should get from the soup, and what information we should get from the tags. 

A great way to figure this out is to use the "inspect" function on your browser. 

.. image:: _static/bbq_inspect.gif
    :scale: 25%
    :align: center
    :alt: By inspecting the locations, we see that they are all h4 tags.


We see that we need to get info from all the ``h4`` tags from the webpage. The *text* in those tags has the information we need!

Looking closer at a tag
====================================

Behind every webpage is HTML code. HTML code is made up of *tags*.

Here is the tag that creates the name of one of the bb.q Chicken's IL locations. The tag is surrounded by the blue rectangle. It is an 'h4' tag.

.. image:: _static/bbq_h4_text.png
    :scale: 50%
    :align: center
    :alt: h4 tag example

The name of this tag is 'h4'. In-between the start and end tag (between the ``<h4>`` and ``</h4>`` is the tag's **text**. For this tag, the text is **bb.q Chicken Urbana Champaign Urbana, IL**. The ``<br>`` tag stands for **break** and adds a line break to the text.

Plan 3: Example
====================================

Here is how to get **text** from all the **'h4'** tags from webpage:

.. raw:: html

   <pre>Goal: Get info from all tags of a certain type
   <pre style="background-color:#D5F5E3;">
   <strong># Get all tags of <mark>a certain type</mark> from the soup</strong>
   tags = soup.find_all(<mark>'h4'</mark>)
   <strong># Collect info from the tags</strong>
   collect_info = []
   for tag in tags:
       <strong># Get <mark>info</mark> from tag</strong>
       info = tag.<mark>text</mark>
       collect_info.append(info)</pre></pre>



Plan 3: How to use it
====================================

Once you've found the tags you want to get information from, do two things:

1. Find the **tag description** and put it into the first slot.

How do you do that? Here are some examples:

==================================== === ===========================  
What you see when you inspect            Tag description in the code
==================================== === ===========================  
``<p>``                              ->  ``'p'``
``<h3>``                             ->  ``'h3'``
``<div class="comment">``            ->  ``'div', class_='comment'``
``<span style="X5e72;">``            ->  ``'span', style='X5e72;'``
``<a class="css4z" href="/orders">`` ->  ``'a', class_='css4z'``
==================================== === ===========================  

2. Determine if you want to get **text** from a tag, or a **link** from a tag. Put that information into the second slot.

================= === ===========================  
The info you want     What you put in the code
================= === ===========================  
The tag's text    ->  ``text``
The tag's link    ->  ``get('href')``
================= === ===========================  


Plan 3: Exercises
====================================
.. mchoice:: get_text_mc_1
    :random:

    What is the text of the tag below?

    .. image:: _static/dining_h2_text.png
        :align: center
        :alt: h2 tag on dining page
    
    -   Today's Menu

        +   Correct! This text is between the <h2 class="menuItem"> and </h2>

    -   h2

        -   No, h2 is the tag name

    -   menuTitle

        -   No

    -   class

        -   No


.. mchoice:: get_tag_description_mc_1
    :random:

    What is the tag description of the tag below?

    .. image:: _static/dining_h2_text.png
        :align: center
        :alt: h2 tag on dining page
    
    -   'h2', class_='menuTitle'

        +   Correct! This is how you would describe the tag type in our web scraping code.

    -   'h2'

        -   That is a part of the tag description, but we can be more specific.

    -   'h2', class='menuTitle'

        -   Very close, but in web scraping code you should use "class_"

    -   <h2 class="menuTitle">

        -   This is what is actually in the tag, but it's not how we would describe the tag in web scraping code.

.. clickablearea:: plan3_click
    :question: Right now, this code gets the *text* from all 'h3' tags in the webpage. If you wanted to get the *links* from all the 'a', class_='headline' tags in the webpage, which part(s) of the code below would you change?
    :iscode:
    :feedback: Check out "how to use this plan".

    # Get all tags of a certain type from the soup
    :click-incorrect:tags = soup.find_all(:endclick::click-correct:'h3':endclick::click-incorrect:):endclick:
   
    # Collect info from the tags
    :click-incorrect:collect_info = []:endclick:
    :click-incorrect:for tag in tags::endclick:
        :click-incorrect:# Get info from tag:endclick:
        :click-incorrect:info = tag.:endclick::click-correct:text:endclick:
        :click-incorrect:collect_info.append(info):endclick:


.. fillintheblank:: plan3_fill_v2

   Fill in the plan in order to get the text from all ``<div class="headline">`` tags on a webpage.

   ``# Get all tags of a certain type from the soup``

   ``tags = soup.find_all(`` |blank| ``)``
   
   ``# Collect info from the tags``

   ``collect_info = []``

   ``for tag in tags:``

       ``# Get info from tag``

       ``info = tag.`` |blank|
      
       ``collect_info.append(info)``

   -    :['"]div['"], class_=['"]headline['"]: Correct.  
        :['"]div['"], class=['"]headline['"]: Very close--but class should be "class_!"
        :div: Good start, but you need more. 
        :.*: Incorrect. 
   -    :text: Correct.
        :get('href'): Remember that you are trying to get the text.
        :.text: Incorrect, the . is already there.
        :.*: Incorrect.   





.. mchoice:: get_text_mc_2
    :random:

    Which tag in the picture below has text?

    .. image:: _static/info_p_text.png
        :align: center
        :alt: span tag on dining page

    -   'h2'

        -   No, there is no h2 tag in this image.

    -   'p'

        +   Correct! The text starts with "Information Science focuses on how people use..."

    -   span, style=’font-weight: 400;’'

        -   No, this tag contains the p tag.

    -   'style'

        -   No, style is an attribute


.. note:: 
      
        .. raw:: html

           <a href="/ns/books/published/cs102web/example1.html" >Click here to go back to the bb.q Chicken example</a>

