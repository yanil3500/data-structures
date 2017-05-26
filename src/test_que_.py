"""Test que.py"""

import pytest


@pytest.fixture
def empty_que():
    from que_ import Queue
    return Queue()

def test_init(empty_que):
    assert empty_que._length == 0 and empty_que._front is None and empty_que._rear is None

