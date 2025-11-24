## 进程池
> 进程池是预先创建并管理一组子进程的技术，用于高效处理批量任务。通过复用固定数量的进程，避免频繁创建/销毁进程的开销，提升cpu密集型任务的性能

- 在成千上万个任务需要被执行时，我们不能无限制的根据任务开启或结束进程，因为创建/销毁进程需要消耗时间；即使已经启动了，操作系统也不能同时处理上千万的进程，这样反而会影响程序的效率
- 定义一个池子，在里面放上固定数量的进程，有需求来了，就拿一个池子中的进程来处理任务，等到处理完毕，进程并不关闭，而是将进程再放回进程池中继续等待任务；如果有很多任务都需要执行，池中的进程数量不够，任务就要等待之前的进程执行任务完毕归来，拿到空闲进程才能继续执行；也就是说，池子中进程的数量是固定的，这样不会增加操作系统的调度难度，还节省了开闭进程的时间，也一定程度上能够实现并发效果
- multiprocessing.Pool是mutiprocessing模块中一个非常有用的工具，用于管理进程池。它允许你并行地执行函数，并且可以轻松地分配多个任务到多个进程中执行，从而提高程序的执行效率，Pool使得多进程编程的管理变得更加容易，尤其是在需要并行处理大量数据时

### 基本概念
> Pool 是进程的集合，用于执行并行任务，它提供了一种简化的接口来并行执行多个任务，将任务分配给多个进程并管理他们的执行

好处
- 通过限制并发进程的数量，可以有效的管理资源消耗
- 可以自动调度和分配任务到多个进程
- 提供了多种方法（如apply、map、apply_async、map_async）来调度任务并收集结果

#### 创建进程池
```python
from multiprocessing import Pool

pool = Pool(processes=4)
```

#### 关闭进程池
```python
pool.close()
pool.join()
```

### 提交任务
> 同步阻塞方式
```python
from multiprocessing import Pool
import time

def task(x):
    time.sleep(1)  # 模拟耗时操作
    return x * x

if __name__=="__main__":
    start = time.time()
    with Pool(4) as pool:
        results = []
        for i in range(4):
            res = pool.apply(task,(i,))
            results.append(res)    # 同步提交，逐个执行
    print(f"结果：{results},耗时{time.time()-start:.2f}秒")

"""
输出
    结果：[0, 1, 4, 9],耗时4.08秒
"""
```

> 异步非阻塞方式
```python
"""
异步非阻塞方式
"""

from multiprocessing import Pool
import time

def task(x):
    time.sleep(1)
    return x*x

if __name__=="__main__":
    start = time.time()
    with Pool(4) as pool: # 自动调用pool.close() 和pool.join()
        async_results = [pool.apply_async(task,(i,))for i in range(4)]  # 异步提交任务
        results = [res.get() for res in async_results]  # 阻塞直到所有结果返回
    print(f"结果:{results},耗时:{time.time()-start:.2f}秒")

"""
输出
    结果:[0, 1, 4, 9],耗时:1.05秒
"""
```

> 批量处理
```python
from multiprocessing import Pool
import time

def task(x):
    time.sleep(1)
    return x*x

if __name__ == "__main__":
    start = time.time()
    with Pool(4) as pool :
        results = pool.map(task,range(4)) # 批量提交
    print(f"结果{results}，耗时{time.time()-start:.2f}秒")
```


### 回调函数
> 需要回调函数的场景：进程池中的任何一个任务处理完了，立刻通知主进程处理结果；主进程需要调用回调函数来处理这个结果
> 直接把耗时间（且已经阻塞）的任务放到进程池中，然后指定回调函数（有主程序负责执行），这样主进程在执行回调函数时就省去了I/O的过程，直接拿到的是任务的结果
> 在python的多进程编程中，apply_async的回调函数(callback)是一种异步处理任务结果的机制，它允许在子进程完成任务后自动触发特定的逻辑，而无需阻塞主进程

#### 回调函数的执行机制
- 运行环境
  回调函数在主进程中执行，而非子进程
  这意味着回调函数内无法直接操作子进程的变量或资源。回调中应避免耗时操作，否则会阻塞主进程
- 参数传递
  回调函数默认接受 任务的返回值 作为唯一参数
  如果需要传递额外参数。可以通过闭包或者全局变量实现
 
> 示例代码
```python
from multiprocessing import Pool

def square(x):
    return x*x

def collect_result(result,result_list):
    result_list.append(result)

if __name__=="__main__":
    with Pool(4) as pool:
        results = []
        for i in range(10):
            pool.apply_async(square,(i,),callback=lambda r:collect_result(r,results))
        pool.close()
        pool.join()
        print("最后结果:",sorted(results))

"""
输出
    最后结果: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
"""
```

### 案例：实时爬取网页内容并存储至本地文件
```python

```