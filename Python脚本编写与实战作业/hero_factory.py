from ez import EZ
from jinx import Jinx
from police import Police
from timo import Timo


class HeroFactory:
    """
    简单工厂模式专门定义一个类来负责创建其他类型的英雄的实例
    """

    def creat_hero(self, name):
        if name == "EZ":
            return EZ()
        elif name == "Jinx":
            return Jinx()
        elif name == "Timo":
            return Timo()
        elif name == "Police":
            return Police()
        else:
            raise Exception("此英雄不在英雄工厂中")


hero_factory = HeroFactory()
jinx = HeroFactory.creat_hero("Jinx")
ez = HeroFactory.creat_hero("EZ")
timo = HeroFactory.creat_hero("Timo")
police = HeroFactory.creat_hero("Police")
