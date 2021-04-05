"""
如果想生成一个平方列表，比如【1,4,9】，用for循环怎么做用列表推导式怎么做
"""
# for循环
list_square = []
for i in range(4):
    list_square.append(i ** 2)
print(list_square)

# 列表推导式
list_square2 = [i ** 2 for i in range(0, 4)]
print("list_square2", list_square2)
