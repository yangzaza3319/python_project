"""
process_lock_and_seg.py
"""
from multiprocessing import Process,Value,Lock

def safe_increment(num,lock):
    with lock:
        num.value += 1
    
if __name__ == "__main__":
    counter = Value("i",0)
    lock = Lock()

    processes = [Process(target=safe_increment,args=(counter,lock)) for _ in range(5)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print(counter.value)

"""
输出
    5
"""