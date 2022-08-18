import math

print(math.degrees(10))  # 572.9577951308232
print(math.degrees(-1))  # -57.29577951308232

print(math.radians(-1000))  # -17.453292519943297

# 由于浮点数保留规则，该比较结果为True
print(math.radians(180) == math.pi)  # True
