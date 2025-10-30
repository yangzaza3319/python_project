## 类的组成成员分类
> Python 的类组成成员可以分为三大类：字段（变量）、方法（函数）和属性（特殊方法）。他们的定义方式、作用域和调用规则各有不同

### 字段（变量）
字段分为实例变量和类变量，核心区别在于存储位置和作用对象：
    - 实例变量：每个变量独立拥有一份实例变量，修改不影响其他对象
    - 类变量：通过类名或实例均可访问，但通过实例修改会创建同名实例变量，覆盖类变量
#### 示例

### 方法（函数）
方法分为实例方法、类方法、和静态方法，区别在于参数和调用方式
    - 实例方法  第一个参数为self,指向调用该方法的实例（必须通过对象调用，可访问实例变量和类变量）
    - 类方法    使用`@classmethod`装饰器，参数为cls(指向类本身)，操作类变量或实现工厂模式（创建实例)
    - 静态方法  使用`@staticmethod`装饰器，无默认参数，不依赖类或实例状态；执行与类相关的工具函数

### 属性（Property）
> 伪装成字段的方法，通过`property`装饰器实现，用于封装逻辑

### 其他特殊成员
- 魔术方法:如`__init__`(构造函数)、`__str__`(字符串表示)等，用于自定义类等行为
- 私有成员:通过双下划线前缀(如__variable)实现封装，仅在类内部访问

#### 示例
```python
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
"""输出
    10
    这是类的公有方法，value：10
    AttributeError: 'MyClass' object has no attribute '__value'. Did you mean: 'value'?
    AttributeError: 'MyClass' object has no attribute '__private_method'
"""
```
## 综合案例
### 需求
- 设置一个`Game`类
- 属性
    - 定义一个类属性`top_score`记录当前游戏的最高分
    - 定义一个实例属性`player_name`记录当前游戏的玩家姓名
- 方法
    - 静态方法`show_help`显示游戏帮助信息
    - 类方法 `show_top_score` 显示历史最高分
    - 实例方法 `start_game` 开始当前玩家的游戏
- 主程序的步骤
    1. 查看帮助信息
    2. 查看历史最高分
    3. 创建游戏对象，开始游戏

![alt text](class_members.png)

## `isinstance`和`issubclass`
> isinstance(a,b)：判断a是否是b类（或者b类的派生类）实例化的对象
```python
class A:
    pass

class B(A):
    pass

obj = B()

print(isinstance(obj,B))
print(isinstance(obj,A))
```

> issubclass(a,b)： 判断a类是否是b类（或者b的派生类）的派生类
```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(issubclass(B,A))
print(issubclass(C,A))
```

## 总结

| 特性         | 普通方法               | 类方法                 | 静态方法               |
|--------------|------------------------|------------------------|------------------------|
| 定义方式     | 不需要装饰器           | `@classmethod`         | `@staticmethod`        |
| 第一个参数   | `self`                 | `cls`                  | 无                     |
| 访问权限     | 访问实例属性和方法     | 访问类属性和方法       | 无法访问类和实例属性   |
| 调用方式     | 通过实例调用           | 通过类或实例调用       | 通过类或实例调用       |
| 适用场景     | 实例相关操作           | 与类相关的操作         | 与类无关的操作         |