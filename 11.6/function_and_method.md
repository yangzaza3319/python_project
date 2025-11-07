## 函数（fuction）VS 方法（method）

### 基本定义
1. 函数
- 在模块级别（全局）或局部作用域中定义
- 调用时不自动传入任何隐式参数
- 通过def直接定义
2. 方法
- 定义在类的内部
- 通过实例调用时，会自动传入实例本身作为第一个参数(通常是self)
- 本质上是一个绑定方法

### 关键区别的对比
特性|函数|方法
---|---|---
定义位置|模块/函数内|类内部
调用方式|直接调用|通过类或者实例调用
第一个参数|显示传入|实例自动传入
类型|`<class 'function'>`|`<class 'method'>`
是否绑定| 否| 绑定到实例或类

> 在其他语言中：如JAVA只有方法，C中只有函数，C++则取决于是否在类中

### 案例理解：同一个def，既是函数又是方法
```python
class Dog():
    def bark(self):
        print("Woof!")

print(Dog.bark)  # 通过类访问，此时为函数——>输出 <function Dog.bark at 0x105351260>

dog = Dog()
print(dog.bark) # 通过实例访问,此时为method——>输出 <bound method Dog.bark of <__main__.Dog object at 0x1052f57f0>>
```


### 通过打印函数(方法)观察两者的区别
```python
def func():
    pass
print(func)

class A:
    def func(self):
        pass
print(A.func)
obj = A()
print(obj.func)
```

### 通过types模块验证两者的区别

```python
from types import FunctionType
from types import MethodType

def func():
    pass
class A:
    def func(self):
        pass
obj = A()

print(isinstance(func,FunctionType))        # 输出 True
print(isinstance(A.func,FunctionType))      # 输出 True
print(isinstance(obj.func,FunctionType))    # 输出 False
print(isinstance(obj.func,MethodType))      # 输出 True

```

### 静态方法是函数
```python
from types import FunctionType
from types import MethodType

def func():
    pass
class A:
    def func(self):
        pass
obj = A()

print(isinstance(func,FunctionType))        # 输出 True
print(isinstance(A.func,FunctionType))      # 输出 True
print(isinstance(obj.func,FunctionType))    # 输出 False
print(isinstance(obj.func,MethodType))      # 输出 True


# 静态方法是函数
from types import FunctionType
from types import MethodType

class A:
    def func(self):
        pass

    @classmethod
    def func1(self):
        pass

    @staticmethod
    def func2(self):
        pass

obj = A()

"""
静态方法其实是函数
"""
print(isinstance(A.func2,FunctionType))    # 输出 True
print(isinstance(obj.func2,FunctionType))  # 输出 True
```
