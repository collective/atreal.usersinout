Changelog
=========

1.2.4 (unreleased)
------------------

- Nothing changed yet.


1.2.3 (2015-10-27)
------------------

- Add uninstall profile.
  [thet]

- Support of password export, from this blueprint:
  http://play.pixelblaster.ro/blog/archive/2011/03/09/export-import-users-in-and-out-of-plone
  [thet]

- Add ``z3c.autoinclude.plugin`` entry point.
  [thet]

- PEP 8, cleanup.
  [thet]


1.2.2 (2011-11-28)
------------------

* Fix behaviour when creating user with no group. [rbeylerian]


1.2.1 (2011-11-18)
------------------

* Update README.txt
  [rbeylerian]

* Added conditional include of CMFCore permisssions.zcml for Plone 4.1 support
  [rbeylerian]

* Update MANIFEST.in (now including docs folder, txt and .mo files)
  [rbeylerian]


1.2
----------------

* Added export support for roles and groups [simu]
* Added filtering for results of acl_users.searchUsers to ignore entries from mutable_properties plugin which resulted in duplicate entries for users and entries for groups [simu]
* Fixed AttributeError raised when exporting and portal_membership.getMemberById returns None (eg. if there are groups created over the plone UI) [simu]
* Added german translation [simu]



1.1 beta1
----------------

* Added group creation / member assignment
* Corrected bug #2
  http://plone.org/products/atreal.usersinout/issues/2
* Typos in french translation
  [tiazma]



1.0 beta4
----------------

* Added translation support
* Added french translations
  [Matthias Broquet a.k.a tiazma]


1.0 - Unreleased
----------------

* Initial release
  [Matthias Broquet a.k.a tiazma]

