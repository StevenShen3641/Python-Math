*注：由于math模块多为浮点数运算，且由于底层规则会被分配到不同地址所以尽量避免比较和is运算等要求精度的操作*

# Python math 模块

Python math模块提供了许多对于浮点数的数学运算函数

该模块下的函数，返回值均为浮点数，除非另有说明

math模块对实数范围内的数进行运算，如需计算复数，则跟换导入cmath模块，使用其中的同名函数，cmath模块和math模块的函数基本一致

## 1 导包，查看内容

导包

```python
import math
```

查看math模块中的内容

```python
import math

print(dir(math))

```

==>
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

## 2 math 模块常量

| 常量     | 描述                          |
| -------- | ----------------------------- |
| math.e   | 欧拉数（2.718...）            |
| math.inf | 正无穷大【浮点数】            |
| math.nan | 【浮点值】NaN（not a number） |
| math.pi  | 圆周率                        |
| math.tau | 圆周常数，大小为2pi           |

### 2.1 e 和 inf

e为欧拉数（2.718...）

math.inf为正无穷大浮点数

当涉及 > 和 < 比较时，所有数都比-math.inf大，所有数都比math.inf小。

math.inf和float('inf')等价，-math.inf和float('-inf')等价

```python
import math

# 欧拉数e
print(math.e)  # 2.718281828459045

# 正无穷大
print(math.inf)  # ==> inf

# 负无穷大
print(-math.inf)  # ==> -inf

# math.inf等价于float('inf')
print(math.inf == float('inf'))  # ==> True

```

特别地，math.inf有一些特殊性质的运算

```python
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

```

注意：math.inf可以参加下述需要传入浮点数参数的运算，按要求正常得出结果，以下不给出具体结果

### 2.2 nan

math.nan返回一个浮点值nan，表示这个值不是一个合法数字，同样也相当于float('nan')的输出，但其type仍然是float

math.nan等价于float('nan')

但是所有的比较操作返回都为False。特别地，两个math.nan并不相等

```python
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

```

同样，因为nan不是一个数，所以相关计算都无法得到数字。
所有涉及nan的操作，返回的都是nan。

```python
from math import nan as NAN
from math import inf as INF

# 结果都为nan
print(NAN * INF)
print(NAN * 0)  # 因为nan不是一个数，所以乘0也是0
print(NAN + 1)  # 加减一样
print(0 / NAN)

# print(NAN / 0)  # 报错，0不能为除数

```

注意：math.nan也可以参加下述需要传入浮点数参数的运算，按要求正常得出结果，以下不给出具体结果

### 2.3 pi 和 tau

```python
import math

# 圆周率和圆周常数
print(math.pi)  # 3.141592653589793
print(math.tau)  # 6.283185307179586

```

### 2.4 常量的类型

这些常量的类型都为float，包括nan和inf

```python
import math

# 类型都为float
print(type(math.nan))
print(type(math.inf))
print(type(math.e))
print(type(math.pi))
print(type(math.tau))
# ==> <class 'float'>

```

## 3 math 模块方法

涉及角的都采用弧度制，可以用math.radians()方法将角度转化为弧度

### 3.1 三角函数

#### 1 math.acos(x)

返回x的反余弦值

x：[-1, 1]之间实数，超出定义域报错

return：一个浮点数，表示x的反余弦值（弧度制），值域为[0, pi]

```python
import math

# print(math.acos(2))  # ValueError: math domain error
print(math.acos(0.5))  # 1.0471975511965979
print(math.acos(-0.5))  # 2.0943951023931957

```

#### 2 math.asin(x)

返回x的反正弦值

x：[-1, 1]之间实数，超出定义域报错

return：一个浮点数，表示x的反正弦值（弧度制），值域为[-pi / 2, pi / 2]

```python
# print(math.asin(1.5))  # ValueError: math domain error
print(math.asin(0.5))  # 0.5235987755982989
print(math.asin(-0.5))  # -0.5235987755982989

```

