# This module is automatically generated by autogen.sh. DO NOT EDIT.

from . import _OpenStack


class _Storage(_OpenStack):
    _type = "storage"
    _icon_dir = "resources/openstack/storage"


class Cinder(_Storage):
    _icon = "cinder.png"


class Manila(_Storage):
    _icon = "manila.png"


class Swift(_Storage):
    _icon = "swift.png"


# Aliases
