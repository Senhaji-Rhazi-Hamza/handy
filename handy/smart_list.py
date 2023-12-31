import re
from types import FunctionType
from typing import List, Tuple


class SmartList(list):
    def filter_by_attribute_values(self, **kwargs):
        def check_that_all_attributes_are_equal(el, **kwargs):
            assert all(
                [v is not None for _, v in kwargs.items()]
            ), f"The key values provided can't be passed as None, kwargs passed {kwargs}"

            return all(
                [
                    ((getattr(el, k) == v) or (str(getattr(el, k)) == str(v)))
                    for k, v in kwargs.items()
                    if hasattr(el, k)
                ]
            )

        return SmartList(
            [el for el in self if check_that_all_attributes_are_equal(el, **kwargs)]
        )

    def filter_by_matched_attributes(self, **kwargs):
        new_kwargs = {
            k: (pattern if isinstance(pattern, re.Pattern) else re.compile(pattern))
            for k, pattern in kwargs.items()
        }

        def check_that_all_attributes_are_matched(el, **kwargs):
            assert all(
                [v is not None for _, v in kwargs.items()]
            ), f"The key values provided can't be passed as None, kwargs passed {kwargs}"

            return all(
                [
                    pattern.match(getattr(el, k))
                    for k, pattern in new_kwargs.items()
                    if hasattr(el, k)
                ]
            )

        return SmartList(
            [el for el in self if check_that_all_attributes_are_matched(el, **kwargs)]
        )

    def group_by_labeled_predicates(
        self, *labeled_predicates: List[Tuple[str, FunctionType]]
    ):
        assert all(
            [isinstance(el[0], str) and isinstance(el[1], FunctionType)]
            for el in labeled_predicates
        ), "all your labeled predicates should be given in form of (str, function)"
        groups = []
        for labeled_predicate in labeled_predicates:
            groups.append(
                labeled_predicate[0], self.filter_by_predicates(labeled_predicate[1])
            )
        return groups

    def filter_by_predicates(self, *predicates):
        return SmartList(
            [el for el in self if all([predicate(el) for predicate in predicates])]
        )

    def __getitem__(self, key):
        if isinstance(key, slice):
            return SmartList(super().__getitem__(key))
        else:
            return super().__getitem__(key)

    def len(self):
        return self.__len__()

    def map(self, func_map):
        return SmartList([func_map(el) for el in self])

    def first(self):
        if len(self) < 1:
            raise IndexError("The collection you're trying to extract from is empty")
        return super().__getitem__(0)

    def last(self):
        if len(self) < 1:
            raise IndexError("The collection you're trying to extract from is empty")
        return super().__getitem__(-1)

    def last_or_none(self):
        if len(self) > 0:
            return super().__getitem__(-1)

    def first_or_none(self):
        if len(self) > 0:
            return super().__getitem__(0)

    def one_or_none(self):
        if len(self) == 1:
            return self.first()

    def sort(self, key=None, reverse=False):
        return SmartList(sorted(self, key=key, reverse=reverse))
