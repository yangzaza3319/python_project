from multiprocessing import Process

def func(name):
    print("hello %s" %name)
    print("子进程运行完成，输出了name变量的内容")

if __name__ == '__main__':
    p =Process(target=func,args=('niuniu',))
    p.start()
    p.join()    # 阻塞等待完成
    print("主程序执行完毕，程序退出")

"""
输出 
    hello niuniu
    子进程运行完成，输出了name变量的内容
    主程序执行完毕，程序退出
"""


