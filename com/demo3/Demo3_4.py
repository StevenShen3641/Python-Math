import math

print(math.ceil(1.2))  # 2
print(math.ceil(-1.2))  # -1
print(math.ceil(-0.5))  # 0
print(math.ceil(0.5))  # 1
print(type(math.ceil(0.5)))  # <class 'int'>

print(math.comb(7, 5))  # 21
# 输入必须为整型
# print(math.comb(7.0, 5.0))  # TypeError: 'float' object cannot be interpreted as an integer
# 输入不能为负数
# print(math.comb(-7, 5))  # ValueError: n must be a non-negative integer
# print(math.comb(7, -5))  # ValueError: k must be a non-negative integer

# 无需k <= n
print(math.comb(5, 7))  # 0

# 可为0
print(math.comb(7, 0))  # 1
print(math.comb(0, 7))  # 0
print(math.comb(0, 0))  # 1

print(math.copysign(4, -7))  # -4.0（浮点数）

# x为0
print(math.copysign(0, -1))  # -0.0
print(math.copysign(0, 4))  # 0.0
# y为0或-0
print(math.copysign(4, 0))  # 4.0
print(math.copysign(4, -0))  # 依旧为4.0
print(math.copysign(4, -0.0))  # -4.0
print(math.copysign(0, -0))  # 0.0
print(math.copysign(0, -0.0))  # -0.0

print(math.fabs(-4))  # 4.0（浮点数）

print(math.factorial(0))  # 1
print(math.factorial(6))  # 720
print(math.factorial(2.0))  # 2 不报错，但警告 DeprecationWarning: Using factorial() with floats is deprecated
# print(math.factorial(2.2))  # ValueError: factorial() only accepts integral values
# print(math.factorial(-1))  # ValueError: factorial() not defined for negative values

print(math.floor(2.3))  # 2
print(math.floor(-2.4))  # -3
print(math.floor(0.2))  # 0
print(math.floor(-0.3))  # -1

print(math.fmod(5.9, 1.2))  # 1.1000000000000005
print(math.fmod(2, 3))  # 2.0（浮点数）
print(math.fmod(0, 3))  # 0.0
# print(math.fmod(0, 0))  # ValueError: math domain error
# print(math.fmod(4, 0))  # ValueError: math domain error
print(math.fmod(math.inf, math.nan))  # nan
# print(math.fmod(math.inf, 7))  # 报错

# 负数
print(math.fmod(5, -3))  # 2.0 (5 = (-1) * (-3) + 2)
print(5 % -3)  # -1 (5 = (-2) * (-3) - 1)
print(math.fmod(-1, 2))  # -1
print(-1 % 2)  # 1
print(math.fmod(-6, -2.5))  # -1.0
print(-6 % -2.5)  # -1.0

# 比较%和fmod
print(-1e-100 % 1e100)  # 1e+100 省略浮点部分
print(math.fmod(-1e-100, 1e100))  # -1e-100 更精确

print(math.frexp(35))  # (0.546875, 6)
print(math.frexp(0))  # (0.0, 0)
print(math.frexp(-32.9))  # (-0.5140625, 6)

print(math.fsum([0.1, 0.2, 0.3, 0.4, 0.5]))  # 1.5
print(sum([0.1, 0.2, 0.3, 0.4, 0.5]))  # 1.5
print(math.fsum((0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)))  # 1.0
print(sum((0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)))  # 0.9999999999999999
print(math.fsum([]))  # 0.0

# print(math.gcd(1.1))  # TypeError: 'float' object cannot be interpreted as an integer
# print(math.gcd((264, 18, 688)))  # TypeError: 'tuple' object cannot be interpreted as an integer
print(math.gcd(264, 18, 688))  # 2
# 有0时
print(math.gcd(0, 0, 16, 4, 8))  # 4 不全为0时，返回除去0的最大公约数
print(math.gcd(0))  # 0
print(math.gcd(0, 0, 0))  # 0 全为0时，返回0
# 有负数时
print(math.gcd(-4, -8, -16))  # 4
print(math.gcd(4, 8, -16))  # 4
# 无参数时
print(math.gcd())  # 0

