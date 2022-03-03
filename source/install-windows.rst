:orphan:

.. _install-windows:

Installing oTree on Windows
===========================

Important note
--------------

If you publish research done with oTree,
you are required to cite
`this paper <http://dx.doi.org/10.1016/j.jbef.2015.12.001>`__.
(Citation: Chen, D.L., Schonger, M., Wickens, C., 2016. oTree - An open-source
platform for laboratory, online and field experiments.
Journal of Behavioral and Experimental Finance, vol 9: 88-97)

If the below steps don't work for you, please email chris@otree.org with details.

Step 1: Install Python
----------------------

Download and install `Python <https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe>`__.

Check the box to add Python to PATH:

.. figure:: _static/setup/py-win-installer-37.png

Step 2: Install oTree
---------------------

Go to the folder where you want to store your oTree project.
Then click the "File" menu and open PowerShell:

.. figure:: _static/setup/open-powershell.png

Enter this command at the prompt:

.. code-block:: bash

    pip3 install -U otree

Next steps
----------

-   If you will use :ref:`oTree Studio <studio>` (recommended),
    go to `otreehub.com <https://www.otreehub.com>`__.
-   If you are experienced in programming and want to use a text editor,
    follow the steps :ref:`here <install-nostudio>`.
