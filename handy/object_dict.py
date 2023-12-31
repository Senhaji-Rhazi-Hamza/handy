import copy


class ObjectDict(dict):
    """Dynamic Class as dict"""

    def __getattr__(self, name):
        if name in self:
            value = self[name]
            if isinstance(value, dict):
                return ObjectDict(value)
            if isinstance(value, list):
                try:
                    return [ObjectDict(element) for element in value]
                except ValueError:
                    pass
            return value
        if not isinstance(getattr(type(self), name), property):
            raise Exception("No such attribute: " + name)

    def __setattr__(self, __name: str, __value) -> None:
        if callable(__value):
            super().__setattr__(__name, __value)
        elif isinstance(__value, dict):
            self[__name] = ObjectDict(__value)
        elif isinstance(__value, list):
            type_wrapper = type(__value)
            self[__name] = type_wrapper([ObjectDict(element) for element in __value])
        else:
            self[__name] = __value

    def clone(self):
        return self.__class__((copy.deepcopy(self)))

    def drop_keys(self, keys):
        for key in keys:
            self.pop(key, None)

    def keep_only_keys(self, keys):
        for key in list(self.keys()):
            if key not in keys:
                self.pop(key, None)
        return self
