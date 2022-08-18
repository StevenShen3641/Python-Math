import math

# print(math.acos(2))  # ValueError: math domain error
print(math.acos(0.5))  # 1.0471975511965979
print(math.acos(-0.5))  # 2.0943951023931957

# print(math.asin(1.5))  # ValueError: math domain error
print(math.asin(0.5))  # 0.5235987755982989
print(math.asin(-0.5))  # -0.5235987755982989

print(math.atan(100))  # 1.5607966601082315
print(math.atan(-100))  # -1.5607966601082315

print(math.atan2(1, 1))  # 0.7853981633974483
print(math.atan2(-1, 1))  # -0.7853981633974483
print(math.atan2(-1, -1))  # -2.356194490192345
print(math.atan2(1, -1))  # 2.356194490192345

print(math.cos(1))  # 0.5403023058681398

# 判断是否相等
a = math.cos(1)
b = math.cos(-1)
print(id(a))  # 2715377076368
print((id(b)))  # 2715377076336
print(a is b)  # 由于运算后地址分配不同，结果为False
print(a == b)  # 数值相等，结果为True

# 由于浮点数保留规则，pi能够得出较为标准的结果
print(math.cos(math.pi))  # -1.0

# 由于精度不够精确，比较时并不相等
print(math.cos(1 + 2 * math.pi) == math.cos(-1))

p1 = [1]
q1 = [-1]  # 一维也必须采用可迭代的形式
p2 = (1, 2, 3)
q2 = (4, 5, 6)
p3 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
q3 = (9, 8, 7, 6, 5, 4, 3, 2, 1)
# print(math.dist(1, -1))  # 不可迭代报错 TypeError: 'int' object is not iterable
# print(math.dist(p1, q2))  # ValueError: both points must have the same number of dimensions
print(math.dist(p1, q1))  # 2.0
print(math.dist(p2, q2))  # 5.196152422706632
print(math.dist(p3, q3))  # 15.491933384829668

# print(math.hypot((1, 2, 3)))  # TypeError: must be real number, not tuple
print(math.hypot(1, 2, 3))  # 3.741657386773941

print(math.sin(1))  # 0.8414709848078965
print(math.sin(100))  # -0.5063656411097588

print(math.tan(1))  # 1.5574077246549023
print(math.tan(-100))  # 0.5872139151569291
