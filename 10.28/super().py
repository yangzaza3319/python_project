# 学生类继承人类，需要初始化姓名和学号
class Person:
    def __init__(self,name):
        self.name = name
        print(f"Person 初始化:{self.name}")
class Student(Person):
    def __init__(self,name,student_id):
        super().__init__(name)
        self.student_id = student_id
        print(f"Student初始化:{self.student_id}")
s = Student("张三","2025001")
"""
输出
    Person 初始化:张三
    Student初始化:2025001
"""

# 狗叫时，先发出通用动物声音，再发出“汪汪”
class Animal:
    def speak(self):
        print("动物发出声音")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("汪汪")
d = Dog()
d.speak()
"""
输出
    动物发出声音
    汪汪
"""

# 一个角色既能飞行，又能游泳，还属于动物
class Animal:
    def __init__(self,name):
        self.name = name
        print(f"Animal:{self.name}")
class Flyable:
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        print("Flyable:我会飞")
class Swimmable:
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        print("Swimmable:我会游泳")
class Duck(Flyable,Swimmable,Animal):
    def __init__(self, name):
        super().__init__(name)
        print("Duck:我是鸭子")

d = Duck("唐老鸭")
print("\nMRO 顺序：",Duck.__mro__)
"""
输出
    Animal:唐老鸭
    Swimmable:我会游泳
    Flyable:我会飞
    Duck:我是鸭子
    MRO 顺序： (<class '__main__.Duck'>, <class '__main__.Flyable'>, <class '__main__.Swimmable'>, <class '__main__.Animal'>, <class 'object'>)
"""