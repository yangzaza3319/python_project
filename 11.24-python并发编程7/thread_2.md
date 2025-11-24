## 线程同步机制
### 互斥锁
> 保证同一时刻只有一个线程能访问共享资源，防止数据竞争
```python
import threading
import time

def increment():
    global shared_counter
    with lock:
        tmp = shared_counter + 1
        time.sleep(0.1)  # 模拟耗时操作
        shared_counter = tmp
        # 打印当前线程名和更新后的值
        print(f"线程 {threading.current_thread().name}: 更新数值到 {shared_counter}")

if __name__ == "__main__":
    shared_counter = 0
    lock = threading.Lock()

    # 创建100个线程
    threads = [threading.Thread(target=increment, name=f"T{i+1}") for i in range(100)]

    # 启动所有线程
    for t in threads:
        t.start()

    # 等待所有线程完成
    for t in threads:
        t.join()

    print(f"最终的数值: {shared_counter}")

"""
输出
    线程 T1: 更新数值到 1
    线程 T2: 更新数值到 2
    线程 T3: 更新数值到 3
    线程 T4: 更新数值到 4
    线程 T5: 更新数值到 5
    线程 T6: 更新数值到 6
    线程 T7: 更新数值到 7
    线程 T8: 更新数值到 8
    线程 T9: 更新数值到 9
    线程 T10: 更新数值到 10
    线程 T11: 更新数值到 11
    线程 T12: 更新数值到 12
    线程 T13: 更新数值到 13
    线程 T14: 更新数值到 14
    线程 T15: 更新数值到 15
    线程 T16: 更新数值到 16
    线程 T17: 更新数值到 17
    线程 T18: 更新数值到 18
    线程 T19: 更新数值到 19
    线程 T20: 更新数值到 20
    线程 T21: 更新数值到 21
    线程 T22: 更新数值到 22
    线程 T23: 更新数值到 23
    线程 T24: 更新数值到 24
    线程 T25: 更新数值到 25
    线程 T26: 更新数值到 26
    线程 T27: 更新数值到 27
    线程 T28: 更新数值到 28
    线程 T29: 更新数值到 29
    线程 T30: 更新数值到 30
    线程 T31: 更新数值到 31
    线程 T32: 更新数值到 32
    线程 T33: 更新数值到 33
    线程 T34: 更新数值到 34
    线程 T35: 更新数值到 35
    线程 T36: 更新数值到 36
    线程 T37: 更新数值到 37
    线程 T38: 更新数值到 38
    线程 T39: 更新数值到 39
    线程 T40: 更新数值到 40
    线程 T41: 更新数值到 41
    线程 T42: 更新数值到 42
    线程 T43: 更新数值到 43
    线程 T44: 更新数值到 44
    线程 T45: 更新数值到 45
    线程 T46: 更新数值到 46
    线程 T47: 更新数值到 47
    线程 T48: 更新数值到 48
    线程 T49: 更新数值到 49
    线程 T50: 更新数值到 50
    线程 T51: 更新数值到 51
    线程 T52: 更新数值到 52
    线程 T53: 更新数值到 53
    线程 T54: 更新数值到 54
    线程 T55: 更新数值到 55
    线程 T56: 更新数值到 56
    线程 T57: 更新数值到 57
    线程 T58: 更新数值到 58
    线程 T59: 更新数值到 59
    线程 T60: 更新数值到 60
    线程 T61: 更新数值到 61
    线程 T62: 更新数值到 62
    线程 T63: 更新数值到 63
    线程 T64: 更新数值到 64
    线程 T65: 更新数值到 65
    线程 T66: 更新数值到 66
    线程 T67: 更新数值到 67
    线程 T68: 更新数值到 68
    线程 T69: 更新数值到 69
    线程 T70: 更新数值到 70
    线程 T71: 更新数值到 71
    线程 T72: 更新数值到 72
    线程 T73: 更新数值到 73
    线程 T74: 更新数值到 74
    线程 T75: 更新数值到 75
    线程 T76: 更新数值到 76
    线程 T77: 更新数值到 77
    线程 T78: 更新数值到 78
    线程 T79: 更新数值到 79
    线程 T80: 更新数值到 80
    线程 T81: 更新数值到 81
    线程 T82: 更新数值到 82
    线程 T83: 更新数值到 83
    线程 T84: 更新数值到 84
    线程 T85: 更新数值到 85
    线程 T86: 更新数值到 86
    线程 T87: 更新数值到 87
    线程 T88: 更新数值到 88
    线程 T89: 更新数值到 89
    线程 T90: 更新数值到 90
    线程 T91: 更新数值到 91
    线程 T92: 更新数值到 92
    线程 T93: 更新数值到 93
    线程 T94: 更新数值到 94
    线程 T95: 更新数值到 95
    线程 T96: 更新数值到 96
    线程 T97: 更新数值到 97
    线程 T98: 更新数值到 98
    线程 T99: 更新数值到 99
    线程 T100: 更新数值到 100
    最终的数值: 100
"""
```
### 死锁与可重入锁
> 死锁：两个或两个以上的进程或线程在执行过程中，因争夺资源而造成的一种互相等待的现象，若无外力作用，他们将无法推进下去，此时称系统处于死锁状态或系统产生了死锁，这些永远在互相等待的进程称为死锁进程