#### 3 math.atan(x)

返回x的反正切值

x：实数

return：一个浮点数，表示x的反正切值（弧度制），值域为[-pi / 2, pi / 2]

```python
print(math.atan(100))  # 1.5607966601082315
print(math.atan(-100))  # -1.5607966601082315

```

#### 4 math.atan2(y, x)

返回给定坐标(x, y)（但是输入值为(y, x)）所得的y / x的反正切值

x, y：实数

return：返回一个浮点数，表示y / x的反正切值（弧度制），值域[-pi, pi]（因为包含了坐标的象限，所以范围是360°）

```python
print(math.atan2(1, 1))  # 0.7853981633974483
print(math.atan2(-1, 1))  # -0.7853981633974483
print(math.atan2(-1, -1))  # -2.356194490192345
print(math.atan2(1, -1))  # 2.356194490192345

```

#### 5 math.cos(x)

返回x的余弦值

x：实数，为弧度制

return：返回一个浮点数，表示x的余弦值，值域为[-1, 1]

注意：

​	1、math.pi精度是有误差的， 等等于结果可能为False（见注）

​	2、减少数据之间的比较运算（见注）

```python
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

```

#### 6 math.dist(p, q)

返回两个点之间的欧几里得距离（长度）

p, q：两个【可迭代】点坐标，坐标值为实数（可为list或tuple，不可迭代int报错）。维数必须相同，否则报错

return：浮点型非负实数

```python
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

```

大致等价于：

​	sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))

​	其中，list(zip((a, b), (c, d))) = [(a, c), (b, d)]，zip(可迭代对象)将每个可迭代对象下标相同的组合在一起，返回一个zip object

#### 7 math.hypot(x1, x2, ..., xn)

返回欧几里得范数，即点到原点之间的欧几里得距离

x1, 2, ..., xn：各个方位的点坐标值（为多个int，而不是一个可迭代数组，否则报错）

return：浮点型非负实数

```python
# print(math.hypot((1, 2, 3)))  # TypeError: must be real number, not tuple
print(math.hypot(1, 2, 3))  # 3.741657386773941

```

#### 8 math.sin(x)

返回x的正弦值

x：实数，为弧度制

return：返回一个浮点数，表示x的正弦值，值域为[-1, 1]

```python
print(math.sin(1))  # 0.8414709848078965
print(math.sin(100))  # -0.5063656411097588

```

#### 9 math.tan(x)

返回x的正切值

x：实数，为弧度制

return：返回一个浮点数，表示x的正弦值，值域为全体实数

```python
print(math.tan(1))  # 1.5574077246549023
print(math.tan(-100))  # 0.5872139151569291

```

### 3.2 角的换算

#### 1 math.degrees(x)

返回弧度x的角度值

x：实数，为弧度制

return：返回一个浮点数，表示弧度x的角度值

```python
import math

print(math.degrees(10))  # 572.9577951308232
print(math.degrees(-1))  # -57.29577951308232

```

#### 2 math.radians(x)

返回角度x的弧度值

x：实数，为角度制

return：返回一个浮点数，表示角度x的弧度值

```python
print(math.radians(-1000))  # -17.453292519943297

# 由于浮点数保留规则，该比较结果为True
print(math.radians(180) == math.pi)  # True

```

### 3.3 双曲函数

#### 1 math.acosh(x)

返回x的反双曲余弦值

x：[1, ∞]，超出定义域报错

return：返回一个浮点数，表示x的反双曲余弦值，值域为[0, ∞]

```python
import math

# print(math.acosh(0.5))  # ValueError: math domain error
print(math.acosh(1))  # 0.0
print(math.acosh(100))  # 5.298292365610484

```

#### 2 math.asinh(x)

返回x的反双曲正弦值

x：实数

return：返回一个浮点数，表示x的反双曲正弦值，值域为全体实数

```python
print(math.asinh(0))  # 0.0
print(math.asinh(6))  # 2.491779852644912

```

