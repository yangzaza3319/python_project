"""同步阻塞方式"""
from multiprocessing import Pool
import time

def task(x):
    time.sleep(1)
    return x * x

if __name__=="__main__":
    start = time.time()
    with Pool(4) as pool:
        results = []
        for i in range(4):
            res = pool.apply(task,(i,))
            results.append(res)
    print(f"结果：{results},耗时{time.time()-start:.2f}秒")

"""
输出
    结果：[0, 1, 4, 9],耗时4.08秒
"""