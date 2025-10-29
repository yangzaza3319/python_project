# 基本鸭子类型
class Duck:
    def quark(self):
        print("嘎嘎")
class Dog:
    def quark(self):
        print("汪汪(假装嘎嘎)")
class RobotDuck:
    def quark(self):
        print("滴滴，我是机器鸭")

def make_it_quark(obj):
    obj.quark()

make_it_quark(Duck())
make_it_quark(RobotDuck())
make_it_quark(Dog())
"""
make_it_quack 完全不在乎传入对象的类型，只要它有 .quack() 方法。
输出
    嘎嘎
    滴滴，我是机器鸭
    汪汪(假装嘎嘎)
"""

# 文件操作中的鸭子类型

def save_data(file_obj):
    file_obj.write("hello,i love python")
with open("duck.txt","w") as f:
    save_data(f)

from io import StringIO  
s = StringIO()
save_data(s)
print(s.getvalue)

"""
运行结果：把需要的字符串写入了duck.txt,并且输出<built-in method getvalue of _io.StringIO object at 0x101b610c0>
"""

# 迭代器协议
class Countdown:
    def __init__(self,n):
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.n < 0:
            raise StopIteration
        self.n -= 1
        return self.n +1
for x in Countdown(3):
    print(x)
"""
输出
    3
    2
    1
    0
"""
