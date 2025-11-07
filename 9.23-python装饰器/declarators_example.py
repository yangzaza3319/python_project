#1.修饰器案例切入
def func1():
    print("在func1()中")

""" 
需求：打印下列内容
hello world
in function1
hello python
"""

# 案例实现
def func2(func):
    def inner():
        print("hello world")
        func()
        print("hello python")
    return inner
func1 = func2(func1)
func1()


#2. 测试某个函数的执行时间（常规方式）
import time

def func1():
    print('in func1')

def timer(func):
    def inner():
        start = time.time()
        func()
        print(time.time() - start)
    return inner

func1 = timer(func1)  # 将dunc1()函数作为参数传出去
func1()


#3.测试某个函数的执行时间（语法糖）
import time

def timer(func):
    def innner():
        start = time.time()
        func()
        print(time.time() -start)
    return innner
@timer
def func2():
    time.sleep(1)
    print('in func2')
func2()

"""
调试结果
显式执行func2()函数
    ——>输出
    in func2
    1.0043830871582031
"""
"""
当我们在某个函数上方使用@my_decorator 的时候，python会自动将下面定义的函数作为参数传递给@my_decorator，即func1 = timer(func1)
"""

#4.装饰带单个参数的函数
import time

def timer(func):
    def inner(a):
        start = time.time()
        func(a)
        print(time.time() - start)
    return inner

@timer
def func3(a):
    time.sleep(1)
    print(a)
func3("hello_world")

"""
输出
hello_world
1.0029830932617188
"""

# 5 装饰带多个位置参数的函数
# 利用多个参数进行传参
def my_decorator(func):
    def wrapper(*args,**kwargs):
        print(f"调用{func.__name__}函数返回：位置参数：{args}，关键字参数：{kwargs}") # 打印调用的函数、传入的参数（此处没有用到关键字参数，所以打印的kwargs参数为空）
        result = func(*args,**kwargs)                                       # 调用原始函数并获取结果
        print(f"{func.__name__}函数返回：{result}")                           # 打印返回结果
        return result
    return wrapper

@my_decorator
def add(x,y):
    return x + y

result = add(3,4)
print(f"最终结果：{result}")
"""
    输出结果
调用add函数返回：参数：(3, 4)，关键字参数：{}
add函数返回：7
最终结果：7
"""

# 6 wraps装饰器

## 回顾开始的案例
import time
def func1():
    print('in func1')

def timer(func):
    def inner():
        start = time.time()
        func()
        print(time.time() - start)
    return inner
func1 = timer(func1) # 将函数本身作为参数传递进去
func1()
### 问题1——>最后执行的`func1`函数和最初的`func1`是否为同一个函数
#问题1 解法：打印函数名

import time
def func1():
    print('in func1')

def timer(func):
    def inner():
        start = time.time()
        func()
        print(time.time() - start)
    return inner
func1 = timer(func1)
print(func1.__name__)
"""
输出
inner
"""

# 使用wraps装饰器装饰
from functools import wraps
import time

def func1():
    print('in func1')

def timer(func):
    @wraps(func)
    def innner():
        start = time.time()
        func()
        print(time.time() - start)
    return innner
func1 = timer(func1)
print(func1.__name__)
"""
输出
func1
"""

# 7 带参数的装饰器
## 案例：创建一个装饰器，接受一个参数，用于指定是否打印函数的执行时间

import time
from functools import wraps

def timing_decorator(print_time=True):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            start_time = time.time()
            result = func(*args,**kwargs)
            end_time = time.time()
            if print_time:
                execution_time = end_time - start_time
                print(f"{func.__name__} 执行时间：{execution_time:.4f}秒")
            return result
        return wrapper
    return decorator
@timing_decorator(print_time=True)
def add(x,y):
    time.sleep(1)
    return(x+y)

@timing_decorator(print_time=False)
def multiply(x,y):
    time.sleep(1)
    return x * y

result_add = add(3,6)
print(f"加法结果为：{result_add}")
result_mutiply = multiply(6,7)
print(f"乘法结果为：{result_mutiply}")
"""
    输出结果
print(f"加法结果为：{result_add}")
result_mutiply = multiply(6,7)
print(f"乘法结果为：{result_mutiply}")
add 执行时间：1.0070秒
>>> print(f"加法结果为：{result_add}")
加法结果为：9
>>> result_mutiply = multiply(6,7)
>>> print(f"乘法结果为：{result_mutiply}")
乘法结果为：42
"""

# 8 多个装饰器装饰同一个函数

def decorator1(func):
    print("decorator1 被应用")
    def wrapper1():
        print("进入 decorator1")
        func()  # ← 这里的 func 是被它包装的函数
        print("退出 decorator1")
    return wrapper1

def decorator2(func):
    print("decorator2 被应用")
    def wrapper2():
        print("进入 decorator2")
        func()  # ← 这里的 func 是被它包装的函数
        print("退出 decorator2")
    return wrapper2

@decorator1
@decorator2
def f():
    print("hello")

f()
"""
    输出
decorator2 被应用
decorator1 被应用
>>> f()
进入 decorator1
进入 decorator2
hello
退出 decorator2
退出 decorator1


    程序执行的过程
f = decorator2(f) -> func = f,return inner2
f = decorator1(f) -> func = inner2,return inner1
f() = inner1() -> inner2() -> f() -> inner2() -> inner1()

       f()
        ↓
   [decorator1]   ← 最外层
        ↓
   [decorator2]   ← 中间层
        ↓
     原始函数     ← 最内层
"""

# 8.1 两个装饰器（一个打印函数执行时间、另一个打印调用参数）
import time
from functools import wraps

def decorator_time(func):
    print("这是打印函数执行时间的装饰器")
    @wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        result1 = func(*args,**kwargs)
        end = time.time()
        execution_time = end - start
        print(f"{func.__name__}执行时间：{execution_time:.4f}秒")
        return result1
    return wrapper
def decorator_argsPrint(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"调用{func.__name__}函数，位置参数：{args}，关键字参数：{kwargs}")
        result2 = func(*args,**kwargs)
        return result2
    return wrapper

@decorator_time
@decorator_argsPrint
def add(x,y,z):
    time.sleep(1)
    print(z)
    return x + y ,z

result1 = add(5,3,"返回元组")  # 参数个数需要对应
print(f"加法结果：{result1}")
"""
输出
这是打印函数执行时间的装饰器
>>> result1 = add(5,3,"返回元组")  # 参数个数需要对应
调用add函数，位置参数：(5, 3, '返回元组')，关键字参数：{}
print(f"加法结果：{result1}")
返回元组
add执行时间：1.0036秒
>>> print(f"加法结果：{result1}")
加法结果：(8, '返回元组')
"""

# 10装饰器的固定结构
from functools import wraps

def decorator_with_args(param):
    def actual_decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            print(f"装饰器参数:{param}")
            return func(*args,**kwargs)
        return wrapper
    return actual_decorator

@decorator_with_args("配置参数")
def my_function():
    print("my_function 被调用")

my_function()