from functools import partial

from . import native, exceptions


class RustObject(object):
    _native_ptr = None

    def __init__(self):
        raise TypeError("Cannot instantiate %r objects" % self.__class__.__name__)

    @classmethod
    def _from_objptr(cls, ptr, shared=False):
        rv = object.__new__(cls)
        rv._native_ptr = ptr
        rv._shared = shared
        return rv

    def _native(self, name):
        return partial(
            getattr(
                native.lib,
                "hypercore_{}_{}".format(self.__class__.__name__.lower(), name)),
            self._native_ptr,
        )
