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