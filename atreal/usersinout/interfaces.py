"""
"""

from zope.interface import Interface
from zope.app.container.constraints import contains
from zope import schema

from atreal.usersinout import UsersInOutMessageFactory as _

class IUsersInOutLayer(Interface):
    """ Marker interface that defines a Zope 3 browser layer.
    """

