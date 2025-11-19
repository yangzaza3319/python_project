from  multiprocessing import Process,Queue,current_process
import time,random,os

def consumer(q):
    while True:
        res = q.get()
        if res is None:
            break
        time.sleep(random.randint(1,3))
        print(f"进程{current_process().name}吃{res}")

def producer(q):
    for i in range(10):
        time.sleep(random.randint(1,3))
        res = f"包子{i}"
        q.put(res)
        print(f"进程{current_process().name}生产了{res}")

if __name__=="__main__":
    q = Queue()

    producers = [Process(target=producer,args=(q,))for _ in range(1)]
    consumers = [Process(target=consumer,args=(q,))for _ in range(10)]

    for p in producers+consumers:
        p.start()
    
    for p in producers:
        p.join()
    
    for _ in range(len(consumers)):
        q.put(None)
    
    for c in consumers:
        c.join()

"""
输出
    进程Process-1生产了包子0
    进程Process-1生产了包子1
    进程Process-1生产了包子2
    进程Process-4吃包子1
    进程Process-7吃包子0
    进程Process-1生产了包子3
    进程Process-5吃包子2
    进程Process-10吃包子3
    进程Process-1生产了包子4
    进程Process-1生产了包子5
    进程Process-3吃包子4
    进程Process-8吃包子5
    进程Process-1生产了包子6
    进程Process-1生产了包子7
    进程Process-1生产了包子8
    进程Process-11吃包子6
    进程Process-9吃包子7
    进程Process-1生产了包子9
    进程Process-6吃包子8
    进程Process-2吃包子9
"""