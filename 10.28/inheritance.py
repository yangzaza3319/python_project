# 对象执行父类方法
class Animal:
    type_name = '动物'
    
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def eat(self, food):
        print(f'{self.name}吃{food}')

class Person(Animal):
    pass


class Cat(Animal):
    pass

class Dog(Animal):
    pass
# 使用
p1 = Person('小问号', 18, '男')
p1.eat('东北菜')  # 输出：小问号吃东北菜

d1 = Dog('小白',3,'公')
d1.eat('狗粮')
"""
小问号吃东北菜
小白吃狗粮
"""

# 多继承

class Animal:
    def __init__(self,name):
        self.name = name


class Flyable:
    def fly(self):
        print("我会飞")

class Swimmable:
    def swim(self):
        print("我会游泳")

class Duck(Animal,Flyable,Swimmable):
    pass

d = Duck("唐老鸭")
d.fly()
d.swim()

# 方法解析的顺序
class A:
    def method(self):
        print("A")
class B(A):
    def method(self):
        print("B")
class C(A):
    def method(self):
        print("C")

class D(B,C):
    pass

d = D()
d.method()

print(D.__mro__)
"""
输出
B
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
***因为B在C之前，所以d.method()输出B***
"""

# 父类的私有属性和私有方法 案例
class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(self.name+"eating...")
    def eat2(self):
        self.eat()

class Dog(Animal):
    pass
a = Dog("小黑")
print(a.name)
a.eat()
a.eat2()
"""
输出
小黑
小黑eating...
小黑eating...
"""

# 多继承
class Shengxian:
    def Fly(self):
        print("我是神仙，我会飞！")
    
    def Eat(self):
        print("吃人参果")
class Monkey:
    def Eat(self):
        print("我是猴子，我爱吃桃子")
class Monkey_king(Shengxian,Monkey):
    def __init__(self):
        self.name = "孙猴子"
    def Eat(self):
        print("我是齐天大圣，不用吃东西")

swk = Monkey_king()
swk.Eat()
"""
输出
我是齐天大圣，不用吃东西
"""