# print(math.isclose(8.005, 8.450, 0.000009, 0.4))  # 报错，后两个参数赋值时需注明参数名称
print(math.isclose(8.005, 8.450, rel_tol=0.000009, abs_tol=0.4))  # False
print(math.isclose(8.005, 8.450, rel_tol=0.000009, abs_tol=0.5))  # True
# print(math.isclose(8.005, 8.450, rel_tol=-0.000009, abs_tol=0.4))   # ValueError: tolerances must be non-negative
# print(math.isclose(8.005, 8.450, rel_tol=0.000009, abs_tol=-0.5))   # ValueError: tolerances must be non-negative
print(math.isclose(8.005, 8.450, rel_tol=0, abs_tol=0.5))  # True 相对容差可以为0

# 当==不再精确时，可用于浮点数判断
print(0.1 + 0.2 == 0.3)  # False
print(0.1 + 0.2)  # 0.30000000000000004
print(math.isclose(0.1 + 0.2, 0.3))  # True

print(math.isfinite(8))  # True
print(math.isfinite(math.inf))  # False
print(math.isfinite(math.nan))  # False

print(math.isinf(math.nan))  # False
print(math.isinf(-math.inf))  # True
print(math.isinf(float('inf')))  # True

print(math.isnan(math.inf))  # False
print(math.isnan(math.nan))  # True
print(math.isnan(float('nan')))  # True

# print(math.isqrt(-1))  # ValueError: isqrt() argument must be nonnegative
# print(math.isqrt(2.5)) # TypeError: 'float' object cannot be interpreted as an integer
print(math.isqrt(0))  # 0
print(math.isqrt(3))  # 1

# 无参数时
print(math.lcm())  # 1
print(math.lcm(0, 1, 2))  # 0
print(math.lcm(1, 2, 4, 5, 7))  # 140
print(math.lcm(-2, -3, -5))  # 30

# print(math.ldexp(2, 5.0))  # TypeError: Expected an int as second argument to ldexp.
print(math.ldexp(1.9, 25))  # 63753420.8
print(math.ldexp(-1, -1))  # -0.5
print(math.ldexp(0, 0))  # 0.0

print(math.modf(-1.8))  # (-0.8, -1.0)
print(type(math.modf(-1.89)))  # <class 'tuple'>

print(math.nextafter(1, 1.2))  # 1.0000000000000002
print(math.nextafter(1.0000000000000002, math.inf))  # 1.0000000000000004
# y为nan时，结果都为nan
print(math.nextafter(0, math.nan))  # nan
print(math.nextafter(-math.inf, 0))  # -1.7976931348623157e+308
print(math.nextafter(math.inf, 0))  # 1.7976931348623157e+308
# x和y相等返回y
print(math.nextafter(1, 1))  # 1.0
print(math.nextafter(math.inf, math.inf))  # inf

print(math.perm(5, 4))  # 1
print(math.perm(5))  # 120
print(math.perm(1, 2))  # 0
print(math.perm(7, 0))  # 1
print(math.perm(0, 7))  # 0
print(math.perm(0, 0))  # 1

print(math.prod([1.0, 2, 3, 4]))  # 24.0
print(math.prod([1, 2, 3, 4]))  # 24
print(math.prod([]))  # 1
# print(math.prod([], 2))  # 报错，需要注明参数名称
print(math.prod([], start=2))  # 2
print(math.prod([1, 2, 3, 4], start=2.5))  # 60.0

print(math.remainder(7, 4))  # -1.0
print(math.remainder(math.inf, math.nan))  # nan
# print(math.remainder(math.inf, 7))  # ValueError: math domain error
print(math.remainder(-5, -6))  # 1.0

print(math.trunc(5))  # 5
print(math.trunc(0.8))  # 0
print(math.trunc(-0.9))  # 0
print(math.trunc(9.8))  # 9
print(math.trunc(-9.8))  # -9

print(math.ulp(math.nan))  # nan
print(math.ulp(-math.inf))  # inf
print(math.ulp(-1))  # 2.220446049250313e-16
print(math.ulp(1))  # 2.220446049250313e-16
print(math.ulp(0.0))  # 5e-324

# 和math.nextafter()比较
print(math.ulp(10))  # 1.7763568394002505e-15
print(math.nextafter(10, 11))  # 10.000000000000002
# 末尾的2即为math.ulp()的值
