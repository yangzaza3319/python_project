# boolExample.py

print("=== Python 布尔值逻辑运算演示 ===\n")

# --- 1. 逻辑与 (and) ---
print("1. 逻辑与 (and) - 全真为真")
print("True  and True  =", True and True)    # True
print("True  and False =", True and False)   # False
print("False and True  =", False and True)   # False
print("False and False =", False and False)  # False

# 在条件表达式中使用
a = 5
b = 10
result = (a > 0) and (b < 20)
print(f"\n示例: (a=5 > 0) and (b=10 < 20) = {result}")

# 短路求值演示
def true_func():
    print("  -> true_func: 返回 True")
    return True

def false_func():
    print("  -> false_func: 返回 False")
    return False

print("\n短路求值 (and): 如果第一个为 False，不计算第二个")
result = false_func() and true_func() # true_func() 不会被调用
print("结果:", result)


# --- 2. 逻辑或 (or) ---
print("\n\n2. 逻辑或 (or) - 一真为真")
print("True  or True  =", True or True)     # True
print("True  or False =", True or False)    # True
print("False or True  =", False or True)    # True
print("False or False =", False or False)   # False

# 在条件表达式中使用
x = 15
y = 3
result = (x > 10) or (y > 10)
print(f"\n示例: (x=15 > 10) or (y=3 > 10) = {result}")

# 短路求值演示
print("\n短路求值 (or): 如果第一个为 True，不计算第二个")
result = true_func() or false_func() # false_func() 不会被调用
print("结果:", result)


# --- 3. 逻辑非 (not) ---
print("\n\n3. 逻辑非 (not) - 取反")
print("not True  =", not True)  # False
print("not False =", not False) # True

# 在条件中使用
age = 17
is_adult = age >= 18
print(f"\n示例: age={age} >= 18 -> is_adult = {is_adult}")
print(f"        not is_adult = {not is_adult}")
if not is_adult:
    print("        你还未成年。")


# --- 4. 复合逻辑表达式 ---
print("\n\n4. 复合逻辑表达式")
p = True
q = False
r = True

print(f"p={p}, q={q}, r={r}")
print("运算符优先级: not > and > or")

# 演示优先级和括号
result1 = p and q or r      # (p and q) or r -> (True and False) or True -> False or True -> True
result2 = p and (q or r)    # p and (q or r) -> True and (False or True) -> True and True -> True
result3 = not p or q        # (not p) or q -> False or False -> False

print(f"p and q or r     = {result1}")
print(f"p and (q or r)   = {result2}")
print(f"not p or q       = {result3}")

