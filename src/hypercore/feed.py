from functools import partial

from . import native, exceptions
from .robject import RustObject


class Feed(RustObject):
    def __init__(self):
        self._native_ptr = self._native("new")
        self.__dealloc_func = self._native("free")
