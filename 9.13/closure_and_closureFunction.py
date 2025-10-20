
# 闭包的特点
def func():
    name = "yc" 
    def inner():
        print(name)
    return inner
f = func()
f()

# 闭包函数案例：使用闭包保持一个计数器的状态

def make_counter():
    count = 0  # 外部变量

    def counter():  # 嵌套函数
        nonlocal count  # 声明使用外层变量
        count += 1
        return count

    return counter  # 返回嵌套函数

# 创建一个计数器
my_counter = make_counter()

# 测试计数器
print(my_counter())  # 输出: 1
my_counter()
my_counter()
my_counter()
print(my_counter())  # 输出: 5


# 判断是否为闭包函数
# 判断闭包函数的方法 `_closure_` 或者查看函数的`_code_.co_freevars`属性

def func():
    name = 'ycyc'
    def inner():
        print(name)
    return inner

f = func()
print(f.__code__.co_freevars)   # 可以通过f.__code__.co_freevars属性来查看到该函数是否应用了外部作用域的变量
print(f.__closure__)    # 如果打印出的内容非空，说明该函数是闭包函数

name = 'EaglesLab'
def func():

    def inner():
        print(name)
    return inner

f = func()
print(f.__code__.co_freevars)
print(f.__closure__)    # 如果答应出的内容是None，说明该函数没有应用外部作用域的变量，不满足闭包函数的条件


# 案例：获取网页内容
## 使用闭包函数将第一次访问到的网页内容封装到外部作用于的变量中，后面直接调用变量

### 普通写法
from urllib.request import urlopen
def func():
    content = urlopen('https://myip.ipip.net').read().decode('utf-8')
    print(content)

for i in range(5):
    func()

"""
当前 IP：115.  来自于：中国 浙江 杭州  电信

当前 IP：115.  来自于：中国 浙江 杭州  电信

当前 IP：115.  来自于：中国 浙江 杭州  电信

当前 IP：115.  来自于：中国 浙江 杭州  电信

当前 IP：115.  来自于：中国 浙江 杭州  电信
"""

### 闭包写法
from urllib.request import urlopen

def func():
    content = urlopen('https://myip.ipip.net').read().decode('utf-8')
    def inner():
        print(content)
    return inner

f = func()
for i in range(5):
    f()

print(f.__code__.co_freevars)