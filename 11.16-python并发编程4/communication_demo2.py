"""
案例1
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