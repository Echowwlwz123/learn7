"""
一个回合制游戏，有两个英雄，分别以两个类进行定义。分别是EZ 和Jinx。
每个英雄都有 hp 属性和 power属性，hp 代表血量，power 代表攻击力
Jinx：hp 的初始值为 1000，power 的初始值为 210。
EZ：hp 的初始值为 1100，power 的初始值为 190。
每个英雄都有一个 fight 方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个 hp 进行对比，血量剩余多的人获胜
"""


class Jinx:
    hp = 1000
    power = 210

    def fight(self, enemy_hp, enemy_power):
        self.enemy_power = enemy_power

        my_final_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp - self.power

        if my_final_hp > enemy_final_hp:
            print(f"Jinx的剩余血量是{my_final_hp}，Jinx赢了")

        elif my_final_hp < enemy_final_hp:
            print(f"Jinx的剩余血量是{my_final_hp}，敌人赢了")
        else:
            print(f"Jinx的剩余血量是{my_final_hp}，双方打平手")
