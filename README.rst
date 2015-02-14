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

    $ NOVICE2=http://www.halhigdon.com/training/51138/Marathon-Novice-2-Training-Program
    $ /higdon.py $NOVICE2 "May 10, 2015"

This generates a file, ``Marathon-Novice-2.2015-05-10.ics``,
for loading into your favorite calendar app.

.. _Novice 2: http://www.halhigdon.com/training/51138/Marathon-Novice-2-Training-Program
.. _Eugene Marathon: http://eugenemarathon.com

Installation
------------

Using pip_:

.. code-block:: console

    $ pip3 install -e git+https://github.com/baldwint/higdon.git#egg=higdon

Or, if you wish to install dependencies yourself, just download
``higdon.py`` and run that directly.

.. _pip: http://www.pip-installer.org/
