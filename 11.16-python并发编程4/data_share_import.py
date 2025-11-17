"""
进程间数据共享
"""
from multiprocessing import Process
import os

count = 0

def increment():
    global count
    count += 1
    print(f"子进程{os.getpid()}修改后的count:{count}")

if __name__=="__main__":
    p1 = Process(target=increment)
    p2 = Process(target=increment)

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print(f"主进程中的 count:{count}")
"""
输出
    子进程59011修改后的count:1
    子进程59012修改后的count:1
    主进程中的 count:0
"""