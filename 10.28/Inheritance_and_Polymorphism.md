## 继承
> 子类可以复用父类的属性和方法，并扩展新功能，实现代码复用和逻辑分层。（如电动车类继承自汽车类，新增充电方法）
1. 创建对象（不用继承）
```python
class Person:
    def __init__(self,name,sex,age):
        self.name = name
        self.age = age
        self.sex = sex
class Cat:
    def __init__(self,name.sex,age):
        self.name = name
        self.age = age
        self.sex = sex
class Dog:
    def __init__(self,name,sex,age):
        self.name = name
        self.age = age
        self.sex = sex
```
2. 创建对象（使用继承）

```python
class Animal(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print(f"{self.name}吃东西...")
class Dog(Animal):
    pass

xiaotianquan = Dog("哮天犬",5)
xiaotianquan.eat()   # 输出 哮天犬吃东西....
```
### 继承的优点
- 增加了类的耦合性(耦合性不宜多，宜精)
- 减少了重复代码
- 代码更加规范化，合理化

### 继承分类
> python中类的种类可以分为新式类和经典类
- 经典类是指没有显式继承自object的类。他们使用旧的类定义方式
- 新式类是指显示继承自object或其他新式类的类

#### 单继承

##### 对象执行父类方法
人、猫、狗继承动物类

##### 方法重写
- 在开发中，父类的方法实现和子类的方法实现完全不同，可以使用覆盖的方式，在子类中重新编写父类的方法实现
- 具体的实现方式，相当于在子类中定义了一个和父类同名的方法并且实现
- 重写之后，在运行时只会调用子类中重写的方法，而不再会调用父类封装的方法

##### 子类中扩展父类的方法
- 子类中的实现方法中包含父类的方法实现 且 父类原本封装的方法实现是子类方法的一部分
- 可以使用
    1. 在子类中重写父类的方法
    2. `super().父类方法`来调用父类方法的执行
    3. 代码其他位置针对子类的需求，编写子类特有的代码实现

##### 父类的私有属性和私有方法
子类对象不能在自己的方法内部，直接访问父类的私有属性或私有方法，但可以通过父类的公有方法间接访问
- 私有属性（私有方法）是对象的隐私，不对外公开，外界以及子类都不能直接访问
- 私有属性（私有方法）通常用于做一些内部的事情

![父类的私有属性和私有方法](image.png)
> B的对象：不能直接访问__num2__属性、不能在demo方法内访问__num2属性、B的对象可以在demo方法内部，能够访问__num2属性和__test方法

#### 多继承
> 一个子类同时继承多个父类，并且具有所有父类的属性和方法(如孩子会继承自己父亲和母亲的特性)

##### 方法解析顺序(MRO)
> 当多个父类有同名方法时，Python MRO(Method Resolution Order)


## 多态
> 同一方法在不同对象中呈现不同行为，增强代码灵活性（例如动物类的发声方法在猫狗对象中过分别输出汪汪和喵喵）
- 多态可以增强代码的灵活性
- 以继承和重写父类方法为前提
- 是调用方法的技巧，不会影响到类的内部设计

### 切入案例
![alt text](UML_introduction.png)

### 哮天犬案例
> 需求
1. 在Dog类中封装方法game
2. 定义Xiaotianquan继承自Dog，并且重写game方法
3. 定义person类并且封装一个和狗玩的方法
![alt text](UML_xioatianquan.png)
> 小结
Human类只需要让狗对象调用dog_play()方法，而不关心具体是什么狗
dog_play()方法是在Dog父类中定义的
在程序执行时，传入不同的狗对象实参，就会产生不同的执行效果

## 鸭子类型

### 什么是鸭子类型
> 在python中，不关心对象是什么类型，只关心它能做什么（不需要显示继承某个类、不需要实现某个接口、只要对象有被需要的的方法或属性）的类型

### 代码示例

#### 基本鸭子类型

#### 文件操作中的鸭子类型
StringIO不是File，但行为像文件，所以能用

#### 迭代器协议
只要实现__iter__和__next__就能被for使用，无需继承Iterator

## 类的约束

### 引入案例
```python
## 写一个简单的支付功能
class QQpay:
    def pay(self,money):
        print('使用QQ支付%s元' % money)
class Alipay:
    def pay(self,money):
        print('使用支付宝支付%s元' % money)
a = Alipay()
a.pay(100)

b = QQpay()
b.pay(200)

## 统一一下付款方式
class QQpay:
    def pay(self,money):
        print('使用QQ支付%s元' % money)
class Alipay:
    def pay(self,money):
        print('使用支付宝支付%s元' % money)

def pay(obj,money):
    obj.pay(money)

pay(Alipay(),100)
pay(QQpay(),200)
"""
输出
    使用支付宝支付100元
    使用QQ支付200元
"""

## 再添加微信支付，但是没有统一标准，换个程序员可能产生混乱的代码
class QQpay:
    def pay(self,money):
        print('使用QQ支付%s元' % money)
class Alipay:
    def pay(self,money):
        print('使用支付宝支付%s元' % money)
class Wechatpay:
    def fukuan(self,money):
        print('使用微信支付%s元' % money)
def pay(obj,money):
    print("************")
    obj.pay(money)

pay(Alipay(),100)
pay(QQpay(),200)

Wechatpay().fukuan(300)
"""
在这种情况下，就不符合鸭子类型，接口出现不统一的情况
输出
    使用支付宝支付100元
    使用QQ支付200元
    使用微信支付300元
"""
```
### 两种类的约束
1. 使用抽象基类(ABC)+`@abstractmethod`
> 适用于需要强制继承关系的场景（如框架、库设计等）
特点 
    - 子类必须继承该基类
    - 实例化时检查是否实现了所有抽象方法
    - Python官方推荐的面向对象约束方式
优点
    - 提前报错（实例化时就检查，不是运行到方法才报错）
    - 代码结构清晰,意图明确
    - 支持抽象属性(@property+@abstractmethod)


2. 使用`Protocol`(结构化鸭子类型)
> 不需要强制继承，只关心'行为'的场景(Python 3.8+)
特点
    - 不要求继承，只要对象有对应方法/属性即可
    - 依赖静态类型检查工具（如mypy）来验证约束
    - 运行时不会报错（除非调用不存在的方法）
优点
    - 极度灵活，符合鸭子类型哲学
    - 适合插件系统、接口回调等场景
    - 与类型提示(Type Hints)完美结合

## `super()`函数
> 用于调用父类的方法，尤其在继承中非常关键。它能保证方法中调用遵循正确的方法解析顺序（MRO），避免重复调用或遗漏

### 基本作用
`super()`返回一个代理对象，可以访问父类中被重写的方法
#### 常见用途示例（在子类中调用父类的`__init__`）
```python
class Animal:
    def __init__(self,name):
        self.name = name
class Dog(Animal):
    def __init__(self,name,bread):
        super().__init__(name) # 调用分类 __init__
        self.bread = bread
d = Dog("旺财","金毛")
print(d.name,d.bread) 
"""
输出
    旺财 金毛
"""
```

### `super()`的两种写法

#### 无参数形式
```python
super().method()
```
- 自动传入当前类和self
- 简洁、安全、支持多继承

#### 带参数形式
```python
super(CurrentClass,self).method()
```

### 案例1: 单继承中调用父类初始化
学生类继承人类，需要初始化姓名和学号

### 案例2: 方法重写时扩展父类的行为
狗叫时，先发出通用动物声音，再发出“汪汪”

### 案例3: 多继承+super()协作
一个角色既能飞行，又能游泳，还属于动物
