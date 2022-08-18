import math

INF = math.inf

# 结果为nan
print(0 * INF)
print(INF / INF)
print(INF - INF)
print(-INF - (-INF))
print(0.1 * INF - 0.5 * INF)  # 可为任意正数
print(-0.1 * INF + 2 * INF)  # 只需一正一副

# 结果为inf或-inf
print(0.002 * INF)  # 可为任意正数 ==> inf
print(-0.01 * INF)  # 可为任意负数 ==> -inf
print(INF * INF)  # ==> inf
print(INF / 2)  # 可为任意正数 ==> inf
print(INF / -2)  # 可为任意负数 ==> -inf
# 加减任意实数也为inf，略


# 其他值
print(0 / INF)  # ==> 0.0 (float)
# print(INF / 0)  # 报错，0不能为除数
