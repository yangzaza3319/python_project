"""
协程相关
"""
## 协程概述
> 协程是用户态的轻量级的线程，由程序自身控制调度，通过协作式多任务实现并发
> 他能够在单线程内挂起和恢复执行，无需操作系统介入，切换开销较小，尤其适用I/O密集型任务（如网络请求、文件读写） 
- 与线程/进程的对比
  - 资源消耗：协程内存占用更低（共享进程内存），线程需要独立栈空间，进程资源消耗最大
  - 切换开销：协程切换在用户态完成，速度极快；线程/进程切换依赖操作系统
  - 适用场景：协程适合高并发I/O操作；线程适合CPU密集型任务；进程适合多核并行计算
- 协程核心优势
  - 高并发：单线程可以处理数千级并发连接(如web服务器) 
  - 无锁机制：避免多线程同步的问题（如死锁、竞态条件）
  - 代码简洁：同步语法写异步逻辑，避免回调地狱
> 回调地狱(Callback Hell)：是异步编程中的一种常见问题，指的是由于多层异步操作嵌套回调函数，导致代码缩进越来越深，逻辑难以阅读和维护的现象

## 协程的实现方式
### 1.生成器函数
> 通过yield暂停执行并传递值：需要手动管理状态，适用于简单的场景

```python
"""
生成器函数
# generator_function.py
"""

def simple_coroutine():
    print("协程启动")
    x = yield
    print(f"接收值：{x}")

coro = simple_coroutine()
next(coro)
try:
    coro.send(10)
except StopIteration:
    print("协程正常结束")

"""
输出
    协程启动
    接收值：10
    协程正常结束
"""
```
### 2.async/await
> 通过asyncio实现异步编程
```python
import asyncio

async def fetch_data(url):
    print(f"请求{url}")
    await asyncio.sleep(1)
    return f"来自{url}的数据"
async def main():
    tasks = [fetch_data('url1'),fetch_data('url2')]
    results = await asyncio.gather(*tasks)
    print(results)

if __name__ == '__main__':
    asyncio.run(main())

"""
    输出
    请求url1
    请求url2
    ['来自url1的数据', '来自url2的数据']
"""
```