#### 3 math.atanh(x)

返回x的反双曲正切值

x：(-1, 1)，超出定义域报错

return：返回一个浮点数，表示x的反双曲正切值，值域为全体实数

```python
# 两端不可取
# print(math.atanh(1))  # ValueError: math domain error
print(math.atanh(0.9999999))  # 8.40562139102231

```

#### 4 math.cosh(x)

返回x的双曲余弦值

x：实数

return：返回一个浮点数，表示x的双曲余弦值，值域为[1, ∞]

```python
print(math.cosh(10))  # 11013.232920103323
print(math.cosh(0))  # 1.0

```

#### 5 math.sinh(x)

返回x的双曲正弦值

x：实数

return：返回一个浮点数，表示x的双曲正弦值，值域为全体实数

```python
print(math.sinh(10))  # 11013.232874703393
print(math.sinh(-1))  # -1.1752011936438014

```

#### 6 math.tanh(x)

返回x的双曲正切值

x：实数

return：返回一个浮点数，表示x的双曲正切值，值域为(-1, 1)（由于精度问题，大于一定值能够取到两端）

```python
# 由于精度问题，大于一定值能够取到两端
print(math.tanh(1000))  # 1.0
print(math.tanh(10))  # 0.9999999958776927

```

### 3.4 数论和表示函数

#### 1 math.ceil(x)

将 x 向上舍入到最接近的整数（大于等于x的最小整数）

x：实数

return：返回一个int整型（不是浮点数），表示舍入的数字

```python
import math

print(math.ceil(1.2))  # 2
print(math.ceil(-1.2))  # -1
print(math.ceil(-0.5))  # 0
print(math.ceil(0.5))  # 1
print(type(math.ceil(0.5)))  # <class 'int'>

```

#### 2 math.comb(n, k)

返回$C^{k}_{n}$

n, k：必须为非负int整型，否则报错

return：返回一个int整型，代表组合的总数

注意以下几种特殊情况：

​	1、无需k <= n，k > n时结果为0

​			math.comb(5, 7) ==> 0

​	2、math.comb(7, 0) ==> 1

​	3、math.comb(0, 7) ==> 0

​	4、math.comb(0, 0) ==> 1

```python
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

```

#### 3 math.copysign(x, y)

返回一个$\frac{y}{|y|}\times|x|$（y非零时，为零时另外考虑），即基于x的绝对值和y的符号的浮点数

x, y：实数

return：返回一个浮点数（不管x是不是整型），由第一个参数的值和第二个参数的符号组成

注意：

​	1、y为0或0.0时，本身带正号，-0.0带负号，而-0依旧是【正号】

​	2、x为0时，y符号为负，输出-0.0，y符号为正，输出0.0

```python
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

```

#### 4 math.fabs(x)

返回x的绝对值

与内置abs()方法不同，此方法始终会返回一个浮点数

x：实数

return：返回一个【浮点数】

```python
print(math.fabs(-4))  # 4.0（浮点数）

```

#### 5 math.factorial(x)

返回x的阶乘

x：必须为非负int整型（0也可以）或值为整数的非负浮点数（会报警告，不推荐），否则报错

return：返回一个正int整型，表示正整数的阶乘

```python
print(math.factorial(0))  # 1
print(math.factorial(6))  # 720
print(math.factorial(2.0))  # 2 不报错，但警告 DeprecationWarning: Using factorial() with floats is deprecated
# print(math.factorial(2.2))  # ValueError: factorial() only accepts integral values
# print(math.factorial(-1))  # ValueError: factorial() not defined for negative values

```

#### 6 math.floor(x)

将 x 向下舍入到最接近的整数（小于等于x的最大整数）

x：实数

return：返回一个int整型（不是浮点数），表示舍入的数字

```python
print(math.floor(2.3))  # 2
print(math.floor(-2.4))  # -3
print(math.floor(0.2))  # 0
print(math.floor(-0.3))  # -1

```

#### 7 math.fmod(x, y)

