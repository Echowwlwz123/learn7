from Python脚本编写与实战作业.jinx import Jinx
from Python脚本编写与实战作业.ez import EZ
from police import Police
from timo import Timo


class Leitai:
    ez = EZ()
    jinx = Jinx()
    timo = Timo()
    police = Police()
    ez.speak_lines("我是EZ，我就是打败天下无敌手")
    jinx.speak_lines("Jinx来也")
    ez.fight(jinx.hp, jinx.power)
    jinx.fight(ez.hp, ez.power)

    timo.speak_lines("提莫队长正在待命")
    police.speak_lines("见识一下法律的子弹")
