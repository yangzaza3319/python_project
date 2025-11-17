"""
manager 代理对象
"""
from multiprocessing import Manager,Process

def update_dict(shared_dict,key):
    shared_dict[key] = key * 2

if __name__ == '__main__':
    with Manager() as manager:
        shared_dict = manager.dict()
        processes = [Process(target=update_dict,args=(shared_dict,i))for i in range(3)]
        for p in processes:
            p.start()
        for p in processes:
            p.join()
        print(shared_dict)

"""
输出
    {1: 2, 0: 0, 2: 4}
"""