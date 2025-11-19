from multiprocessing import Process,JoinableQueue,current_process
import random,time

def consumer(q):
    while True:
        res = q.get()
        time.sleep(random.randint(1,3))
        print(f"进程{current_process().name} 吃了 {res}")
        q.task_done()

def prodecer(q):
    for i in range(10):
        time.sleep(random.randint(1,3))
        res = f"{i}号包子"
        q.put(res)
        print(f"进程{current_process().name}生产了{res}")
    q.join()

if __name__== "__main__" :
    q = JoinableQueue()

    prodecers = [Process(target=prodecer,args=(q,)) for _ in range(1)]
    consumers = [Process(target=consumer,args=(q,),daemon=True) for _ in range(10)]

    for p in prodecers+consumers:
        p.start()
    
    for p in prodecers:
        p.join()
    

    print("所有队列处理完成，程序退出")

"""
输出
    进程Process-4 吃了 2号包子
    进程Process-1生产了3号包子
    进程Process-2 吃了 3号包子
    进程Process-1生产了4号包子
    进程Process-8 吃了 4号包子
    进程Process-1生产了5号包子
    进程Process-9 吃了 5号包子
    进程Process-1生产了6号包子
    进程Process-1生产了7号包子
    进程Process-10 吃了 6号包子
    进程Process-7 吃了 7号包子
    进程Process-1生产了8号包子
    进程Process-6 吃了 8号包子
    进程Process-1生产了9号包子
    进程Process-11 吃了 9号包子
    所有队列处理完成，程序退出
"""