返回x / y的余数

x：实数

y：非零实数

return：返回一个浮点值（即使余数为整数），表示x / y的余数

注意：

​	y不等于nan时，x不能等于±inf，y等于nan时，返回nan

​	该方法和%不同

​	1、除数和被除数为整型时，%返回整型数据，而fmod返回浮点数

​	2、%余数的符号和y相同，而fmod余数的符号则和x相同

​	3、由于上述特性，%计算浮点数余数（特别是一负一正且较小的数除以较大的数）时可能会保留更大的整数从而省略浮点部分，而fmod则不会，因此%适用于整型，fmod适用于浮点型

```python
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

```

#### 8 math.frexp(x)

返回(m, e)，其中，x == m * (2 ** e)

x：实数

return：一个元组(m, e)，m是尾数为浮点型，e是指数为整型，使得x == m * (2 ** e)，且满足

​	1、x = 0时，返回(0.0, 0)

​	2、x非零时，满足0.5 <= abs(m) < 1，此时计算得e唯一，因此m也唯一

```python
print(math.frexp(35))  # (0.546875, 6)
print(math.frexp(0))  # (0.0, 0)
print(math.frexp(-32.9))  # (-0.5140625, 6)

```

#### 9 math.fsum(x)

返回可迭代数组x内所有元素的和

x：可迭代数组x，x内各个元素都为实数

return：返回一个浮点值，表示可迭代对象中所有元素的总和

注意：由于算法不同，很多情况下该方法精度比内置函数sum要高

```python
print(math.fsum([0.1, 0.2, 0.3, 0.4, 0.5]))  # 1.5
print(sum([0.1, 0.2, 0.3, 0.4, 0.5]))  # 1.5
print(math.fsum((0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)))  # 1.0
print(sum((0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)))  # 0.9999999999999999
print(math.fsum([]))  # 0.0

```

#### 10 math.gcd(*x1, x2, ..., xn*)

返回给定的整数参数的最大公约数

*x1, x2, ..., xn（非必需参数）*：都为int整型（而不是一个可迭代数组），否则报错

return：返回一个int整型，表示两个或多个整数的最大公约数，当括号内无参数时，返回0

注意：

​	1、输入整型可以为负数，负数的公因数只比正数多了其公因数的相反数，所以计算时相当于计算这些整数绝对值的最大公因数

​	2、有0存在时：

​			不全为0时，返回【除去0】的最大公约数

​			全为0时，返回0

​	3、无参数时，返回0

```python
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

```

#### 11 math.isclose(a, b, *, *rel_tol, abs_tol*)

##### *注：\*后的参数一定要按照key=value的形式进行传参，此时按位置顺序传参无效*

用于检查两个值是否彼此接近，如果值接近，则返回True，否则返回False

计算公式：abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

a, b：两个实数

*rel_tol*：大于等于0实数，为相对容差，是a和b之间允许的最大差值相对于a和b中较大值的比值，为定值，因此相对最大差值会随着a和b的变化而变化。默认值为1e-09，确保在十进制下两数有大约9位数字相同。

*abs_tol*：大于等于0，最小绝对容差，当a和b过小，相对容差产生的最大差值过小，其不能再正常发挥作用时，最小绝对容差充当最大差值。默认值为0.0

return：返回一个布尔值，如果上述公式成立，返回True，不成立返回False

注意：

​	由于浮点数运算规则精度局限，==不再发挥作用时，该方法可用于判断两浮点数的近似相等

```python
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

```

#### 12 math.isfinite(x)

判断x是否有限，如果x既不是正负无穷也不是NaN，则返回True，否则返回False

x：实数和浮点值math.nan以及±math.inf

return：返回一个布尔值，如果x既不是正负无穷也不是NaN，则返回True，否则返回False

```python
print(math.isfinite(8))  # True
print(math.isfinite(math.inf))  # False
print(math.isfinite(math.nan))  # False

```

#### 13 math.isinf(x)

