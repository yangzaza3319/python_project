## 一、编程范式对比
### 1. 面向过程编程（Procedural Programming）
核心思想：以步骤和过程为中心，将复杂问题分解为一系列可顺序执行的函数。
核心思想
步骤分解：将问题拆解为多个子任务，每个任务由独立函数实现。
顺序执行：程序按代码书写顺序执行，通过 if、for 等控制流程。
数据与操作分离：数据存在变量中，函数通过参数接收数据并返回结果。
典型特征
模块化函数：如 add(a, b) 实现复用。
线性流程：如 读取 → 处理 → 输出。
高效性：无对象创建开销，适合简单或高性能场景。
✅ 优点：逻辑清晰、执行高效
❌ 缺点：复杂项目中代码臃肿、难以维护

### 2. 面向对象编程（Object-Oriented Programming, OOP）
> 核心思想：以对象为核心，模拟现实世界事物的交互，将数据与操作封装为对象。
#### 核心概念
概念|说明|示例
------|------|------
类（Class）|对象的模板，描述共性特征（属性）和行为（方法）| Car 类含 color 属性和 accelerate() 方法
对象（Object|类的具体实例，拥有独立状态和行为|一辆红色 Car 
封装（Encapsulation）|数据与方法捆绑，仅通过接口交互|银行余额只能通过 deposit() 修改
继承（Inheritance） |子类复用并扩展父类功能 |ElectricCar 继承 Car，新增 charge()
多态（Polymorphism）|同一方法在不同对象中有不同行为| Animal.speak() → 狗“汪汪”，猫“喵喵”
抽象（Abstraction）|提取共性，隐藏实现细节|定义 Shape 抽象类，要求子类实现 area()
#### 核心优势
- 可维护性：对象低耦合，修改局部不影响整体。
- 可扩展性：通过继承/多态灵活新增功能。
- 复用性：类可跨项目复用。
- 逻辑直观：贴近现实世界认知模型。

### 3. 面向过程 vs 面向对象 对比

维度| 面向过程|面向对象
------|--------|--------
核心问题 |“怎么做？” |“谁来做？”
组织方式| 函数 + 数据分离 |对象 = 数据 + 方法
适用场景 |简单任务、脚本、性能敏感 |复杂系统、长期维护项目
代码结构 |线性流程 |职责分工（对象协作）
扩展难度 |需修改多处函数 |新增类/方法即可
#### 总结
面向过程：步骤驱动，适合“一次性”任务。
面向对象：对象驱动，适合“可演化”系统。

## 二、类与对象基础
### 1. 类（Class）
> 是对具有相同特征和行为的事物的抽象统称。
 是模板，不能直接使用。

#### 包含
- 属性（Attributes）：描述特征（如 name, age）
- 方法（Methods）：描述行为（如 run(), eat()）
>  类名命名：大驼峰命名法（CapWords），如 Student, BankAccount
### 2. 对象（Object）
> 是类的具体实例，可直接使用;拥有类中定义的所有属性和方法;不同对象的属性值可以不同
*类似：类 = 飞机图纸，对象 = 制造出的飞机*
### 3. 类与对象的关系
- 先有类，后有对象。
- 一个类 → 多个对象。
- 对象的属性和方法由类决定，不多不少。

## 三、类的设计三要素
设计一个类时，需明确：
1. 类名：从事物或业务中提取，使用大驼峰命名。
2. 属性：这类事物的特征（名词），如 name, height
3. 方法：这类事物的行为（动词），如 run(), eat()

### 示例：
    类名：Human
    属性：name, age, height
    方法：run(), eat()

## 四、类的定义

```python
class Human(object):
"""
定义一个类“人”，人类有思想，并且具备姓名，年龄，身高。人类会吃饭、跑步
"""
mind = "思考中..." # 类属性（所有实例共享）

def __init__(self, name, age, height):
# 初始化方法：通过 self 给对象封装实例属性
self.name = name
self.age = age
self.height = height

def run(self): # 实例方法
print("高高兴兴的跑步")

def eat(self):
print("大口大口的吃饭")
```
> __init__ 是构造方法，创建对象时自动调用。

## 五、对象的实例化
>实例化：通过类创建具体对象的过程。

```python
xiaoming = Human('小明', 18, 173.5)
xiaohong = Human('小红', 20, 165)
```
### 实例化过程发生了什么？
1. 在内存中开辟新对象空间。
2. 自动调用 __init__，并将对象地址传给 self。
3. 在 __init__ 中通过 self 添加实例属性。

