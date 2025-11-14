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
    print("主进程结束，等待子进程...")

