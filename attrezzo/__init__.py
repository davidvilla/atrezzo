"Test doubles for Python"

from unittest.mock import Base, Mock, MagicMock

from .internal import AttributeFactory


class Stub(MagicMock):
    def __init__(self, *args, **kargs):
        Base.__setattr__(self, '_setting_up', False)
        print("init")
        super().__init__(*args, **kargs)

    def __enter__(self):
        self._setting_up = True
        print("enter")

    def __exit__(self, *args):
        self._setting_up = False
        print("exit")
        return self

    def returns(self, value):
        self.return_value = value

    def __call__(self, *args):
        print(self.__class__, self._setting_up)
        if self._setting_up:
            return self

        return super().__call__(*args)

    #def __getattr__(self, key):
    #    if key == "_mock_methods":
    #        return None
#
    #    attr = Stub()
    #    setattr(self, key, attr)
    #    return attr

        # attr = AttributeFactory.create(self, key)
        # setattr(self, key, attr)
        # return attr

    #   AttributeFactory.create(self, key)
    #    return object.__getattribute__(self, key)
