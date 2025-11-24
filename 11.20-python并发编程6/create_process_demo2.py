from threading import Thread
import time

class MyThread(Thread):
    def __init__(self,name):
        super().__init__()
        self.name=name

    def run(self):
        print(f"{self.name}运行中...")
        time.sleep(1)

if __name__ == '__main__':
    t1 = MyThread("自定义线程")
    t1.start()

"""
输出
    自定义线程运行中...
"""