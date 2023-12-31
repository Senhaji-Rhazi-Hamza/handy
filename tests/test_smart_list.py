from handy import SmartList


def test_first(simple_smart_list):
    assert simple_smart_list.first() == 1


def test_last(simple_smart_list):
    assert simple_smart_list.last() == 10


def test_len(simple_smart_list):
    assert simple_smart_list.len() == 10


def test_filter_odd(simple_smart_list):
    def is_odd_prdicate(el):
        return el % 2 == 0

    assert simple_smart_list.filter_by_predicates(is_odd_prdicate) == [
        2,
        4,
        6,
        8,
        10,
    ]
