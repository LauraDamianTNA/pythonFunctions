from distutils.command.build import build
from lib_hello import build_hello
import pytest


def test_build_hello():
    assert build_hello("world") == "Hello, world!"
