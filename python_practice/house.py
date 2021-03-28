# 通过class定义一个类
class House:
    # 类的静态属性
    door = ""
    floor = ""

    # 类的方法
    def cook(self):
        print("我在厨房做炸鸡")

    def sleep(self):
        print("我在卧室睡觉")


# 实例对象
bob_house = House()
bob_house.door = "white"
bob_house.floor = "black"
print(bob_house)
# 可以用debug的方式，查看实例的属性内容
# 定义多个实例对象
# 修改当前实例的属性不会影响其他实例
mary_house = House()
print(mary_house)
