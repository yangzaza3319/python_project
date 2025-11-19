import multiprocessing
import time

def calculate_square(num,queue):
    result = num * num
    print(
        f"进程{multiprocessing.current_process().name }计算 {num} 的平方,结果是{result}"
    )
    time.sleep(1)
    queue.put(result)

if __name__=="__main__":
    numbers = [1,2,3,4,5]
    queue = multiprocessing.Queue()
    processes = []

    for num in numbers:
        p = multiprocessing.Process(target=calculate_square,args=(num,queue))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
    
    results = []

    while not queue.empty():
        results.append(queue.get())

    print(f"所有进程计算结果:{results}")
    print("主进程结束")

"""
输出 
    进程Process-1计算 1 的平方,结果是1
    进程Process-2计算 2 的平方,结果是4
    进程Process-5计算 5 的平方,结果是25
    进程Process-4计算 4 的平方,结果是16
    进程Process-3计算 3 的平方,结果是9
    所有进程计算结果:[1, 4, 16, 25, 9]
    主进程结束
"""