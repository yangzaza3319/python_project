from multiprocessing import Process
import time

def func(name):
    print("hello %s" %name)
    time.sleep(1)
    print("子进程结束")

if __name__ == "__main__":
    for i in range(5):
        p = Process(target=func,args=('niuniu',))
        p.start()
        p.join()
    print("所有子进程已完成，主进程结束")
"""
输出 
    hello niuniu
    子进程结束
    hello niuniu
    子进程结束
    hello niuniu
    子进程结束
    hello niuniu
    子进程结束
    hello niuniu
    子进程结束
    所有子进程已完成，主进程结束
"""