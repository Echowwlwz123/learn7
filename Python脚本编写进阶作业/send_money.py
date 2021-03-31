from Python脚本编写进阶作业 import money


def send(salary):
  print(f"原本存款有{money.saved_money}块钱")
  money.saved_money = money.saved_money + salary
  print(f"这个月发{salary}块钱")
