# 双下方法
> 也叫魔术方法或特殊方法，是指以下划线开头或结尾的方法
> 双下方法是Python面向对象编程的核心机制，用于定义类的“行为协议”，让自定义对象能像内置类型（如int\list\str）一样支持运算法符、函数调用、迭代等操作

## 常用双下方法
1. `__init__`
> 用于初始化类的实例，接收参数并设置实例属性
```python
# 代码示例
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
```

2. `__len__`
> 用于获取对象的长度或元素个数
```python
class B:
    def __len__(self):
        return 666
b = B()
print(len(b)) # len一个对象就会触发__len__方法
class A:
    def __init__(self):
        self.a = 1
        self.b = 2
    def __len__(self):
        return len(self.__dict__)
a = A()
print(len(a))
```
3. `__hash__`
> 决定一个对象是否可以被哈希(hashable)，从而能否作为字典的键或集合的元素
```python
class A:
    def __init__(self):
        pass
    def __str__(self):
        return '小问号'
a = A()
print(a)
print('%s' % a)

```

4. `__str__`
> 如果一个类中定义了__str__方法,那么在print(obj)时，默认输出该方法的返回值
```python
class A:
    def __init__(self):
        pass
    def __str__(self):
        return '小问号'
a = A()
print(a)          # 输出 小问号
print('%s' % a)   # 输出 小问号
```

5. `__repr__`
> 如果一个类中定义了__repr__方法，那么在repr(obj)时，默认输出该方法的返回值

```python
class A:
    def __init__(self):
        pass
    def __repr__(self):
        return "小问号"
a = A()
print(repr(a))   # 输出 小问号
print('%s' % a)  # 输出 小问号
```
6. `__call__`
> 通过obj触发执行
```python
class Foo:
    def __init__(self):
        print('__init__')
    
    def __call__(self, *args, **kwds):
        print('__call__')

obj = Foo()  # 执行__init__
obj() # 执行call
```

7. `__eq__`
> 通过`==`触发类中的`__eq__`方法
```python
# __eq__
class A:
    def __init__(self):
        self.a = 1
        self.b = 2
    def __eq__(self, obj):
        if self.a == obj.a and self.b == obj.b:
            return True
a = A()
b = A()
print(a == b)   # 输出 True
```
8. `__del__`
> 析构方法,当对象在内存中被释放时，自动触发执行
此方法无须定义，程序员无需关心内存的分配与释放，这些工作都是交给Python解释器执行，所以析构函数的调用由解释器在垃圾回收时自动触发执行

9. `__new__`
> 在Python中,__new__是一个控制对象创建过程中的魔术方法，他比`__init__`更早执行
- 优先级
`__new__`是一个控制对象创建过程的魔术方法，它比__init__更早执行
- 返回值
`__new__`必须返回实例对象(否则`__init__`不会执行)，而`__init__`无返回值
- 静态方法
`__new__`隐式作为静态方法存在，第一个参数是类本身cls,而非实例self
- 继承链
若未重写`__new__`，python会沿继承链调用父类的`__new__`,直至`object.__new__`
