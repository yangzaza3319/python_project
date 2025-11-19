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

"""
输出
    结果[0, 1, 4, 9]，耗时1.05秒
"""

from multiprocessing import Pool

def square(x):
    return x*x

def collect_result(result,result_list):
    result_list.append(result)

if __name__=="__main__":
    with Pool(4) as pool:
        results = []
        for i in range(10):
            pool.apply_async(square,(i,),callback=lamba r:collect_result(r,results))
            pool.close()
            pool.join()
            print("最后结果:",sorted(results))