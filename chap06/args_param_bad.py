def total_produt(*values):
    if len(values) == 0:
        raise TypeError("引数は1個以上指定してください。")
    result = 1
    for value in values:
        result *= value
    return result


print(total_produt())
