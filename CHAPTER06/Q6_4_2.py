import math


def gen_prime(x=2):
    # 素数を返すジェネレーター関数（２）sprt(x)以下だけ調べる方法
    while True:
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                break
        else:
            yield x
        x += 1


# 実行例
i = gen_prime()
for c in range(10):
    print(next(i), end="")
print("")
