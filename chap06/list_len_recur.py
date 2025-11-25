# 入れ子のリストの要素をカウント
def recursive_len(data):
    result = 0
    if isinstance(data, list):
        for elem in data:
            result += recursive_len(elem)
    else:
        result = 1
    return result


data = [[15, 87, [1, 3, 5, 7]], 58, [2, 4, 6, 8, 10]]

print(recursive_len(data))
