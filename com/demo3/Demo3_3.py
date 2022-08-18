import math

# print(math.acosh(0.5))  # ValueError: math domain error
print(math.acosh(1))  # 0.0
print(math.acosh(100))  # 5.298292365610484

print(math.asinh(0))  # 0.0
print(math.asinh(6))  # 2.491779852644912

# 两端不可取
# print(math.atanh(1))  # ValueError: math domain error
print(math.atanh(0.9999999))  # 8.40562139102231

print(math.cosh(10))  # 11013.232920103323
print(math.cosh(0))  # 1.0

print(math.sinh(10))  # 11013.232874703393
print(math.sinh(-1))  # -1.1752011936438014

# 由于精度问题，大于一定值能够取到两端
print(math.tanh(1000))  # 1.0
print(math.tanh(10))  # 0.9999999958776927
