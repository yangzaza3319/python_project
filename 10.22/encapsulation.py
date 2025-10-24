# 建家具类并且实例化家具对象

class HouseItem:
    def __init__(self,name,area):
        self.name = name
        self.area = area
    def __str__(self):
        return "[%s] 占地面积 %.2f" % (self.name,self.area)
##  创建家具
bed = HouseItem("床",4)
chest = HouseItem("衣柜",2)
table = HouseItem("餐桌",1.5)
print(bed)     # 输出 [床] 占地面积 4.00
print(chest)   # 输出 [衣柜] 占地面积 2.00
print(table)   # 输出 [餐桌] 占地面积 1.50


# 创建房间类并且实例化房间对象
class House:
    def __init__(self,house_type,area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []
    
    def  __str__(self):
        return ("户型:%s\n总面积:%.2f[剩余:%.2f]\n家具：%s"
        % (self.house_type,self.area,self.free_area,self.item_list))
    
    def add_item(self,item):
        print("要添加%s" % item)
my_home = House("汤臣二品两室一厅",60)
print(my_home)
"""
输出
户型:汤臣二品两室一厅
总面积:60.00[剩余:60.00]
家具：[]
"""

# 在House中完善添加家具的方法

def add_item(self,item):
    print("要添加 %s" % item)
    if item.area > self.free_area:   # 判断家具面积是否大于剩余面积
        print("%s 的面积太大，房间里装不下" %item.name)
        return
    self.item_list.append(item.name)  # 将新家具的名称列表中
    self.free_area -= item.area



# # 完整案例

"""
- 房子(House) 有户型、总面积和家具名称列表
- 家具(HouseItem) 有名字和占地面积，其中
    - 床（bed）占地4平方米
    - 衣柜(chest) 占地2平方米
    - 餐桌(table) 占地1.5平方米
- 将以上三件家具添加到房子中
- 另外添加冰箱发现放不下
- 打印房子时，输出（户型、总面积、剩余面积、家具名称列表）
"""

class HouseItem:
    def __init__(self,name,area):
        self.name = name
        self.area = area
    
    def __str__(self):
        return "[%s] 占地面积 %.2f" %(self.name,self.area)
    
bed = HouseItem("席梦思",10)
chest =  HouseItem("衣柜",20)
table = HouseItem("餐桌",15)
fridge = HouseItem("冰箱",15)

class House:
    def __init__(self,house_type,area):
        self.area = area
        self.item_list=[]
        self.house_type = house_type
        self.free_area = area

    def __str__(self):
        return ("户型:%s\n；总面积为：%.2f[剩余%.2f]\n;家具:%s" % (self.house_type,self.area,self.free_area,self.item_list))
    
    def add_item(self,item):
        print("要添加%s" % item)
        if item.area > self.free_area:
            print("%s 的面积太大，不能添加到房子中！" % item.name)
            return 
        self.item_list.append(item)
        self.free_area -= item.area

my_home = House("碧根果园两室一厅",50)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
my_home.add_item(fridge)

print(my_home)

"""
输出
要添加[席梦思] 占地面积 10.00
要添加[衣柜] 占地面积 20.00
要添加[餐桌] 占地面积 15.00
要添加[冰箱] 占地面积 15.00
冰箱 的面积太大，不能添加到房子中！
户型:碧根果园两室一厅
；总面积为：50.00[剩余5.00]
;家具:[<__main__.HouseItem object at 0x101535160>, <__main__.HouseItem object at 0x10142e210>, <__main__.HouseItem object at 0x10142f390>]
"""


# 案例二：士兵突击
"""
需求
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
"""
# # 定义枪类
class Gun:
    def __init__(self, model):
        self.module = model          # 注意：这里你写的是 module，但通常应为 model（拼写问题，不影响运行）
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count
    
    def shoot(self):
        if self.bullet_count <= 0:
            print("没子弹了....")
            return
        self.bullet_count -= 1  # 修正：原来是 self.bullet，应为 self.bullet_count
        print("%s 发射子弹[%d]...突突突" % (self.module, self.bullet_count))


# 创建枪对象
ak47 = Gun("ak47")
ak47.add_bullet(50)
ak47.shoot()  # 这里会输出：ak47 发射子弹[49]...突突突


# 定义士兵类
class Soldier:
    def __init__(self, name, gun=None):
        self.name = name
        self.gun = gun
    
    def fire(self):
        if self.gun is None:
            print("[%s]还没发枪..." % self.name)
        else:
            print("[%s]冲锋！！！" % self.name)
            if self.gun.bullet_count <= 0:
                print("没子弹了,快换弹夹")
                self.gun.add_bullet(50)
            self.gun.shoot()  # 注意：无论是否加子弹，最后都要射击一次


# 测试
xiaowenhao = Soldier("xiaowenhao", ak47)
xiaowenhao.fire()