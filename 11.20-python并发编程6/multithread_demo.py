import threading
import time,os


def task(name,delay):
    print(f"当前线程ID（Python标识符）:{threading.get_ident()}")
    print(f"线程对象标识符:{threading.current_thread().ident}")

    print(f"{name}-{os.getpid()} 开始执行")
    time.sleep(delay)
    print(f"{name}-{os.getpid()} 执行完毕")

if __name__ == '__main__':
    threads = [threading.Thread(target=task,args=(f"线程{i}",2)) for i in range(10)]
    for i in threads:
        i.start()
    for i in threads:
        i.join()
    print("主线程/主线程PID",os.getpid())

"""
输出
    当前线程ID（Python标识符）:6147387392
    线程对象标识符:6147387392
    线程0-8403 开始执行
    当前线程ID（Python标识符）:6164213760
    线程对象标识符:6164213760
    线程1-8403 开始执行
    当前线程ID（Python标识符）:6181040128
    线程对象标识符:6181040128
    线程2-8403 开始执行
    当前线程ID（Python标识符）:6197866496
    线程对象标识符:6197866496
    线程3-8403 开始执行
    当前线程ID（Python标识符）:6214692864
    线程对象标识符:6214692864
    线程4-8403 开始执行
    当前线程ID（Python标识符）:6231519232
    线程对象标识符:6231519232
    线程5-8403 开始执行
    当前线程ID（Python标识符）:6248345600
    线程对象标识符:6248345600
    线程6-8403 开始执行
    当前线程ID（Python标识符）:6265171968
    线程对象标识符:6265171968
    线程7-8403 开始执行
    当前线程ID（Python标识符）:6281998336
    线程对象标识符:6281998336
    线程8-8403 开始执行
    当前线程ID（Python标识符）:6298824704
    线程对象标识符:6298824704
    线程9-8403 开始执行
    线程1-8403 执行完毕
    线程0-8403 执行完毕
    线程5-8403 执行完毕
    线程8-8403 执行完毕
    线程2-8403 执行完毕
    线程6-8403 执行完毕
    线程7-8403 执行完毕线程3-8403 执行完毕
    
    线程9-8403 执行完毕
    线程4-8403 执行完毕
    主线程/主线程PID 8403
"""
