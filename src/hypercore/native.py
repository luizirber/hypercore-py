import os

from . import exceptions
from ._native import ffi, lib


def string_rv(c_str):
    try:
        return ffi.string(c_str).decode("utf-8")
    finally:
        lib.hypercore_free_str(c_str)
