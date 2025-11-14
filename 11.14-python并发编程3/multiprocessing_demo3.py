import multiprocessing
import time

def worker(num):
    print(f"进程{num}开始工作")
    time.sleep(2)
    print(f"进程{num}工作结束")
if __name__=='__main__':
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=worker,args=(i,))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()

    print("所有进程完成，主进程退出...")


"""
输出 
    进程0开始工作
    进程2开始工作
    进程1开始工作
    进程1工作结束
    进程2工作结束
    进程0工作结束
    所有进程完成，主进程退出...
"""