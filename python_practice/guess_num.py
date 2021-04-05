import random

computer_num: int = random.randint(1, 100)
while True:
    person_num = int(input("请输入一个数字"))
    if person_num > computer_num:
        print("大一点")
    elif person_num < computer_num:
        print("小一点")
    elif person_num == computer_num:
        print("猜对了")
        break
