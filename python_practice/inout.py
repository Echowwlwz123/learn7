name = 'lili'
age = 20
list1 = [1, 2, 3]
dict1 = {'name': 'tom', 'gender': 'male'}
print('my list is {0},dic is {1}'.format(list1, dict1))
print('my name is {1} ,my age is {0} ,{0}{1}'.format(name, age))

namelist = ['lili', 'tom', 'jerry']
print('our name:{}，{}，{}'.format(*namelist))

print('my name is {name},gender is {gender}'.format(**dict1))

print(f"my name is {name},my list is {list1[0]},my dirc is {dict1['name']}")
print(f"my name is {name.upper()}")

print(f"the result is {(lambda x: x + 1)(3)}")
