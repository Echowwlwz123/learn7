"""
 # setUpClass， tearDownClass是在整个类的前后调用的方法
"""
import unittest


class Search:

    def search_fun(self):
        print("search")
        return True


class TestSearch1(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")
        cls.search = Search()

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def test_search1(self):
        print("test_search1")
        # search = Search()
        # assert断言
        assert True == self.search.search_fun()

    def test_search2(self):
        print("test_search2")
        # search = Search()
        # assert断言
        assert True == self.search.search_fun()

    def test_search3(self):
        print("test_search3")
        # search = Search()
        # assert断言
        assert True == self.search.search_fun()

    def test_equal(self):
        print("断言相等")
        # self.assertEqual(1,1,"判断1==1")
        self.assertTrue(1 == 2, "verify")

    def test_notequal(self):
        print("断言不相等")
        self.assertNotEqual(1, 2, "判断1!=2")


class TestSearch2(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass2")
        cls.search = Search()

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass2")

    def test_search1(self):
        print("test_search12")
        # search = Search()
        # assert断言
        assert True == self.search.search_fun()

    def test_search2(self):
        print("test_search22")
        # search = Search()
        # assert断言
        assert True == self.search.search_fun()

    def test_search3(self):
        print("test_search32")
        # search = Search()
        # assert断言
        assert True == self.search.search_fun()

    def test_equal(self):
        print("断言相等2")
        # self.assertEqual(1,1,"判断1==1")
        self.assertTrue(1 == 2, "verify")

    def test_notequal(self):
        print("断言不相等2")
        self.assertNotEqual(1, 2, "判断1!=2")


class TestSearch3(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass3")
        cls.search = Search()

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass3")

    def test_search1(self):
        print("test_search123")
        # search = Search()
        # assert断言
        assert True == self.search.search_fun()

    def test_search2(self):
        print("test_search223")
        # search = Search()
        # assert断言
        assert True == self.search.search_fun()

    def test_search3(self):
        print("test_search323")
        # search = Search()
        # assert断言
        assert True == self.search.search_fun()

    def test_equal(self):
        print("断言相等23")
        # self.assertEqual(1,1,"判断1==1")
        self.assertTrue(1 == 2, "verify")

    def test_notequal(self):
        print("断言不相等23")
        self.assertNotEqual(1, 2, "判断1!=2")


if __name__ == '__main__':
    # 方法1：执行当前文件所有的unittest测试用例
    # unittest.main()
    # 方法二：执行指定的测试用例，将要执行的测试用例添加到测试套件里，批量执行测试方法
    # 创建一个测试套件，testsuite
    # suite = unittest.TestSuite()
    # suite.addTest(TestSearch1("test_search1"))
    # suite.addTest(TestSearch1("test_search2"))
    # unittest.TextTestRunner().run(suite)

    # 方法三：执行某个测试类,将某个测试类加入测试套件中，批量执行测试类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestSearch1)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestSearch2)
    suite = unittest.TestSuite([suite1, suite2])
    unittest.TextTestRunner(verbosity=2).run(suite)
