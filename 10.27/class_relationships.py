# 依赖关系案例：人把大象装进冰箱 (对大象类和冰箱类进行依赖)

class Elephant:
    def __init__(self, name):
        self.name = name

    def enter(self):  
        print(f"{self.name}进了冰箱～")


class Refrigerator:  
    def __init__(self, name):
        self.door_open = False
        self.name = name

    def open_door(self):
        self.door_open = True
        print(f"{self.name}冰箱门打开了")

    def close_door(self):
        self.door_open = False
        print(f"{self.name}冰箱门关上了")


class Person:
    def put_elephant(self, elephant: Elephant, fridge: Refrigerator):
        fridge.open_door()
        elephant.enter()  
        fridge.close_door()


if __name__ == "__main__":
    elephant = Elephant("小飞象")
    fridge = Refrigerator("卡萨帝冰箱")
    person = Person()
    person.put_elephant(elephant, fridge)


"""
输出
卡萨帝冰箱冰箱门打开了
小飞象进了冰箱～
卡萨帝冰箱冰箱门关上了
"""


# 关联关系
class Boy:
    def __init__(self,name,girlfriend = None):
        self.name = name
        self.girlfriend = girlfriend
    
    def date(self):
        if self.girlfriend:
            print('%s 和 %s 一起共进晚餐' % (self.name,self.girlfriend.name))
        else:
            print("%s还不赶紧找个对象" % (self.name))

class Girl:
    def __init__(self,name):
        self.name =name

boy1 = Boy("西格玛男人")
boy1.date()

girl = Girl("恋爱脑")

boy2 = Boy("渣男",girl)
boy2.date()


"""
输出
西格玛男人还不赶紧找个对象
渣男 和 恋爱脑 一起共进晚餐
"""

# 典型关联关系案例
## 1. 单向关联(从老师查学校)
class School:
    def __init__(self,name):
        self.name = name

class Teacher:
    def __init__(self,name,school:School):
        self.name = name
        self.school = school
## 2. 双向关联

class School:
    def __init__(self,name):
        self.name = name
        self.teachers = []
    def add_teacher(self,teacher):
        if teacher not in self.teachers:
            self.teachers.append(teacher)
            teacher.school = self 
class Teacher:
    def __init__(self,name,school=None):
        self.name = name
        self.school = school

school = School("清华")
teacher = Teacher("钟老师")
school.add_teacher(teacher) # 自动设置双向关系

# 组合案例
## 设计一个游戏，让游戏里面的人物互殴，加上一个武器类，让人使用武器攻击

class Gamerole:
    def __init__(self,name,ad,hp,wea=None):
        self.name = name
        self.ad = ad
        self.hp = hp 
        self.wea = wea

    def attack(self,p1):
        p1.hp -= self.ad
        print('%s 攻击了 %s,%s掉了%s血，还剩%s'%(self.name,p1.name,self.ad,p1.hp))
    
    def equip_weapon(self,wea):
        self.wea = wea
        wea.ad += self.ad
        wea.owner_name = self.name

class Weapon:
    def __init__(self,name,ad,owner_name = None):
        self.name = name
        self.owner_name = owner_name
        self.ad = ad

    def weapon_attack(self,p2):
        p2.hp = p2.hp - self.ad
        print('%s利用%s攻击了%s,%s还剩%s血'%(self.owner_name,self.name,p2.name,p2.name,p2.hp))
    
man = Gamerole('人',10,100)
dog = Gamerole('狗',50,100)
stick = Weapon('木棍',40)

man.equip_weapon(stick)
man.wea.weapon_attack(dog)

"""
输出 
人利用木棍攻击了狗,狗还剩50血
"""

import time
import random

class Gamerole:
    def __init__(self,name,ad,hp):
        self.name = name
        self.ad = ad
        self.hp = hp
    
    def attack(self,p1):
        p1.hp -= self.ad
        print('%s攻击%s,%s掉了%s血，还剩%s' %(self.name,p1.name,p1.name,self.ad,p1.hp))

    def equip_weapon(self,wea):
        self.wea = wea
        wea.ad += self.ad
        wea.owner_name = self.name
    
class Weapon:
    def __init__(self,name,ad,owner_name = None):
        self.name = name
        self.owner_name = owner_name
        self.ad = ad
    def weapon_attack(self,p2):
        p2.hp = p2.hp -self.ad
        print('%s 利用 %s 攻击了 %s ,%s 还剩 %s血'%(self.owner_name,self.name,p2.name,p2.name,p2.hp))

sunwukong = Gamerole("孙悟空",20,500)
caocao = Gamerole("曹操",20,100)
anqila = Gamerole("安琪拉",50,80)

zhaoyun = Gamerole("赵云",30,450)
guanyu = Gamerole("关羽",80,200)
diaochan = Gamerole("貂蝉",60,150)

blue_list = [sunwukong,caocao,anqila]
red_list = [zhaoyun,guanyu,diaochan]

if __name__ == '__main__':
    print("游戏开始加载")

    for i in range(0,101,2):
        time.sleep(0.1)
        char_num = i // 2
        per_str = '\r%s%s : %s\n' %(i,'*' &char_num) \
            if i == 100 else '\r%s%s:%s'%(i,'*'*char_num)
        print(per_str,end='',flush=True)
    
    info = input("游戏加载完毕,如入任意字符开始")
    print("蓝方阵营".center(20,'*'))
    for i in blue_list:
        print(i.name.center(20))
    
    while True:
        if len(blue_list) == 0:
            print("红色方胜利")
            break
        if len(red_list) == 0:
            print("蓝色方胜利")
            break
        
        index1 = random.randint(0,len(blue_list) - 1)
        index2 = random.randint(0,len(red_list) - 1)

        time.sleep(1)
        role1 = blue_list[index1]
        time.sleep(1)
        role2 = red_list[index2]
        time.sleep(1)
        role1.attack(role2)
        role2.attack(role1)

        if role1.hp<= 0:
            print("%s阵亡"% role1.name)
            blue_list.remove(role1)
        if role2.hp <= 0:
            print("%s阵亡" %role2.name)
            red_list.remove(role2)