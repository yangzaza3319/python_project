"""
通过继承类创建子进程
"""

import os
from multiprocessing import Process

class MyProcess(Process):
    def __init__(self,name):
        super().__init__()
        self.name = name
    
    def run(self):
        print(os.getpid())
        print('%s正在和女主播聊天'%self.name)

if __name__ == '__main__':
    p1 = MyProcess('张三')
    p1.start()
    print('主进程结束')