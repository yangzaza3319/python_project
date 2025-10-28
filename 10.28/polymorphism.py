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