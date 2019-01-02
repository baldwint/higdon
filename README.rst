Training Calendar Generator
===========================

This simple program generates a ``.ics`` calendar file from a Hal
Higdon training plan, tailored to a race day that you specify.

Usage
-----

Specify the URL of the plan you wish to use, and the target race day.
For example, to make a calendar for the 2015 `Eugene Marathon`_, using
the `Novice 2`_ plan:

.. code-block:: console

    $ NOVICE2=https://www.halhigdon.com/training-programs/marathon-training/novice-2-marathon/
    $ higdon $NOVICE2 "May 10, 2015"

This generates a file, ``novice-2-marathon.2015-05-10.ics``,
for loading into your favorite calendar app.

.. _Novice 2: https://www.halhigdon.com/training-programs/marathon-training/novice-2-marathon/
.. _Eugene Marathon: http://eugenemarathon.com

Installation
------------

Using pip_:

.. code-block:: console

    $ pip3 install higdon

Development version:

.. code-block:: console

    $ pip3 install -e git+https://github.com/baldwint/higdon.git#egg=higdon

Or, if you wish to install dependencies yourself, just download
``higdon.py`` and run that directly.

.. _pip: http://www.pip-installer.org/
