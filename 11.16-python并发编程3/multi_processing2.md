## 进程间数据共享
> 在python中，由于进程键内存空间相互独立，直接共享数据需借助特定机制

```python
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
```

## 原生共享内存方案(Value/Array)
> 适合共享简单整数类型（如整数、浮点数）或数组。通过底层共享内存实现，无需复制数据，性能较高

```python
# data_share_demo.py
"""
原生共享内存方案（Value/Array）
"""
from  multiprocessing import Process,Value,Array

def increment(num):
    num.value += 1

if __name__ == '__main__':
    counter = Value('i',0)
    arr = Array('d',[0.0,1.0,2.0])
    processes = [Process(target=increment,args=(counter,)) for _ in range(5)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print(counter.value)
"""
输出 
    3
"""
```

## 进程同步机制
> 共享数据时需要通过锁（Lock）、信号量（Semaphore）等保证数据一致性

```python
"""
process_lock_and_seg.py
"""
from multiprocessing import Process,Value,Lock

def safe_increment(num,lock):
    with lock:
        num.value += 1
    
if __name__ == "__main__":
    counter = Value("i",0)
    lock = Lock()

    processes = [Process(target=safe_increment,args=(counter,lock)) for _ in range(5)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print(counter.value)

"""
输出
    5
"""
```

## Manager 代理对象方案
适合复杂的数据结构（如列表、字典）。通过代理模式，由Manager服务进程管理数据，子进程通过代理访问
Manager提供了一种方式来创建多个进程之间共享的对象。Manager允许不同的进程通过通过代理对象来共享数据结构，包括列表、字典、命名空间等，而无需显式的进程间通信机制(如队列或者管道)。Manager实现了进程间的同步机制，确保多个进程可以安全的读写共享数据
multiprocessing.Manager提供了一个管理器对象，这个管理器可以生成各种共享对象，如列表、字典、队列、锁等。所有这些对象都可以被不同的进程安全的访问和修改

### 共享对象类型
- list：共享的列表
- dict：共享的字典
- Namespace：共享的命名空间，允许存储任意属性
- Queue：共享的队列，用于进程间通信
- Lock：锁，用于进程同步，防止数据竞争

### 基本使用流程
1. 从`multiprocessing.Manager()`创建管理器对象
2. 使用管理器对象来创建和共享数据结构（如list、dict等）
3. 在多个进程中共享这些数据结构
4. 进程完成后，关闭管理器对象

```python
"""
manager 代理对象
"""
from multiprocessing import Manager,Process

def update_dict(shared_dict,key):
    shared_dict[key] = key * 2

if __name__ == '__main__':
    with Manager() as manager:
        shared_dict = manager.dict()
        processes = [Process(target=update_dict,args=(shared_dict,i))for i in range(3)]
        for p in processes:
            p.start()
        for p in processes:
            p.join()
        print(shared_dict)

"""
输出
    {1: 2, 0: 0, 2: 4}
"""
```