判断x是否为正负无穷，是返回True，否则返回False

x：实数和浮点值math.nan以及±math.inf

return：返回一个布尔值，如果x是正负无穷，则返回True，否则返回False

```python
print(math.isinf(math.nan))  # False
print(math.isinf(-math.inf))  # True
print(math.isinf(float('inf')))  # True

```

#### 14 math.isnan(x)

判断数字是否为NaN（非数字），如果数字是NaN（不是数字），则返回True，否则返回False

x：实数和浮点值math.nan以及±math.inf

return：返回一个布尔值，如果x是nan，则返回True，否则返回False

```python
print(math.isnan(math.inf))  # False
print(math.isnan(math.nan))  # True
print(math.isnan(float('nan')))  # True

```

#### 15 math.isqrt(x)

返回整数x的平方根，并将平方根数向下舍入到最接近的整数（小于等于x的最大整数）

x：非负int整型，否则报错

```python
# print(math.isqrt(-1))  # ValueError: isqrt() argument must be nonnegative
# print(math.isqrt(2.5)) # TypeError: 'float' object cannot be interpreted as an integer
print(math.isqrt(0))  # 0
print(math.isqrt(3))  # 1

```

对于某些应用来说，可能需要得到最小正整数a使得n <= a^2，此时使用a = 1 + math.isqrt(n - 1)（n - 1为了防止完全平方跟出错）

证明：反证，令m为非完全平方（等号取不到）n，n为a

n^2^ < m < (n + 1)^2^ < m + 1 < (n + 2)^2^

n^2^ + 1 < m < n^2^ + 2n

n^2^ + 2 < m + 1 < n^2^ + 2n + 1

两式不能同时满足

#### 16 math.lcm(*x1, x2, ..., xn*)

返回给定的整数参数中的最小公倍数

*x1, x2, ..., xn（非必需参数）*：都为int整型（而不是一个可迭代数组），否则报错

return：返回一个int整型，表示两个或多个整数的最小公倍数，当括号内无参数时，返回【1】

注意：

​	1、输入整型可以为负数，负数的公倍数可以乘其对应正数的相反数，所以计算时相当于计算这些整数绝对值的最小公倍数

​	2、有0存在时，都返回0

​	3、无参数时，返回【1】

```python
# 无参数时
print(math.lcm())  # 1
print(math.lcm(0, 1, 2))  # 0
print(math.lcm(1, 2, 4, 5, 7))  # 140
print(math.lcm(-2, -3, -5))  # 30

```

#### 17 math.ldexp(x, i)

返回 x * (2 ** i)，math.frexp的反函数

x, i：x为实数，i为int整型，否则报错

return：返回一个浮点值，返回 x * (2 ** i)

```python
# print(math.ldexp(2, 5.0))  # TypeError: Expected an int as second argument to ldexp.
print(math.ldexp(1.9, 25))  # 63753420.8
print(math.ldexp(-1, -1))  # -0.5
print(math.ldexp(0, 0))  # 0.0

```

#### 18 math.modf(x)

以元组形式返回x的小数部分和正数部分，两个值都带x的符号

x：实数

return：返回一个元组，且元组内两个数都为浮点型（包括整数部分）

```python
print(math.modf(-1.8))  # (-0.8, -1.0)
print(type(math.modf(-1.89)))  # <class 'tuple'>

```

#### 19 math.nextafter(x, y)

返回x的下一个浮点值，方向为x朝y

x：实数

return：返回x的下一个【浮点值】，方向为x朝y，由于规则，小数部分最后一位改变的位置由整个数（整数部分的长短）决定。x和y相等时，返回x或y的浮点类型值

```python
print(math.nextafter(1, 1.2))  # 1.0000000000000002
print(math.nextafter(1.0000000000000002, math.inf))  # 1.0000000000000004
# y为nan时，结果都为nan
print(math.nextafter(0, math.nan))  # nan
print(math.nextafter(-math.inf, 0))  # -1.7976931348623157e+308
print(math.nextafter(math.inf, 0))  # 1.7976931348623157e+308
# x和y相等返回y
print(math.nextafter(1, 1))  # 1.0
print(math.nextafter(math.inf, math.inf))  # inf

```

