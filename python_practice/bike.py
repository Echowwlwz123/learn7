"""
需求文档：
写一个Bicycle(自行车)类,有run(骑行)方法, 调用时显示骑行里程km(骑行里程为传入的数字):再写一个电动自行车类EBicycle继承自Bicycle,添加电池电量valume属性通过，参数传入, 同时有两个方法：
1）fill_charge(vol) 用来充电, vol 为电量
2）run(km) 方法用于骑行,每骑行10km消耗电量1度,当电量消耗尽时调用Bicycle的run方法骑行，通过传入的骑行里程数，显示骑行结果
"""


class bycycle:
    def __init__(self, a):
        print(a)

    # self 代表普通函数和类方法的区别。
    def run(self, miles):
        """
        调用时显示骑行里程km:
        :param miles:骑行里程，要求为数字类型
        :return:
        """
        print(f"用脚踩了{miles}公里，好累的")


class EBicycle(bycycle):
    def __init__(self, valume):
        """
        # 构造函数,在类实例化的时候传入的参数
        # 类变量、普通、 实例变量、
        # valume = 0 类变量，整个类内
        :param valume:电池量
        """
        self.valume = valume

    def fill_charge(self, vol):
        """
        :param vol: 充电变量
        :return:
        """
        # 如果传入的数据是int类型、
        if isinstance(vol, int):
            self.vol = self.valume + vol

    def run(self, miles):
        """
        run(km) 方法用于骑行,
        每骑行10km消耗电量1度,
        当电量消耗尽时调用Bicycle的run方法骑行，
        通过传入的骑行里程数，
        显示骑行结果
        :param miles:
        :return:
        """
        # 先计算电量能够支撑的公里数,每骑行10km消耗电量1度,
        ele_miles = self.valume * 10

        # 再计算剩余公里数
        # 传入的公里数减去电量支持的公里数。
        # 计算电量公里数和传入公里数的差值
        res_miles = miles - ele_miles

        # 当电量支撑的公里数<=0 时， 代表电量未耗尽
        if res_miles <= 0:
            print(f"使用电瓶车骑行{ele_miles}公里")
        else:
            print(f"使用电动车骑行的公里数位{ele_miles}")
            # , 当电量消耗尽时调用Bicycle的run方法骑行，
            # 通过传入的骑行里程数，显示骑行结果
            # Bike().run
            # 如果子类重写了父类，那么又需要去调用父类的属性，可以使用
            # super() ， super() == Bicycle()
            # 调用父类的构造函数
            super().run(res_miles)


# 电量类实例化的时候传入的
ebike = EBicycle(20)
ebike.run(1000)
