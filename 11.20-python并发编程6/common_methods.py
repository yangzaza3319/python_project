from threading import Thread
import threading
from multiprocessing import Process
import os,time


def work():
    time.sleep(3)
    print(threading.current_thread().name)


if __name__ == '__main__':
    t = Thread(target=work)
    t.start()

    print(threading.current_thread().name)
    print(threading.current_thread())
    print(threading.enumerate())
    print(threading.active_count())

    t.join()
    print("主线程/主进程")
    print(t.is_alive())

"""
输出
    MainThread
    <_MainThread(MainThread, started 8767971456)>
    [<_MainThread(MainThread, started 8767971456)>, <Thread(Thread-1 (work), started 6117076992)>]
    2
    Thread-1 (work)
    主线程/主进程
    False
"""
