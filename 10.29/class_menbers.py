# 类中的字段（变量）
class Dog:
    species = "西高地"
    def __init__(self,name):
        self.name = name 

d = Dog("来福")
print("我的小狗叫"+d.name)

d1 = Dog("旺财")
print("我最爱的种类是"+Dog.species)
d.species = "边牧"
print("我最爱的种类是"+d.species)
"""
输出
    我的小狗叫来福
    我最爱的种类是西高地
    我最爱的种类是边牧
"""

# 类中的方法（函数）
class Dog:
    species = "Canis lupus"  # 类变量

    def __init__(self, name, age=0):
        self.name = name  # 实例变量
        self.age = age

    def bark(self):
        print(f"{self.name} is barking!")

    @classmethod
    def create_from_string(cls, s):
        name, age = s.split(",")
        return cls(name, int(age))  # 创建实例时调用__init__方法

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def describe():
        return "Dogs are domesticated animals."

d = Dog("Buddy", 11)
d.bark()  # Buddy is barking!

d1 = Dog.create_from_string("Max,5")    # 通过类方法创建实例
d2 = Dog("Bella", 3)  # 通过类方法创建实例
print(d2.name)
print(d1.age)

print(Dog.get_species())    # 类方法调用
d3 = Dog("Charlie", 2)
print(d3.get_species())  # 实例调用

print(Dog.describe())  # 静态方法调用
"""
输出 
    Dogs are domesticated animals.
"""

# 属性案例

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value

    @balance.deleter
    def balance(self):
        del self.__balance

account = BankAccount(100)
print(account.balance)  # 调用getter方法
account.balance = 200  # 调用setter方法
del account.balance  # 删除属性
print(account.balance)
"""
输出
    AttributeError: 'BankAccount' object has no attribute '_BankAccount__balance'（）
del account.balance 调用了 @balance.deleter：
del self.__balance 这行代码 真正删除了实例属性 _BankAccount__balance（因为 __balance 被名称改写）。
接着 print(account.balance) 会调用 @property 的 getter： return self.__balance，但此时 self.__balance 已经不存在了！
"""

# 其他特殊成员的示例
class MyClass:
    def __init__(self, value):
        self.value = value  # 公有属性
        self.__value = value # 私有属性

    def public_method(self):    
        return f'这是类的公有方法, value: {self.value}'

    def __private_method(self):
        return f'这是类的私有方法, value: {self.__value}'

    def get_value(self):
        return self.__value     # 通过公有方法访问私有属性

obj = MyClass(10)
print(obj.value)       # 访问公有属性
print(obj.public_method())     # 调用公有方法
print(obj.__value)  # 访问公有属性
print(obj.__private_method())  # 调用私有方法
"""
输出
    10
    这是类的公有方法，value：10
    AttributeError: 'MyClass' object has no attribute '__value'. Did you mean: 'value'?
    AttributeError: 'MyClass' object has no attribute '__private_method'
"""

# 综合案例