#### 20 math.perm(n, *k*)

返回不重复且有顺序地从 n 项中选择 k 项的方式总数（排列）

n, *k*：必须为非负int整型，否则报错。k默认值为n

return：返回一个int整型，代表排列的总数

注意以下几种特殊情况：

​	1、无需k <= n，k > n时结果为0

​			math.perm(1, 2) ==> 0

​	2、math.perm(7, 0) ==> 1

​	3、math.perm(0, 7) ==> 0

​	4、math.perm(0, 0) ==> 1

```python
print(math.perm(5, 4))  # 1
print(math.perm(5))  # 120
print(math.perm(1, 2))  # 0
print(math.perm(7, 0))  # 1
print(math.perm(0, 7))  # 0
print(math.perm(0, 0))  # 1

```

#### 21 math.prod(*x*, *,  *start*)

返回可迭代数组x内所有元素的积

x：可迭代数组x，x内各个元素都为实数

*start*：起始值，即start * x1 * x2 * ... * xn，实数，默认值为1

return：若x内和start都为整型，返回int整型，否则返回一个浮点值，表示可迭代对象中所有元素的积。若x为空的可迭代对象，返回起始值

```python
print(math.prod([1.0, 2, 3, 4]))  # 24.0
print(math.prod([1, 2, 3, 4]))  # 24
print(math.prod([]))  # 1
# print(math.prod([], 2))  # 报错，需要注明参数名称
print(math.prod([], start=2))  # 2
print(math.prod([1, 2, 3, 4], start=2.5))  # 60.0

```

#### 22 math.remainder(x, y)

返回x / y的绝对值最小的余数

x：实数

y：非零实数

return：返回一个浮点值（即使余数为整数），表示x / y的绝对值最小的余数

注意：

​	1、y不等于nan时，x不能等于±inf，y等于nan时，返回nan

​	2、其会比较不同商的余数，取绝对值最小的那个，与math.fmod()不同

```python
print(math.remainder(7, 4))  # -1.0
print(math.remainder(math.inf, math.nan))  # nan
# print(math.remainder(math.inf, 7))  # ValueError: math domain error
print(math.remainder(-5, -6))  # 1.0

```

#### 23 math.trunc(x)

返回x的整数部分

x：实数

return：返回一个int整型，表示x的整数部分（若为0没有正负之分）

```python
print(math.trunc(5))  # 5
print(math.trunc(0.8))  # 0
print(math.trunc(-0.9))  # 0
print(math.trunc(9.8))  # 9
print(math.trunc(-9.8))  # -9

```

#### 24 math.ulp(x)

返回x的最小比特位进一的值，最大浮点数返回退一的值

x：实数

return：返回一个浮点值，表示x的最小比特位进一的值

注意：

​	可以和math.nextafter()比较得到ulp的作用

​	以下几种特别情况

​		1、x为nan，返回nan

​		2、x为负数时，返回ulp(-x)

​		3、x为±inf时，都返回inf

​		4、x为0时，返回最小正浮点数

​		5、x为可表示的最大浮点数（1.7976931348623157e+308）时，返回退一的值

```python
print(math.ulp(math.nan))  # nan
print(math.ulp(-math.inf))  # inf
print(math.ulp(-1))  # 2.220446049250313e-16
print(math.ulp(1))  # 2.220446049250313e-16
print(math.ulp(0.0))  # 5e-324

# 和math.nextafter()比较
print(math.ulp(10))  # 1.7763568394002505e-15
print(math.nextafter(10, 11))  # 10.000000000000002
# 末尾的2即为math.ulp()的值

```

### 3.5 幂函数和对数函数

#### 1 math.exp(x)

返回e^x^

x：实数

return：浮点数，表示e的x次幂

