import unittest


class TestStringMethods(unittest.TestCase):
    # 每个测试用例之前都会执行setup
    def setUp(self) -> None:
        print("setup")

    # 每个测试用例之后都会执行tearDown
    def tearDown(self) -> None:
        print("teardown")

    # setUpClass， tearDownClass是在整个类的前后调用的方法
    @classmethod
    def setUpClass(cls) -> None:
        print("setupclass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardownclass")

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        print("testupper")

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
        print("test_isupper")

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
        print("test_split")


if __name__ == '__main__':
    unittest.main()
