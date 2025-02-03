import pytest
from handyobj import SmartList


@pytest.fixture
def simple_smart_list():
    return SmartList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
