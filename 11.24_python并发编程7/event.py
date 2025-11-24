import threading
import time

event = threading.Event()

def waiter():
    print("等待事件触发")
    event.wait()
    print("事件已触发")

def setter():
    time.sleep(2)
    event.set()
    print("事件已设置！")

t1 = threading.Thread(target=waiter)
t2 = threading.Thread(target=setter)

t1.start()
t2.start()

t1.join()
t2.join()

print("程序结束")

"""
输出
    等待事件触发
    事件已设置！
    事件已触发
    程序结束
"""