## 进程间通信

> IPC（Inter_Process Communication）
> 在计算机系统中，进程是操作系统分配资源的最小单位，每个进程拥有独立的内存空间和资源
> 由于进程间的内存隔离，进程间通信成为实现多进程协作的关键技术

> 队列和管道都是将数据存放于内存中，队列又是基于（管道+锁）实现的，可以让我们从复杂的锁问题中解脱出来，我们应该尽量避免使用共享数据，尽可能使用消息传递和队列，避免处理复杂的同步和锁问题，而且在进程数目增多时，往往可以获得更好的可扩展性

### 管道
> 点对点通信，返回两个连接对象

```python
from multiprocessing import Pipe

conn1,conn2 = Pipe()
conn1.send("hello")
print(conn2.recv())

"""
输出 
    hello
"""
```

### 队列
> 安全传递数据，支持多生产者和消费者

```python
# 伪代码
from multiprocessing import Queue
q = Queue([maxsize])
```

#### 常见方法

方法|含义
---|---
q.get(block=True,timeout=(None))|返回q中的一个项目。如果q为空，此方法将阻塞，直到队列中有项目可用为止。block用于控制阻塞行为，默认为True. 如果设置为False，将引发Queue.Empty异常（定义在Queue模块中）。timeout是可选超时时间，用在阻塞模式中。如果在制定的时间间隔内没有项目变为可用，将引发Queue.Empty异常。
q.get_nowait()|同q.get(False)方法
q.put(obj,block=True,timeout=None)|将obj放入队列。如果队列已满，此方法将阻塞至有空间可用为止。black控制阻塞行为，默认为True。如果设置为False，将引发Queue.Empty异常（定义在Queue库模块中）。timeout指定在阻塞模式中等待可用空间的时间长短，超时后将引起Queue.Full异常
q.qsize()|返回队列中目前项目的正确数量。此函数的结果并不可靠，因为在返回结果和在稍后程序中使用结果之间，队列中可能添加或删除了项目。在某些系统上，此方法可能引发NotImplementedError异常。
q.empty()|如果调用此方法时q为空，返回True；如果其他进程或线程正在往队列中添加项目，结果是不可靠的；也就是说，在返回和使用结果之间，队列中可能已经加入了新的项目
q.full()|如果q已满，返回值为True；由于线程的存在，结果也有可能是不可靠的（参考q.empty()）方法
q.close()|关闭队列，防止队列中加入更多数据。调用此方法时，后台线程将继续写入那些已入队列但尚未写入的数据，但将此方法完成时马上关闭。如果q被垃圾收集，将自动调用该方法。关闭队列不会在队列使用者中生成任何类型的数据结束信号或异常。例如，如果某个使用者正在被阻塞在get（）操作上，关闭生产者中的队列不会导致get（）方法返回错误
q.cancel_join_thread()|不会在进程退出时自动连接后台线程，这可以防止join_thread()方法阻塞
q.join_thread()| 连接队列的后台进程，此方法用于在调用q.close()方法后，等待所有队列项被消耗。默认情况下，此方法不是q的原始创建者的所有进程调用。调用q.cancel_join_thread()方法可以禁止这种行为

#### 代码案例
```python
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
```
#### 案例分析1
> 定义两个进程，一个用于生产数据，一个用于消费数据，使用队列进行数据交换

```python
"""
案例1
# communication_demo2.py
"""
from  multiprocessing import  Process,Queue

import time

def func_put(q):
    for i in range(3):
        q.put(f"数据{i+1}")

def func_get(q):
    time.sleep(1)
    while True:
        try:
            print(f"GET到数据：{q.get_nowait()}")
        except Exception:
            print("数据已经被全部拿完了")
            break


if __name__ == "__main__":
    q = Queue()
    p_put =Process(target=func_put,args=(q,))
    p_get =Process(target=func_get,args=(q,))
    p_put.start()
    p_put.join()

    p_get.start()
    p_get.join()

"""
输出
    GET到数据：数据1
    GET到数据：数据2
    GET到数据：数据3
    数据已经被全部拿完了
"""
```


#### 案例分析2
> 多个进程通过计算并通过队列返回结果

```python
import multiprocessing
import time

def calculate_square(num,queue):
    result = num * num
    print(
        f"进程{multiprocessing.current_process().name }计算 {num} 的平方,结果是{result}"
    )
    time.sleep(1)
    queue.put(result)

if __name__=="__main__":
    numbers = [1,2,3,4,5]
    queue = multiprocessing.Queue()
    processes = []

    for num in numbers:
        p = multiprocessing.Process(target=calculate_square,args=(num,queue))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
    
    results = []

    while not queue.empty():
        results.append(queue.get())

    print(f"所有进程计算结果:{results}")
    print("主进程结束")

"""
输出 
    进程Process-1计算 1 的平方,结果是1
    进程Process-2计算 2 的平方,结果是4
    进程Process-5计算 5 的平方,结果是25
    进程Process-4计算 4 的平方,结果是16
    进程Process-3计算 3 的平方,结果是9
    所有进程计算结果:[1, 4, 16, 25, 9]
    主进程结束
"""
```

