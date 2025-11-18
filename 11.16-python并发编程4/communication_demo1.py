"""
代码示例
communication_demo1.py
"""
from multiprocessing import Queue

q = Queue(3)

q.put('1')
q.put('2')
q.put('3')

try:
    q.put_nowait('4')
except:
    print("队列已经满了")

print(q.get())
print(q.get())
print(q.get())

# print(q.get()) # 此时队列已空，在运行这段代码，会发生阻塞——>解决方法 等待队列中put新数据


try:
    q.get_nowait()
except:
    print("队列已经空了")

print(q.empty())

"""
输出
    队列已经满了
    1
    2
    3
    队列已经空了
True
"""