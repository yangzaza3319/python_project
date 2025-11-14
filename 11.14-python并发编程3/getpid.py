import os
from multiprocessing import Process

def func():
    print('子进程id:',os.getpid(),'父进程id:',os.getppid())
    print("子进程结束")

if __name__=="__main__":
    p = Process(target=func,args=())
    p.start()
    print("主进程id:",os.getpid())
    print("主进程结束，等待子进程结束中...")
"""
输出
    主进程id: 48464
    主进程结束，等待子进程结束中...
    子进程id: 48466 父进程id: 48464
    子进程结束
"""

