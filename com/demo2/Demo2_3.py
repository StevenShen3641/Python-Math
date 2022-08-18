import math

# 浮点值nan
NAN = math.nan

print(NAN)  # ==> nan

# nan不是0
print(NAN == 0)  # ==> False

# nan和它自己或其它元素比较操作都为False
print(NAN < math.inf)  # ==> False
print(NAN > -1)  # ==> False

# 两个nan并不相等
print(NAN == NAN)  # ==> False
print(NAN == float('nan'))  # ==> False