```python
import math

print(math.exp(3.9))  # 49.40244910553017
print(math.exp(-1.1))  # 0.33287108369807955

```

#### 2 math.expm1(x)

返回e^x^ - 1

x：实数

return：浮点数，表示e的x次幂减一

```python
print(math.expm1(3.9))  # 48.40244910553017
print(math.expm1(-1.1))  # -0.6671289163019205

```

该方法可以有效防止直接计算math.exp(x) - 1造成的精度丢失问题

#### 3 math.log(x, *base*)

返回x的底数为base的对数

x：正实数，否则报错

*base*：正且不等于1的实数，默认e，否则报错

return：返回一个浮点值，表示x的自然对数

```python
# print(math.log(1, -1))  # ValueError: math domain error
# print(math.log(-1, 1))  # ValueError: math domain error
# print(math.log(0))  # ValueError: math domain error
# print(math.log(9, 0))  # ValueError: math domain error
# print(math.log(1, 1))  # ZeroDivisionError: float division by zero
print(math.log(5))  # 1.6094379124341003

```

#### 4 math.log1p(x)

返回1 + x的自然对数

x：大于-1实数，否则报错

return：返回一个浮点值，表示 1+x 以 e 为底的自然对数

```python
# print(math.log1p(-1))  # ValueError: math domain error
print(math.log1p(0))  # 0.0
print(math.log1p(1))  # 0.6931471805599453

```

当x趋近0时，该函数值比math.log()更精确

#### 5 math.log2(x)

返回x以2为底的对数

x：正实数，否则报错

return：返回一个浮点值，表示x以 2 为底的对数

```python
print(math.log2(3))  # 1.584962500721156

```

该方法通常比math.log(x, 2)更精确

#### 6 math.log10(x)

返回x以10为底的对数，同上

该方法通常比math.log(x, 10)更精确

#### 7 math.pow(x, y)

返回x的y次幂

x：实数，代表基数

y：实数，代表指数

return：返回一个浮点值，表示x的y次幂

注意：如果x为负且y不是整数（整数包括浮点型整数），报错

```python
# print(math.pow(-1, 1.2))  # ValueError: math domain error
print(math.pow(-1, -2.0))  # 1.0
print(math.pow(2, 8))  # 256.0
print(math.pow(4, -2.2))  # 0.04736614270344993

```

#### 8 math.sqrt(x)

返回x的平方根

x：非负实数

return：返回一个浮点值，表示x的平方根

```python
print(math.sqrt(2))  # 1.4142135623730951

```

### 3.6 特殊函数

#### 1 math.erf(x)

返回自变量为x的误差函数值，其中误差函数为$erf(x) = \frac{2}{\sqrt{π}}\int_0^xe^{-t^2}\,{\rm d}t $

x：实数

return：返回一个浮点值，表示x的误差函数值

```python
import math

print(math.erf(0))  # 0.0
print(math.erf(3))  # 0.9999779095030014
print(math.erf(10))  # 1.0 精度不够

```

该函数可以用于生成正态函数的积分值

#### 2 math.erfc(x)

返回自变量为x的互补误差函数值，其为1 - erf(x)

x:实数

return：返回一个浮点值，表示x的互补误差函数值

```python
print(math.erfc(2))  # 0.004677734981047266
print(math.erfc(-6))  # 2.0 精度不够
print(math.erfc(0))  # 1.0
print(math.erfc(10))  # 2.088487583762545e-45 整数位为0的数能存储更多小数位

```

#### 3 math.gamma(x)

返回自变量为x的gamma函数值，其为$gamma(x)=\int_0^{＋∞}t^{x-1}e^{-t}\,{\rm d}t $

x：排除所有非正整数的实数，否则报错

return：返回一个浮点值，表示x的gamma函数值

```python
# print(math.gamma(0))  # ValueError: math domain error
print(math.gamma(10))  # 362880.0

```

#### 4 math.lgamma(x)

返回自变量为x的gamma函数值的绝对值的自然对数值，同上