``django-settings-diff``
========================

A very simple tool to help diff two Django settings modules.

Motivation
----------

Let's say that you have done some significant refactoring to your settings module. For example, you have gone from a single settings file to a modular approach, where there is no longer a single ``settings.py``. You want to make sure that your settings are effectively *exactly* the same as before, though! Of course you can't rely on simple file diffing, since there is no longer a single ``settings.py``.

There are some non-intuitive things to account for, which ``django-settings-diff`` handles for you:

1. Even with a single ``settings.py``, there is a (potentially) significant difference between simply importing the file and the "final" settings that are used by Django (see https://docs.djangoproject.com/en/2.1/topics/settings/#using-settings-in-python-code). That is, we want to compare the *actual settings at runtime*!
2. The ``settings`` object cannot be naively treated as a ``dict`` -- it is similar, but different enough to prevent easy diffing.

So, it isn't doing anything crazy, but it removes some overhead.

Installation
------------

Install from pip (recommended):

::

    $ pip install django-settings-diff

Or, install straight from the repo:

::

    $ git clone https://github.com/GreenBankObservatory/django-settings-diff
    $ pip install django-settings-diff

Note that this will install a wrapper script for you: ``diffsettings``

Entry Points
------------

Use the wrapper script (recommended):

::

    $ diffsettings -h

Call the module:

::

    $ python -m django_settings_diff -h

Import as library:

::

    $ python
    >>> from django_settings_diff import diffsettings
    >>> help(diffsettings)

Usage
-----

There is a standard usage pattern that is intended.

Dump Settings
~~~~~~~~~~~~~

You should first ensure that you have saved two versions of your settings. For this example we will use ``myapp/settings_old.py`` and ``myapp/settings_new.py``.

Then, pickle the settings modules to disk:

::

    DJANGO_SETTINGS_MODULE=myapp.settings_old diffsettings --dump old_settings.pkl
    DJANGO_SETTINGS_MODULE=myapp.settings_new diffsettings --dump new_settings.pkl

Diff Settings
~~~~~~~~~~~~~

Now we can diff the two settings objects:

::

    diffsettings old_settings.pkl new_settings.pkl 

See the documentation for `deepdiff <https://github.com/seperman/deepdiff>`_ for help deciphering the output.