```python
"""
死锁和不可重入锁案例
Deadlocks_and_Non-Recursive_Locks.py
"""
from threading import Lock
import time

mutexA = Lock()
mutexA.acquire()
mutexA.acquire()
print(123)
mutexA.release()
mutexA.release()
"""
muteA是不可重入锁，同一线程多次acquire同一个锁会阻塞自己，所以后面的逻辑不会执行
"""
```

> 可重入锁：threading.RLock 允许统一进程多次获取锁（避免死锁）。RLock内部维护着一个Lock和一个counter变量，counter记录了acquire的次数，从而使得资源可以被多次acquire。直到一个线程内所有的acquire都被release，其他的线程才能获得资源
```python
from threading import RLock as Lock


mutexA = Lock()
mutexA.acquire()
mutexA.acquire()
print(123)
mutexA.release()
mutexA.release()


"""
使用Rlock后可以连续acquire两次，并且不会发生阻塞
输出
    123
"""
```

### 同步锁
- 协调线程间的执行顺序（如生产者-消费者模型）
- 控制并发数量（如限制同时访问数据库的连接数）

#### 信号量
> 控制同时访问资源的线程数量：适用于限制并发数
```python
import threading

semaphore = threading.Semaphore(2) # 最多同时运行2个线程

def task():
    with semaphore:
        print(f"{threading.current_thread().name}正在工作")
        threading.Event().wait(3)

threads = [threading.Thread(target=task) for _ in range(10)]
for i in threads:
    i.start()
for i in threads:
    i.join()
"""
输出
    Thread-1 (task)正在工作
    Thread-2 (task)正在工作
    Thread-3 (task)正在工作
    Thread-4 (task)正在工作
    Thread-5 (task)正在工作
    Thread-6 (task)正在工作
    Thread-7 (task)正在工作
    Thread-8 (task)正在工作
    Thread-9 (task)正在工作
    Thread-10 (task)正在工作
"""
```

#### 条件变量
> 实现线程间通知机制：适用于生产者-消费者模型

```python
"""
条件变量案例
# condition_variable.py
"""
import threading

queue = []
condition = threading.Condition()

def producer():
    with condition:
        queue.append("小问号菜馆A套餐")
        condition.notify()

def consumer():
    with condition:
        while not queue:
            condition.wait()
        data = queue.pop()
        print(f"消费数据: {data}")

threading.Thread(target=producer).start()
threading.Thread(target=consumer).start()

"""
输出
    消费数据: 小问号菜馆A套餐
"""
```

#### 事件
> 简单线程间状态通知：事件常用于跨线程的状态同步
```python
""" 
事件案例
# event.py
"""
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

# 启动线程（建议不要设为 daemon，或者确保主线程等待）
t1 = threading.Thread(target=waiter)
t2 = threading.Thread(target=setter)

t1.start()
t2.start()

# 主线程等待两个子线程完成
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
```

