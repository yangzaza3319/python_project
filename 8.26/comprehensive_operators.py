# comprehensive_operators.py
## python基本运算符演示

# --- 算术运算符 ---
print("1 + 1 =", 1 + 1)                 # 输出： 1 + 1 = 2
print("5 - 2 =", 5 - 2)                 # 输出： 5 - 2 = 3
print("10 / 2 =", 10 / 2)     # 浮点数   输出： 10 / 2 = 5
print("7 // 2 =", 7 // 2)     # 地板除   输出： 7 % 2 = 3
print("7 % 3 =", 7 % 3)       # 取模     输出： 7 % 3 = 2
print("2 ** 3 =", 2 ** 3)     # 幂运算   输出： 2 ** 3 = 8

# --- 关系运算符 ---
print("5 == 5 is", 5 == 5)     # 输出 5 == 5 is True
print("1 != 1 is", 1 != 1)     # 输出 1 ！= 1 is False 
print("3 > 2 is", 3 > 2)       # 输出 3 > 2 is True
print("5 < 9 is", 5 < 9)       # 输出 5 < 9 is True
print("3 >= 19 is", 3 >= 19)   # 输出 3 >= 19 is False
print("45 <= 45 is", 45 <= 45) # 输出 45 <= 45 is True


# --- 逻辑运算符 ---
print("True and False is", True and False)  # 输出 True and False is False
print("True or False is", True or False)    # 输出 True or False is True
print("not True is", not True)              # 输出 not True is False


# --- 赋值运算符 ---
x = 5
print(x) # 输出 5 

x2 += 7  # x2 = x2 + 7
print("x2 += 7 -> x2 =", x2)    # 输出 x2 += 7  ——> x2 = 12 

x3 = 1
x3 -= 6  # x3 = x3 - 6
print("x3 -= 6 -> x3 =", x3)    # 输出 x3 -= 6  ——> x3 = -5

x4 = 0.5
x4 *= 5  # x4 = x4 * 5
print("x4 *= 5 -> x4 =", x4)    # 输出 x4 *= 5 ——> x4 = 2.5


x5 /= 3  # x5 = x5 / 3
x6 = 6
x6 /= 3 
print("x5 /= 3 -> x5 =", x5)       # 输出 x5 /= 3 ——> x5 = 1.66666666667
print("x6 /= 3 -> x6 =", x6)       # 输出 x6 /= 3 ——> x6 = 2.0


x7 = 4
x7 //= 2 # x = x // 2
x8 = 5
x8 //= 2
print("x7 //= 2 -> x7 =", x7)        # 输出 x7 // 2 = 2 
print("x8 //= 2 ——> x8 =",x8)        # 输出 x8 // 2 = 2

x9 = 11
x9 %= 5  # x9 = x9 % 5
print("x9 %= 5 -> x9 =", x9)            # 输出 x9 %= 5 ——> x9 = 1 

x10 = 2
x10 **= 3 # x10 = x10 ** 3
print("x10 **= 3 -> x10 =", x10)        # 输出 x10 **= 3 ——> x10 = 8

# --- 位运算符 ---
a = 5  # 二进制: 101
b = 3  # 二进制: 011
print(f"a = {a} (二进制: {bin(a)})")   # 输出 a = 5 (二进制: 0b101)
print(f"b = {b} (二进制: {bin(b)})")   # 输出 b = 3 (二进制: 0b11)
print(f"{a} & {b} =", a & b)  # 101 & 011 = 001 -> 1   # 输出 5 & 3 = 1
print(f"{a} | {b} =", a | b)  # 101 | 011 = 111 -> 7   # 输出 5 | 3 = 7
print(f"{a} ^ {b} =", a ^ b)  # 101 ^ 011 = 110 -> 6   # 输出 5 ^ 3 = 6
print(f"~{a} =", ~a)          # 按位取反                # 输出 ~5 = -6
print(f"{a} << 1 =", a << 1)  # 左移1位: 1010 -> 10     # 输出 5 << 1 = 10
print(f"{a} >> 1 =", a >> 1)  # 右移1位: 010 -> 2       # 输出 5 >> 1 = 2


# --- 成员运算符 ---
print((3 in [1,2,3]))       # 输出True
print((1 not in [1,2,3]))   # 输出False