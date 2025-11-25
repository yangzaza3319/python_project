""""
协程相关：续
""""
## 协程的基本语法
### 定义协程函数
> 使用async def 声明协程函数
```python
# 伪代码
import asyncio

async def my_coroutine():
    print("协程开始")
    await asyncio.sleep(1)  # 模拟I/O操作
    print("协程结束")
```

### 运行协程
> 协程需要通过事件循环执行

```python
# 伪代码
async def main():
    await my_coroutine()


if __name__ == "__main__":
    asyncio.run(main())
```

## 事件循环
> 事件循环是协程的调度核心。负责执行、切换和监控协程任务
```python
"""
协程的事件循环
# event_loop_of_coroutines.py
"""
import asyncio


async def task1():
    print("任务1开始")
    await asyncio.sleep(2)
    print("任务1结束")

async def task2():
    print("任务2开始")
    await asyncio.sleep(1)
    print("任务2结束")

async def main():
    await asyncio.gather(task1(), task2())

if __name__ == "__main__":
    asyncio.run(main())

"""
输出
    任务1开始
    任务2开始
    任务2结束
    任务1结束
"""
```
## 进阶用法
### 任务
> 将协程封装为任务，更灵活的控制执行

```python
# 伪代码
async def main():
    task = asyncio.create_task(my_coroutines())
    await task
```

### 超时控制
> 设置协程执行的超时时间

```python
# 伪代码
async def slow_task():
    awit asyncio.sleep(10)
async def main():
    try:
        await asyncio.wait_for(slow_task(),timeout=3)
    except asyncio.TimeoutError:
            print("任务超时")
```

### 协程同步
> 使用锁Lock保护共享资源

```python
lock = asyncio.Lock()

async def safe_write():
    async with lock:
        pass
```