## 六、访问对象的属性和方法

``` python
print(xiaoming.name) # 小明（实例属性）
print(xiaoming.mind) # 思考中...（类属性）

xiaoming.run() # 高高兴兴的跑步
xiaohong.eat() # 大口大口的吃饭
```
### 查看对象所有实例属性
```python
print(xiaoming.__dict__)#输出：{'name': '小明', 'age': 18, 'height': 173.5}
```
> __dict__ 不包含类属性和方法。

## 七、从类名角度操作类
### 1. 查看类内容：类名.__dict__
```python
print(Human.__dict__) # 返回类的命名空间字典（包含属性、方法等）
# 通过 类名.__dict__['attr'] = value 只能读，不能改（只读映射）。
```
### 2. 万能的点号 .（推荐方式）
支持对类的属性/方法进行 增、删、改、查：

```python
print(Human.mind) # 思考中...
Human.mind = '高智慧' # 修改类属性
print(Human.mind) # 高智慧

del Human.mind # 删除类属性

Human.walk = lambda self: print("walking...") # 动态添加方法
```
#### 注意
```python
Human.eat = "吞咽" # eat 不再是方法，而是字符串
Human.eat() # ❌ TypeError: 'str' object is not callable
```

## 八、从对象角度操作属性
### 1. 属性类型
实例属性：属于对象独有（如 name, age）
类属性：所有对象共享（如 mind）
### 2. 属性操作（增删改查）
#### 查看
```python
print(xiaoming.name) # 实例属性
print(xiaoming.mind) # 类属性（通过对象访问）
print(xiaoming.__dict__) # 仅实例属性
```
#### 修改
```python
xiaoming.age = 19 # 修改实例属性
注意：这不会修改类属性，而是创建同名实例属性！
xiaoming.mind = "深度思考"
print(xiaoming.mind) # 深度思考（实例属性）
print(Human.mind) # 高智慧（类属性未变）
```
#### 新增（动态绑定）
```python
xiaoming.weight = 65 # 动态添加实例属性
print(xiaoming.weight) # 65
# xiaohong 没有 weight 属性
```
#### 删除
```python
del xiaoming.age
print(xiaoming.age) # ❌ AttributeError
```
### 3. 属性查找顺序（MRO 简化版）
> 当访问 obj.attr 时，Python 按顺序查找：
1. 实例属性（obj.__dict__）
2. 类属性（Class.__dict__）
3. 父类属性（继承链）
4. 未找到 → AttributeError
5. 安全操作属性的内置函数

函数|作用|示例
------ |------ |------
hasattr(obj, 'attr')| 判断是否有属性 |hasattr(xiaoming, 'weight')
getattr(obj, 'attr', default)|获取属性值 |getattr(xiaoming, 'age', 0)
setattr(obj, 'attr', value)|设置属性|setattr(xiaoming, 'score', 90)
delattr(obj, 'attr')|删除属性|delattr(xiaoming, 'score')

## 九、类属性 vs 实例属性 使用建议

场景 |推荐使用
------| --------
所有对象共享的数据（如学校名、计数器）| 类属性
每个对象独有的状态（如姓名、成绩） |实例属性

```python
class Student:
school = "清华大学" # 类属性
count = 0 # 类属性：统计人数

def __init__(self, name):
self.name = name # 实例属性
Student.count += 1 # 修改类属性

s1 = Student("张三")
s2 = Student("李四")
print(Student.count) # 2
```
十、总结：关键要点速记

- 面向过程：步骤驱动，函数+数据分离，适合简单任务。
- 面向对象：对象驱动，封装+继承+多态，适合复杂系统。
- 类是模板，对象是实例。
- 实例属性在 __init__ 中用 self.xxx 定义。
- 类属性在类中直接定义，所有实例共享。
- 对象可通过 . 动态增删改查属性（灵活但需谨慎）。
- 属性查找顺序：实例 → 类 → 父类。
- 使用 hasattr / getattr 安全操作属性。
- 类名用大驼峰命名法（如 BankAccount）。

##  配套案例：校园管理系统（School Management System）
> 模拟一个简单的校园场景，包含 学生（Student） 和 教师（Teacher），两者都继承自 人类（Human） 基类，体现 OOP 核心思想

### 案例目标
1. 展示类与对象的定义与实例化
2. 演示实例属性vs类属性
3. 实现封装（私有属性）
4. 使用继承与方法重写
5. 体现多态的行为
6. 动态操作属性（增删改查）

### 见配套案例