# 多态引入案例
class Human(object):
    def work(self):
        return "喝杯咖啡，开始工作"
    
class IT(Human):
    def work(self):
        return "开始码代码"

class Designer(Human):
    def work(self):
        return "开始美工"

def job(person):
    print(person.work())
ps = Designer()
it = IT()

job(ps)
job(it)
"""
输出
开始美工
开始码代码
"""


# 哮天犬案例
class Dog(object):
    def __init__(self,name):
        self.name = name
    def dog_play(self):
        print("%s 蹦蹦跳跳的玩耍..." % (self.name))    
class Xiaotianquan(Dog):
    def dog_play(self):
        print("%s 飞到天上去玩耍..." % (self.name) )
        
class Human():
    def __init__(self,name):
        self.name = name

    def dog_play(self,dog):
        print("%s和%s 在快乐的玩耍" %(self.name,dog.name))
        dog.dog_play()
wangcai = Dog("旺财")
xiaotianquan = Xiaotianquan("飞天旺财")
xiaoming = Human("小明")
xiaoming.dog_play(wangcai)
xiaoming.dog_play(xiaotianquan)
"""
输出
小明和旺财 在快乐的玩耍
旺财 蹦蹦跳跳的玩耍...
小明和飞天旺财 在快乐的玩耍
飞天旺财 飞到天上去玩耍...
"""