#### 生产者消费者模型
> 在并发编程中使用生产者消费者模型能够解决大多数并发问题。该模式通过平衡生产线程和消费线程的工作能力来提高整体程序处理数据的速度

##### 生产者消费者模型的好处
在线程世界里，生产者就是生产数据的线程，消费者就是消费数据的线程
在多线程开发中，如果生产者处理速度很快，而消费者处理速度很慢，生产者必须等消费者处理完，才能继续生产数据；同理，如果消费者的处理能力大于生产者，消费者必须等生产者；为了解决这个问题而引入生产者消费者模型

##### 什么是生产者消费者模型
生产者消费者模式是通过一个容器来解决生产者和消费者的强耦合问题
生产者和消费者彼此之间不直接通讯，而通过阻塞队列来进行通讯，所以生产者生产完数据之后不用等消费者处理，直接塞给阻塞队列，消费者不着生产者要数据，而是直接从阻塞队列里面取，阻塞队列就相当于一个缓冲区，平衡消费者和生产者的处理能力

##### 示例代码
```python
from  multiprocessing import Process,Queue,current_process
import time,random,os

def consumer(q):
    while True:
        res = q.get()
        if res is None:
            break
        time.sleep(random.randint(1,3))
        print(f"进程{current_process().name}吃{res}")

def producer(q):
    for i in range(10):
        time.sleep(random.randint(1,3))
        res = f"包子{i}"
        q.put(res)
        print(f"进程{current_process().name}生产了{res}")

if __name__=="__main__":
    q = Queue()

    producers = [Process(target=producer,args=(q,))for _ in range(1)]
    consumers = [Process(target=consumer,args=(q,))for _ in range(10)]

    for p in producers+consumers:
        p.start()
    
    for p in producers:
        p.join()
    
    for _ in range(len(consumers)):
        q.put(None)
    
    for c in consumers:
        c.join()

"""
输出
消费者进程随机出现，因为
    进程Process-1生产了包子0
    进程Process-1生产了包子1
    进程Process-1生产了包子2
    进程Process-4吃包子1
    进程Process-7吃包子0
    进程Process-1生产了包子3
    进程Process-5吃包子2
    进程Process-10吃包子3
    进程Process-1生产了包子4
    进程Process-1生产了包子5
    进程Process-3吃包子4
    进程Process-8吃包子5
    进程Process-1生产了包子6
    进程Process-1生产了包子7
    进程Process-1生产了包子8
    进程Process-11吃包子6
    进程Process-9吃包子7
    进程Process-1生产了包子9
    进程Process-6吃包子8
    进程Process-2吃包子9
"""
```

#### JoinableQueue([maxsize])
> 创建可连接的共享进程队列。这就是一个Queue对象，但队列允许项目的使用者通知生产者项目已经被成功处理。通知进程是使用共享的信号和条件变量实现的

方法|含义
---|---
q.task_done()|消费者使用此方法发出信号，表示q.get()返回的结果已经被处理。如果调用此方法的次数大于从队列中删除的结果数量。将引发ValueError异常
q.join()|生产者将使用此方法进行阻塞，直到队列中所有项目均被处理。阻塞将持续到为队列中的每个项目均调用q.task_done()方法为止


##### 代码案例
```python
from multiprocessing import Process,JoinableQueue,current_process
import random,time

def consumer(q):
    while True:
        res = q.get()
        time.sleep(random.randint(1,3))
        print(f"进程{current_process().name} 吃了 {res}")
        q.task_done()

def prodecer(q):
    for i in range(10):
        time.sleep(random.randint(1,3))
        res = f"{i}号包子"
        q.put(res)
        print(f"进程{current_process().name}生产了{res}")
    q.join()

if __name__== "__main__" :
    q = JoinableQueue()

    prodecers = [Process(target=prodecer,args=(q,)) for _ in range(1)]
    consumers = [Process(target=consumer,args=(q,),daemon=True) for _ in range(10)]

    for p in prodecers+consumers:
        p.start()
    
    for p in prodecers:
        p.join()
    

    print("所有队列处理完成，程序退出")

"""
输出
    进程Process-4 吃了 2号包子
    进程Process-1生产了3号包子
    进程Process-2 吃了 3号包子
    进程Process-1生产了4号包子
    进程Process-8 吃了 4号包子
    进程Process-1生产了5号包子
    进程Process-9 吃了 5号包子
    进程Process-1生产了6号包子
    进程Process-1生产了7号包子
    进程Process-10 吃了 6号包子
    进程Process-7 吃了 7号包子
    进程Process-1生产了8号包子
    进程Process-6 吃了 8号包子
    进程Process-1生产了9号包子
    进程Process-11 吃了 9号包子
    所有队列处理完成，程序退出
"""
```