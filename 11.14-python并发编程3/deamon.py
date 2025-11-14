# deamon.py

from multiprocessing import Process
import time

def worker():
    print("守护进程正在工作...")
    n = 0
    while True:
        print(f"  工作循环 {n}")
        n += 1
        time.sleep(0.5)

if __name__ == '__main__':
    p = Process(target=worker)
    p.daemon = True
    p.start()
    
    print("主进程睡眠 2 秒...")
    time.sleep(2)
    print("主进程结束！")  # 此时守护进程会被强制终止

"""
输出 
    主进程睡眠 2 秒...
    守护进程正在工作...
    工作循环 0
    工作循环 1
    工作循环 2
    工作循环 3
    主进程结束！
"""