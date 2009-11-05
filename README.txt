==================================
atreal.usersinout Package Readme
==================================

Overview
--------

This plone product allows you to import / export portal's members within CSV
files. Few properties may equally been set.


Description
-----------

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
------------

* Use buildout, add atreal.usersinout in both of your eggs and zcml sections.


Important
---------

Off course, those functionalities are only available for member with 'Manager' role.


Note
----

* Adding member in group(s) will supported, but is currently not implemented. This
  is the reason why you'll find a 'groups' fied in the CSV file. Leave it empty.
* Global roles can be imported but currently not exported. Will be implemented soon.


Authors
-------

:atReal Team - contac@atreal.net :
Matthias Broquet <tiazma>


TODO
----

* Groups support (import and export).
* Roles support (export only)
* Customizable CSV header.
* French translations.
