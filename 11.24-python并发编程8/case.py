"""
基于变量同步机制，实现多进程-生产/消费者模型完整版本
"""
import queue
import threading

def producer(i):
    with condition:
        queue.append(f"小问号菜品{i}")
        condition.notify()


def consumer(i):
    with condition:
        while not queue and not producer_done:
            condition.wait()
        if queue:
            data = queue.pop()
        elif producer_done:
            return
        print(f"消费者{i} 的消费数据:{data}")


if __name__ == '__main__':
    queue = []
    condition = threading.Condition()
    producer_done = False

    pt =  [threading.Thread(target=producer,args=(i,)) for i in range(3)]
    ct = [threading.Thread(target=consumer,args=(i,)) for i in range(10)]

    for t in pt+ct:
        t.start()
    with condition:
        producer_done = True
        condition.notify_all()
    for t in pt:
        t.join()
    for t in ct:
        t.join()
    print("主进程/线程处理完成")


"""
输出
    消费者0 的消费数据:小问号菜品2
    消费者1 的消费数据:小问号菜品1
    消费者2 的消费数据:小问号菜品0
    主进程/线程处理完成
"""