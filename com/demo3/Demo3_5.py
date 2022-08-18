import math

print(math.exp(3.9))  # 49.40244910553017
print(math.exp(-1.1))  # 0.33287108369807955

print(math.expm1(3.9))  # 48.40244910553017
print(math.expm1(-1.1))  # -0.6671289163019205

# print(math.log(1, -1))  # ValueError: math domain error
# print(math.log(-1, 1))  # ValueError: math domain error
# print(math.log(0))  # ValueError: math domain error
# print(math.log(9, 0))  # ValueError: math domain error
# print(math.log(1, 1))  # ZeroDivisionError: float division by zero
print(math.log(5))  # 1.6094379124341003

# print(math.log1p(-1))  # ValueError: math domain error
print(math.log1p(0))  # 0.0
print(math.log1p(1))  # 0.6931471805599453

print(math.log2(3))  # 1.584962500721156

# print(math.pow(-1, 1.2))  # ValueError: math domain error
print(math.pow(-1, -2.0))  # 1.0
print(math.pow(2, 8))  # 256.0
print(math.pow(4, -2.2))  # 0.04736614270344993

print(math.sqrt(2))  # 1.4142135623730951

