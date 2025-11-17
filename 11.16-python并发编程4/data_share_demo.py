"""
原生共享内存方案（Value/Array）
"""
from  multiprocessing import Process,Value,Array

def increment(num):
    num.value += 1

if __name__ == '__main__':
    counter = Value('i',0)
    arr = Array('d',[0.0,1.0,2.0])
    processes = [Process(target=increment,args=(counter,)) for _ in range(5)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print(counter.value)

"""
输出 
    3
"""