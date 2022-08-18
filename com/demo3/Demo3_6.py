import math

print(math.erf(0))  # 0.0
print(math.erf(3))  # 0.9999779095030014
print(math.erf(10))  # 1.0 精度不够

print(math.erfc(2))  # 0.004677734981047266
print(math.erfc(-6))  # 2.0 精度不够
print(math.erfc(0))  # 1.0
print(math.erfc(10))  # 2.088487583762545e-45 整数位为0的数能存储更多小数位

# print(math.gamma(0))  # ValueError: math domain error
print(math.gamma(10))  # 362880.0


