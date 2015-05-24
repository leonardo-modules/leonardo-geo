
====================
Leonardo Google Maps
====================

Google Maps for Leonardo CMS

.. contents::
    :local:

Installation
------------

.. code-block:: bash

    pip install leonardo_geo

or as leonardo bundle

.. code-block:: bash

    pip install django-leonardo["geo"]

Add ``leonardo_geo`` to APPS list, in the ``local_settings.py``::

    APPS = [
    	...
        'leonardo_geo'
        ...
    ]


Load new template to db

.. code-block:: bash

	python manage.py sync_all
