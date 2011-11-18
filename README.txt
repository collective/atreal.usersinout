.. contents::

Overview
========

This plone product allows you to import / export portal's members within CSV
files. Few properties may equally been set.


Description
===========

* after being installed with the Quickinstaller tool, it adds an additional
  item in the control panel.
  
* Informations concerned are those managed by portal_registration and portal_membership.
  (i.e. username, password, roles, emails, location, description ...)

* A CSV template is directly available via the control panel, to use as a base
  for your own CSV file.

* There is no pretreatment. Data are used out-of-the-box. If any error occured
  in the CSV while importing, you have to correct those yourself.
  
* On errors, this product allows you to download a CSV file only filled with the
  matching lines. Use it to correct your errors, then retry.
  
  
Installation
============

* Use buildout, add atreal.usersinout in both of your egg and zcml sections.


Important
=========

Off course, those functionalities are only available for member with 'Manager' role.


Note
====

* Adding member in group(s) is now supported, but currently the export not
  implemented. 
* Global roles can be imported but currently not exported. Will be implemented soon.


Authors
=======

|atreal|_

* `atReal Team`_

  - Matthias Broquet [tiazma]

.. |atreal| image:: http://www.atreal.fr/medias/atreal-logo-48.png
.. _atreal: http://www.atreal.fr/
.. _atReal Team: mailto:contact@atreal.fr


Contributors
============

* `atReal Team`_

  - Romain BEYLERIAN [rbeylerian]

.. _atReal Team: mailto:contact@atreal.fr


Credits
=======

Thanks to Simon Kaser <simu> from raptus - raptus.com for roles / groups export
and german translation.


TODO
====

* Customizable CSV header.
