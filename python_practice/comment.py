# a, b = 0, 1
# while a < 100:
#     print(a, end=',')
#     a, b = b, a + b
# 函数累积了在随后的呼叫中传递给它的参数
def f(a, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))


# 如果您不希望后续呼叫之间共享默认值
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))
