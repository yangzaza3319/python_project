## 封装
> 将数据和方法捆绑在对象内部，仅通过暴露的接口与外界交互，保护数据安全并简化使用

### 案例解析

#### 第一步将内容封装到类中，并且实例化对象
```python
class Foo:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def detail(self):
        print(self.name)
        print(self.age)
    
obj1 = Foo('xiaohong',18)
obj2 = Foo('xiaoming',16)
```

#### 第二步通过对象调用被封装的内容
```python
class Foo:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def detail(self):
        print(self.name)
        print(self.age)

obj1 = Foo('wuyanzu',38)
obj2 = Foo('liuyifei',18)

# 通过对象直接调用被封装的内容
print(obj1.name)
print(obj2.age)

# 通过self 间接调用被封装的内容
obj1.detail()
obj2.detail()
```

#### 案例一：摆放家具

1. 需求

- 房子(House) 有户型、总面积和家具名称列表
- 家具(HouseItem) 有名字和占地面积，其中
    - 床（bed）占地4平方米
    - 衣柜(chest) 占地2平方米
    - 餐桌(table) 占地1.5平方米
- 将以上三件家具添加到房子中
- 打印房子时，输出（户型、总面积、剩余面积、家具名称列表）

2. 剩余面积
- 在创建房子对象时，定义一个'剩余面积'的属性，'初始值'和'总面积相等'
- 调用`add_item`方法时，向房间'添加家具'时，'剩余面积' -= '家具面积'
> 应该先开发家具类：1️⃣：家具简单；2️⃣：房子要使用到家具，被使用的类，通常应该先开发

##### 创建家具类并且实例化家具对象
```python
class HouseItem:
    def __init__(self,name,area):
        self.name = name
        self.area = area
    def __str__(self):
        return "[%s] 占地面积 %.2f %(self.name,self.area)"
# 创建家具
bed = HouseItem("床",4)
chest = HouseItem("衣柜",2)
table = HouseItem("餐桌",1.5)
print(bed)
print(chest)
print(table)
```

##### 创建房间类并且实例化房间对象
```python
class House:
    def __init__(self,house_type,area):
        self.housetype = house_type
        self.area = area
        self.free_area = area
        self.item_list = []
    
    def  __str__(self):
        return ("户型:%s\n总面积:%.2f[剩余:%.2f]\n家具：%s"
        % (self.house_type,self.area,self.free_area,self.ite_list))
    
    def add_item(self,item):
        print("要添加%s" % item)
my_houme = House("汤臣二品两室一厅"，60)
print(my_home)
```

#### 案例二：士兵突击

1. 需求
- 士兵许三多有一把AK47
- 士兵可以开火
- 枪能够发射子弹
- 枪能够填装子弹

2. 开发枪类
- 发射方法(shoot())需求
    - 判断是否有子弹
    - 使用`print`提示射击，并且输出子弹数量

3. 开发士兵类
- 冲锋方法(fire())需求
    - 判断是否有枪，没有枪没法冲锋
    - 喊一声口号
    - 装填子弹
    - 射击