## 线程池
> 线程池通过预创建并复用一组线程，减少频繁创建/销毁线程的开销，适用于I/O密集型任务（如网络请求、文件读写）
- 优点：资源复用、负载均衡、简化线程管理
- 试用场景：批量下载、Web服务器请求处理、数据库并发查询

### 基本操作
> 通过`concurrent.futures.ThreadPoolExecutor`实现
```python
"""
线程基本操作
# basic_thread_operations.py
"""
from concurrent.futures  import ThreadPoolExecutor

def task(n):
    return n * n

# 创建线程池（使用with上下文管理）
with ThreadPoolExecutor(max_workers=2) as executor:
    # 提交任务方式1:submit逐个提交
    future = executor.submit(task, 5)
    print(future.result())
    
    # 提交任务方式2:map批量提交
    results = executor.map(task, [1,2,3])
    print(list(results))

"""
输出
    25
    [1, 4, 9]
"""
```

### 注意事项
- 线程处理：建议设为CPU核心数*2(I/O密集型)
- 异常处理：通过try except 捕获future.result()的异常
- 资源释放：通过shutdown()或上下文管理器自动关闭线程池

### 结合同步机制使用
> 当多个线程访问共享资源（如全局变量、文件）时，需通过同步机制避免资源竞争和数据不一致

