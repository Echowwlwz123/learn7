"""
创建一个人类
"""


class person:
    name = 'default'
    age = 12
    gender = 'male'
    weight = 0

    def __init__(self, name, age, gender, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight
        print("init section")

    def eat(self):
        print(f"{self.name} eating")

    def jump(self):
        print(f"{self.name} jumping")

    def sleep(self):
        print(f"{self.name} sleeping")


zs = person('zhangsan', 20, 'female', 120)
print(f"zhangsan 的名字是：{zs.name},zhangsan 的年龄是{zs.age},zhangsna 的性别是{zs.gender},zhangsand的体重是{zs.weight}")
zs.eat();
ls = person('lisi', 25, 'male', 110)
print(f"lisi 的名字是：{zs.name},lisi 的年龄是{zs.age},lisi 的性别是{zs.gender},lisi 的体重是{zs.weight}")
ls.jump()
