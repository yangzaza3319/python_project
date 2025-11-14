"""
直接创建父进程和子进程
"""
from multiprocessing import Process

def func(name):
    print("hello %s" % name)
    print("子进程结束")
if __name__ == '__main__':
    p = Process(target=func,args=('niuniu',))
    p.start()
    print("主进程结束")