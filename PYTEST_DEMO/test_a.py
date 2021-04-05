import pytest


def inc(x):
    return x + 1


# pytest解释器运行
# 参数化测试用例
@pytest.mark.parametrize('a,b', [
    (4, 5),
    (1, 20),
    ('a1', 'a2'),
    (6, 9)
])
def test_answer(a, b):
    assert inc(a) == b


def test_answer1():
    assert inc(4) == 5


@pytest.fixture()
def login():
    print("登录操作")
    username = "Jerry"
    return username


class TestDemo:

    def test_a(self, login):
        print(f"testa,username = {login}")

    def test_b(self):
        print("testb")

    def test_c(self, login):
        print(f"testc login = {login}")


# 加一个入口函数就可以用python解释器运行
if __name__ == '__main__':
    pytest.main(['test_a.py::TestDemo', '-v'])
