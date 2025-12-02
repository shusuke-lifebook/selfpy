import math


# 素数を求めるジェネレーター
def get_primes():
    num = 2
    # 2から順に素数を判定し、素数の場合にだけyield(無限ループ)
    while True:
        if is_prime(num):
            yield num
        num += 1


# 引数valueが素数であるか判定する関数
def is_prime(value):
    result = True
    for i in range(2, math.floor(math.sqrt(value)) + 1):
        if value % i == 0:
            result = False
            break
    return result


# 素数を順に出力
for prime in get_primes():
    print(prime)
    if prime >= 100:
        break
