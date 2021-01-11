from unittest import TestCase
from hamcrest import assert_that, is_
from attrezzo import Stub


class FreeStubTests(TestCase):
    def setUp(self):
        self.stub = Stub()

    def test_basic_stub_method(self):
        with self.stub:
            self.stub.foo().returns(2)

        # print(self.stub)
        # print(self.stub.foo)
        # print(self.stub.foo())
        assert_that(self.stub.foo(), is_(2))
