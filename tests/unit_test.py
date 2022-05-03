from unittest import TestCase
from attrezzo import Stub, ANY
from hamcrest import assert_that, is_


class StubTest(TestCase):
    def test_basic_method(self):
        with Stub() as stub:
            stub.foo().returns(2)

        self.assertEqual(stub.foo(), 2)
        assert_that(stub.foo(), is_(2))

    def test_func(self):
        with Stub() as stub:
            stub().returns(2)

        self.assertEqual(stub(), 2)

    def test_dynamic_method(self):
        stub = Stub()
        self.assertEqual(stub.foo(), None)

    def test_return_args(self):
        with Stub() as stub:
            stub.foo(ANY).return_args()

        self.assertEqual(stub.foo(1, 2, 3), (1, 2, 3))
