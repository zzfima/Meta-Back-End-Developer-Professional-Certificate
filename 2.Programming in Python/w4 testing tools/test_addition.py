import addition
import pytest


def test_add():
    assert addition.add(5, 6) == 11


def test_sub():
    assert addition.sub(5, 4) == 1
