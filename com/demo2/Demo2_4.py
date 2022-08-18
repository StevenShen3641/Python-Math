from math import nan as NAN
from math import inf as INF

# 结果都为nan
print(NAN * INF)
print(NAN * 0)  # 因为nan不是一个数，所以乘0也是0
print(NAN + 1)  # 加减一样
print(0 / NAN)

# print(NAN / 0)  # 报错，0不能为除数
