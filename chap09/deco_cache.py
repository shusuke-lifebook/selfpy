import random
from functools import lru_cache


# 0から100の乱数を取得
@lru_cache(maxsize=5)
def get_0_to_100():
    return random.randint(0, 100)


print(get_0_to_100())
print(get_0_to_100())
