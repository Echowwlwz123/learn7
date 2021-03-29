from Python脚本编写与实战作业.jinx import Jinx
from Python脚本编写与实战作业.ez import EZ


class leitai:
    ez = EZ()
    jinx = Jinx()

    ez.fight(jinx.hp, jinx.power)
    jinx.fight(ez.hp, ez.power)
