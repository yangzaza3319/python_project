# __len__
class B:
    def __len__(self):
        return 666
b = B()
print(len(b)) # len一个对象就会触发__len__方法，输出 666
class A:
    def __init__(self):
        self.a = 1
        self.b = 2
    def __len__(self):
        return len(self.__dict__)
a = A()      
print(len(a))    # 输出 2

# __hash__
class A:
    def __init__(self):
        self.a = 1
        self.b =2
    def __hash__(self):
        return hash(str(self.a)+str(self.b))

# __str__
class A:
    def __init__(self):
        pass
    def __str__(self):
        return '小问号'
a = A()
print(a)          # 输出 小问号
print('%s' % a)   # 输出 小问号

# __repr__

class A:
    def __init__(self):
        pass
    def __repr__(self):
        return "小问号"
a = A()
print(repr(a))   # 输出 小问号
print('%s' % a)  # 输出 小问号


# __call__


class Foo:
    def __init__(self):
        print('__init__')
    
    def __call__(self, *args, **kwds):
        print('__call__')

obj = Foo()  # 执行__init__,输出__init__
obj() # 执行call， 输出__call__


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

# __new__
class A:
    def __new__(cls,*args,**kwargs): # 调用父类的`__new__`创建实例并返回实例
        print("in new function")
        return object.__new__(A,*args,**kwargs)
    def __init__(self):
        self.x = 1
        print("in init function")

a = A()
print(a.x) # 输出 1