```python
from concurrent.futures import ThreadPoolExecutor
from threading import Lock, current_thread

# 共享变量
counter = 0
lock = Lock()


def task():
    global counter
    with lock:
        old_value = counter
        counter += 1
        # 打印当前线程和计数变化
        print(f"[{current_thread().name}] {old_value} → {counter}")


if __name__ == "__main__":
    print("开始执行 100 个并发任务（使用 10 个工作线程）...\n")

    with ThreadPoolExecutor(max_workers=10) as executor:
        # 提交 100 个任务
        futures = [executor.submit(task) for _ in range(100)]

        # 等待所有任务完成（确保异常能被捕获）
        for future in futures:
            future.result()  # 这里无异常，但保持良好习惯

    print(f"\n 最终计数：{counter}")

"""
输出
    [ThreadPoolExecutor-0_0] 0 → 1
    [ThreadPoolExecutor-0_1] 1 → 2
    [ThreadPoolExecutor-0_0] 2 → 3
    [ThreadPoolExecutor-0_0] 3 → 4
    [ThreadPoolExecutor-0_1] 4 → 5
    [ThreadPoolExecutor-0_1] 5 → 6
    [ThreadPoolExecutor-0_4] 6 → 7
    [ThreadPoolExecutor-0_4] 7 → 8
    [ThreadPoolExecutor-0_3] 8 → 9
    [ThreadPoolExecutor-0_6] 9 → 10
    [ThreadPoolExecutor-0_6] 10 → 11
    [ThreadPoolExecutor-0_6] 11 → 12
    [ThreadPoolExecutor-0_6] 12 → 13
    [ThreadPoolExecutor-0_6] 13 → 14
    [ThreadPoolExecutor-0_6] 14 → 15
    [ThreadPoolExecutor-0_6] 15 → 16
    [ThreadPoolExecutor-0_6] 16 → 17
    [ThreadPoolExecutor-0_6] 17 → 18
    [ThreadPoolExecutor-0_6] 18 → 19
    [ThreadPoolExecutor-0_6] 19 → 20
    [ThreadPoolExecutor-0_6] 20 → 21
    [ThreadPoolExecutor-0_6] 21 → 22
    [ThreadPoolExecutor-0_6] 22 → 23
    [ThreadPoolExecutor-0_6] 23 → 24
    [ThreadPoolExecutor-0_6] 24 → 25
    [ThreadPoolExecutor-0_6] 25 → 26
    [ThreadPoolExecutor-0_6] 26 → 27
    [ThreadPoolExecutor-0_6] 27 → 28
    [ThreadPoolExecutor-0_6] 28 → 29
    [ThreadPoolExecutor-0_6] 29 → 30
    [ThreadPoolExecutor-0_6] 30 → 31
    [ThreadPoolExecutor-0_6] 31 → 32
    [ThreadPoolExecutor-0_6] 32 → 33
    [ThreadPoolExecutor-0_6] 33 → 34
    [ThreadPoolExecutor-0_6] 34 → 35
    [ThreadPoolExecutor-0_6] 35 → 36
    [ThreadPoolExecutor-0_6] 36 → 37
    [ThreadPoolExecutor-0_6] 37 → 38
    [ThreadPoolExecutor-0_6] 38 → 39
    [ThreadPoolExecutor-0_6] 39 → 40
    [ThreadPoolExecutor-0_6] 40 → 41
    [ThreadPoolExecutor-0_6] 41 → 42
    [ThreadPoolExecutor-0_6] 42 → 43
    [ThreadPoolExecutor-0_6] 43 → 44
    [ThreadPoolExecutor-0_6] 44 → 45
    [ThreadPoolExecutor-0_6] 45 → 46
    [ThreadPoolExecutor-0_5] 46 → 47
    [ThreadPoolExecutor-0_5] 47 → 48
    [ThreadPoolExecutor-0_5] 48 → 49
    [ThreadPoolExecutor-0_5] 49 → 50
    [ThreadPoolExecutor-0_5] 50 → 51
    [ThreadPoolExecutor-0_5] 51 → 52
    [ThreadPoolExecutor-0_5] 52 → 53
    [ThreadPoolExecutor-0_5] 53 → 54
    [ThreadPoolExecutor-0_5] 54 → 55
    [ThreadPoolExecutor-0_5] 55 → 56
    [ThreadPoolExecutor-0_5] 56 → 57
    [ThreadPoolExecutor-0_5] 57 → 58
    [ThreadPoolExecutor-0_5] 58 → 59
    [ThreadPoolExecutor-0_5] 59 → 60
    [ThreadPoolExecutor-0_5] 60 → 61
    [ThreadPoolExecutor-0_5] 61 → 62
    [ThreadPoolExecutor-0_2] 62 → 63
    [ThreadPoolExecutor-0_8] 63 → 64
    [ThreadPoolExecutor-0_1] 64 → 65
    [ThreadPoolExecutor-0_4] 65 → 66
    [ThreadPoolExecutor-0_4] 66 → 67
    [ThreadPoolExecutor-0_0] 67 → 68
    [ThreadPoolExecutor-0_0] 68 → 69
    [ThreadPoolExecutor-0_9] 69 → 70
    [ThreadPoolExecutor-0_7] 70 → 71
    [ThreadPoolExecutor-0_7] 71 → 72
    [ThreadPoolExecutor-0_7] 72 → 73
    [ThreadPoolExecutor-0_7] 73 → 74
    [ThreadPoolExecutor-0_7] 74 → 75
    [ThreadPoolExecutor-0_7] 75 → 76
    [ThreadPoolExecutor-0_7] 76 → 77
    [ThreadPoolExecutor-0_7] 77 → 78
    [ThreadPoolExecutor-0_7] 78 → 79
    [ThreadPoolExecutor-0_7] 79 → 80
    [ThreadPoolExecutor-0_7] 80 → 81
    [ThreadPoolExecutor-0_7] 81 → 82
    [ThreadPoolExecutor-0_7] 82 → 83
    [ThreadPoolExecutor-0_7] 83 → 84
    [ThreadPoolExecutor-0_7] 84 → 85
    [ThreadPoolExecutor-0_7] 85 → 86
    [ThreadPoolExecutor-0_7] 86 → 87
    [ThreadPoolExecutor-0_7] 87 → 88
    [ThreadPoolExecutor-0_7] 88 → 89
    [ThreadPoolExecutor-0_7] 89 → 90
    [ThreadPoolExecutor-0_7] 90 → 91
    [ThreadPoolExecutor-0_9] 91 → 92
    [ThreadPoolExecutor-0_2] 92 → 93
    [ThreadPoolExecutor-0_5] 93 → 94
    [ThreadPoolExecutor-0_4] 94 → 95
    [ThreadPoolExecutor-0_8] 95 → 96
    [ThreadPoolExecutor-0_1] 96 → 97
    [ThreadPoolExecutor-0_3] 97 → 98
    [ThreadPoolExecutor-0_0] 98 → 99
    [ThreadPoolExecutor-0_6] 99 → 100
    
     最终计数：100
"""
```
