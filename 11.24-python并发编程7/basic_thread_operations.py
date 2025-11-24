"""
线程基本操作
# basic_thread_operations.py
"""
from concurrent.futures  import ThreadPoolExecutor

def task(n):
    return n * n

with ThreadPoolExecutor(max_workers=2) as executor:
    future = executor.submit(task, 5)
    print(future.result())

    results = executor.map(task, [1,2,3])
    print(list(results))

"""
输出
    25
    [1, 4, 9]
"""
