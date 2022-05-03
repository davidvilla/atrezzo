"Test doubles for Python"

from unittest.mock import Base, Mock, MagicMock



class MagicStub(MagicMock):
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


ANY = object()


def func_returning(value=None):
    return lambda *args, **kargs: value


def func_returning_input(invocation):
    def func(*args, **kargs):
        if not args:
            raise TypeError("%s has no input args" % invocation)

        if len(args) == 1:
            return args[0]

        return args

    return func


def func_raising(e):
    def raise_(e):
        raise e

    return lambda *args, **kargs: raise_(e)


class Stub:
    def __new__(cls, collaborator=None):
        klass = type(cls.__name__, (cls,), dict(cls.__dict__))
        return object.__new__(klass)

    def __init__(self):
        self._setting_up = False
        self._double = self
        self._delegate = func_returning(None)

    def __enter__(self):
        self._setting_up = True
        print("enter")
        return self

    def __exit__(self, *args):
        self._setting_up = False
        print("exit")

    def __getattr__(self, name):
        setattr(self.__class__, name, Stub())
        return getattr(self, name)

    def __get__(self, obj, type=None):
        self._double = obj
        return self

    def __call__(self, *args, **kwargs):
        if self._double._setting_up:
            return self

        return self._delegate(*args, **kwargs)

    def returns(self, value):
        self._delegate = func_returning(value)

    def return_args(self):
        self._delegate = func_returning_input(None)
