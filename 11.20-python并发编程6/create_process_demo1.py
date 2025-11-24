from threading import Thread
import time

def task(name,delay):
    print(f"{name}开始执行")
    time.sleep(delay)
    print(f"{name}执行完毕")

if __name__ == '__main__':
    t1 = Thread(target=task,args=("线程A",2))
    t1.start()
    t1.join()

"""
输出
    线程A开始执行
    线程A执行完毕
"""