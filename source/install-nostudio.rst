:orphan:

.. _install-nostudio:

oTree Setup (text editor)
=========================

Note: it's recommended to use `oTree Studio <https://www.otreehub.com/studio>`__
since it is specifically designed for building oTree apps.
You can easily switch to using a text editor later, by downloading your code.

Run oTree
---------

If you're on MacOS, run::

    /Applications/Python\ 3.9/Install\ Certificates.command

(If you are not using version 3.9 of Python, edit the above command appropriately.)

From your command prompt, create your project folder::

    otree startproject myproject

When it asks you "Include sample games?" choose yes.

Move into the folder you just created::

    cd myproject


**If you see a ``models.py`` in each folder, then switch to the documentation here:**
`https://otree.readthedocs.io/en/self/ <https://otree.readthedocs.io/en/self/>`__

If you don't see a models.py in each folder, that means you are using the new no-self format.

Run the server::

    otree devserver

Open your browser to `http://localhost:8000/ <http://localhost:8000/>`__.
You should see the oTree demo site.

To stop the server, press ``Control + C`` at your command line.

To create a new app, run ``otree startapp your_app_name``.

Session configs are defined in ``settings.py``.

About @staticmethod, etc.
-------------------------

If you are using a text editor to write your oTree code, remember to add ``@staticmethod`` before
all functions inside a page class, like ``is_displayed``, ``vars_for_template``, ``before_next_page``, etc.
They are sometimes omitted from this documentation for brevity.
They are not mandatory but will help your editor provide better autocompletion.

If you are using PyCharm, VS Code, or another IDE, you can also add type annotations on your functions.

For example:

.. code-block:: python

    @staticmethod
    def is_displayed(player: Player):
        ...

Or:

.. code-block:: python

    def creating_session(subsession: Subsession):
        ...


Upgrading/reinstalling oTree
----------------------------

We recommend upgrading every couple of weeks.

.. code-block:: bash

    pip3 install -U otree

The best way to ensure that your apps continue to work after you upgrade is to
use only the functions described in this documentation.
Some code snippets you may find online were written by people who access oTree's internal functions
and "hack" them to do something different.
Although these snippets can enable some innovative new functionality,
be aware that they increase the chance of things breaking when you upgrade,
because oTree's internal code layout changes from release to release.
