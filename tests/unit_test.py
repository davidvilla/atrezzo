from unittest import TestCase
from attrezzo import DStub
from hamcrest import assert_that, is_


class StubTest(TestCase):
    def test_basic_stub_method(self):
        with DStub() as stub:
            stub.foo().returns(2)

        self.assertEqual(stub.foo(), 2)
        assert_that(stub.foo(), is_(2))
