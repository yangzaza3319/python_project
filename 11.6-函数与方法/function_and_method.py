# 通过打印函数（方法名）来观察函数和方法的区别
def func():
    pass
print(func)

class A:
    def func(self):
        pass
print(A.func)      # 输出 <function A.func at 0x105351080>
obj = A()
print(obj.func)    # 输出 <bound method A.func of <__main__.A object at 0x1052f5160>>

# 同一个def,既是函数又是方法
class Dog():
    def bark(self):
        print("Woof!")

print(Dog.bark)

dog = Dog()
print(dog.bark)


"""
输出
    <function Dog.bark at 0x105351260>
    <bound method Dog.bark of <__main__.Dog object at 0x1052f57f0>>
"""

# 通过types模块验证区别
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

