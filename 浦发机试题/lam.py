"""
需求：给定一个只包含正整数且非空的数组，返回该数组中重复次数最多的前N个数字（返回结果按重复次数从多到少降序）
"""
a = [1, 6, 7, 4, 4, 5, 4, 5, 4, 5, 5, 6, 7, 8, 5, 6, 7, 3, 4, 2, 2, 1, 4, 8, 9, 4, 5, 6]


def get_datas(a):
    result = []
    data_dict = {}
    # 键值对：键：数字，值：在列表中的次数
    for item in set(a):
        data_dict[str(item)] = a.count(item)
    print(f"data_dict:{data_dict}")
    # 将键值对按值（数字出现的次数）排序 ---从高到低排序
    res = sorted(data_dict.values(), reverse=True)
    for num in res:
        for key, value in data_dict.items():
            # 如果值在列表中不存在，则添加到结果列表中
            if num == value and key not in result:
                result.append(key)

    return result


a1 = get_datas(a)
print(f"a1:{a1}")
