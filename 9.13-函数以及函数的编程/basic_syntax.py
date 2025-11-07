# basic_syntax.py
# Python 函数基本语法演示

# 1. 最简单的函数：无参数，无返回值
def say_hello():
    """打印问候语"""
    print("Hello from the function!")

# 调用函数
say_hello()


# 2. 带参数的函数
def greet(name):
    """接收一个名字参数并打招呼"""
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")


# 3. 带返回值的函数
def add_numbers(a, b):
    """计算两个数的和并返回结果"""
    result = a + b
    return result

sum_value = add_numbers(5, 3)
print(f"5 + 3 = {sum_value}")


# 4. 带默认参数的函数
def create_greeting(name, greeting="Hi"):
    """用指定的问候语和名字创建问候语"""
    return f"{greeting}, {name}!"

print(create_greeting("Charlie"))           # 使用默认问候语
print(create_greeting("Diana", "Good morning"))  # 提供两个参数


# 5. 函数可以返回多个值（实际上是返回一个元组）
def divide_with_remainder(dividend, divisor):
    """返回除法的商和余数"""
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder  # 返回元组

q, r = divide_with_remainder(10, 3)
print(f"10 ÷ 3 = {q} 余 {r}")


# 6. 空函数 (使用 pass 占位)
def todo_function():
    """待实现的函数"""
    pass  # pass 是空操作，用于保持语法正确

todo_function()  # 可以调用，但什么都不做
