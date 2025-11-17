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
q.get(block=True,timeout=(None))|
返回q中的一个项目。如果q为空，此方法将阻塞，直到队列中有项目可用为止。block用于控制阻塞行为，默认为True. 如果设置为False，将引发Queue.Empty异常（定义在Queue模块中）。timeout是可选超时时间，用在阻塞模式中。如果在制定的时间间隔内没有项目变为可用，将引发Queue.Empty异常。
q.get_nowait()|同q.get(False)方法
q.put(obj,block=True,timeout=None)|
将obj放入队列。如果队列已满，此方法将阻塞至有空间可用为止。black控制阻塞行为，默认为True。如果设置为False，将引发Queue.Empty异常（定义在Queue库模块中）。timeout指定在阻塞模式中等待可用空间的时间长短，超时后将引起Queue.Full异常
q.qsize()|
返回队列中目前项目的正确数量。此函数的结果并不可靠，因为在返回结果和在稍后程序中使用结果之间，队列中可能添加或删除了项目。在某些系统上，此方法可能引发NotImplementedError异常。
q.empty()|
如果调用此方法时q为空，返回True；如果其他进程或线程正在往队列中添加项目，结果是不可靠的；也就是说，在返回和使用结果之间，队列中可能已经加入了新的项目
q.full()|
如果q已满，返回值为True；由于线程的存在，结果也有可能是不可靠的（参考q.empty()）方法
q.close()|
关闭队列，防止队列中加入更多数据。调用此方法时，后台线程将继续写入那些已入队列但尚未写入的数据，但将此方法完成时马上关闭。如果q被垃圾收集，将自动调用该方法。关闭队列不会在队列使用者中生成任何类型的数据结束信号或异常。例如，如果某个使用者正在被阻塞在get（）操作上，关闭生产者中的队列不会导致get（）方法返回错误
q.cancel_join_thread()|不会在进程退出时自动连接后台线程，这可以防止join_thread()方法阻塞
q.join_thread()| 连接队列的后台进程，此方法用于在调用q.close()方法后，等待所有队列项被消耗。默认情况下，此方法不是q的原始创建者的所有进程调用。调用q.cancel_join_thread()方法可以禁止这种行为

#### 代码案例
```python

```