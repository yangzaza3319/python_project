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
    with Pool(4) as pool:
        async_results = [pool.apply_async(task,(i,))for i in range(4)]
        results = [res.get() for res in async_results]
    print(f"结果:{results},耗时:{time.time()-start:.2f}秒")

"""
输出
    结果:[0, 1, 4, 9],耗时:1.05秒
"""